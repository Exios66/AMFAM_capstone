"""Majority-vote tally: K independent agent runs on a slice, tallied per image.

Each "agent" is an independent run of the eval runner on the SAME dataset with
the SAME prompt version but a DIFFERENT sampling temperature (so the votes are
independent draws, not a replay of one deterministic run). The agent runs
register no Braintrust scorers (``--scorers none``) — scoring happens locally
in the tally, which is the point of the experiment.

The v19 prompt (the vote fork of v18.1) frames each model as one independent
vote in a K-member committee; every run also emits the ``<confidence>``
self-report, which the tally uses to break ties.

Default usage (print the commands, spend nothing):

    python scripts/braintrust/majority_vote_tally.py

Execute the K agent runs, then tally:

    python scripts/braintrust/majority_vote_tally.py --run-votes --k 3

Tally only (reuse existing agent manifests):

    python scripts/braintrust/majority_vote_tally.py --tally-only

Output: ``reports/monte_carlo/majority_vote_tally.md`` — per-run accuracy,
majority-vote accuracy (and delta), agreement rate, per-class vote accuracy.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))  # noqa: E402

from src.monte_carlo import safe_div  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
RUNNER = ROOT / "scripts" / "braintrust" / "braintrust_openrouter_input.py"
MANIFESTS_DIR = ROOT / "reports" / "manifests"
OUTPUT_PATH = ROOT / "reports" / "monte_carlo" / "majority_vote_tally.md"

DEFAULT_TEMPERATURES = (0.1, 0.3, 0.6)


def agent_manifest_path(prompt_version: str, idx: int) -> Path:
    return MANIFESTS_DIR / f"vote_{prompt_version}_agent{idx}.jsonl"


def run_agent(dataset: str, prompt_version: str, idx: int, temperature: float,
              reasoning_effort: str | None, limit: int | None,
              samples_per_class: int | None, agent_account: bool,
              research_funding: bool) -> None:
    """Run one agent eval via the runner; the manifest is the durable vote."""
    cmd = [
        sys.executable, str(RUNNER),
        "--dataset", dataset,
        "--prompt-version", prompt_version,
        "--temperature", str(temperature),
        "--experiment-name", f"vote_{prompt_version}_agent{idx}",
        "--manifest", str(agent_manifest_path(prompt_version, idx)),
        "--scorers", "none",
        "--no-sound",
    ]
    if reasoning_effort:
        cmd += ["--reasoning-effort", reasoning_effort]
    if limit:
        cmd += ["--limit", str(limit)]
    if samples_per_class:
        cmd += ["--samples-per-class", str(samples_per_class)]
    if agent_account:
        cmd.append("--agent")
    if research_funding:
        cmd.append("--research-funding")
    print(f"\n>>> {' '.join(cmd)}")
    subprocess.run(cmd, cwd=ROOT, check=True)


def load_agent_rows(path: Path) -> dict[str, dict]:
    """Return {filename: record} (last state per filename) for one agent."""
    final: dict[str, dict] = {}
    for line in path.read_text(encoding="utf-8").splitlines()[1:]:
        if not line.strip():
            continue
        record = json.loads(line)
        final[record["filename"]] = record
    return final


def tally(manifests: list[Path], prompt_version: str) -> None:
    """Majority-vote the agents' per-image predictions and write the report."""
    agents = [load_agent_rows(p) for p in manifests]
    filenames = set()
    for rows in agents:
        filenames |= {fn for fn, r in rows.items() if r.get("status") == "completed"}
    filenames = sorted(filenames)

    per_agent = [sum(1 for fn in filenames
                     if (agents[i].get(fn) or {}).get("predicted", "").strip().lower()
                     == (agents[i].get(fn) or {}).get("expected")) for i in range(len(agents))]

    vote_correct = 0
    vote_total = 0
    agreement = Counter()
    per_class = Counter()
    per_class_correct = Counter()
    for fn in filenames:
        records = [agents[i].get(fn) for i in range(len(agents))]
        expected = next(r["expected"] for r in records if r)
        votes = Counter()
        conf_sum: dict[str, float] = defaultdict(float)
        for r in records:
            if not r or r.get("status") != "completed":
                continue
            pred = (r.get("predicted") or "").strip().lower()
            if not pred:
                continue
            votes[pred] += 1
            conf_sum[pred] += float(r.get("self_report") or 0.0)
        if not votes:
            continue
        best = max(votes.values())
        winners = [label for label, count in votes.items() if count == best]
        if len(winners) > 1:
            # Tie: prefer the label with the highest summed self-reported confidence.
            winners.sort(key=lambda label: (conf_sum[label], label), reverse=True)
        final_vote = winners[0]
        vote_total += 1
        correct = final_vote == expected
        vote_correct += int(correct)
        agreement[votes[final_vote]] += 1
        per_class[expected] += 1
        per_class_correct[expected] += int(correct)

    vote_acc = safe_div(vote_correct, vote_total)
    single_accs = [safe_div(c, vote_total) for c in per_agent]
    best_single = max(single_accs) if single_accs else 0.0

    lines = [
        f"# Majority-Vote Tally (v{prompt_version}, K={len(agents)})",
        "",
        "Each agent is an independent run of the same prompt at a different "
        "sampling temperature; the tally majority-votes their predictions per "
        "image (ties broken by summed `<confidence>` self-report).",
        "",
        "## Per-run accuracy",
        "",
        "| agent | rows | correct | accuracy |",
        "|---|---:|---:|---:|",
    ]
    for i, rows in enumerate(agents):
        rows = {fn: r for fn, r in rows.items() if r.get("status") == "completed"}
        correct = per_agent[i]
        lines.append(f"| agent{i} | {len(filenames)} | {correct} | "
                     f"{safe_div(correct, len(filenames)):.3f} |")
    lines += [
        "",
        "## Majority vote",
        "",
        "| metric | value |",
        "|---|---:|",
        f"| images | {vote_total} |",
        f"| majority-vote accuracy | {vote_acc:.3f} |",
        f"| best single agent | {best_single:.3f} |",
        f"| **delta vs best single agent** | **{vote_acc - best_single:+.3f}** |",
        f"| unanimous (K/{len(agents)}) images | {agreement[len(agents)]} |",
        f"| K-1 majority images | {agreement[len(agents) - 1]} |",
        "",
    ]
    lines += ["## Per-class vote accuracy", "", "| class | correct | total | accuracy |",
              "|---|---:|---:|---:|"]
    for cls in sorted(per_class):
        total = per_class[cls]
        correct = per_class_correct[cls]
        lines.append(f"| {cls} | {correct} | {total} | {safe_div(correct, total):.3f} |")
    lines.append("")

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Report saved: {OUTPUT_PATH}")
    print("\n" + "\n".join(lines[:18]))


def run() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dataset", default="fixed_size_sampled",
                        help="Dataset slice to vote on (default: fixed_size_sampled)")
    parser.add_argument("--prompt-version", default="v19",
                        help="Prompt version for the agents (default: v19, the vote fork)")
    parser.add_argument("--k", type=int, default=3,
                        help="Number of independent agent runs (default: 3)")
    parser.add_argument("--temperatures", default=None,
                        help=f"Comma-separated temperatures per agent "
                             f"(default: {','.join(map(str, DEFAULT_TEMPERATURES))})")
    parser.add_argument("--reasoning-effort", default=None,
                        help="Reasoning effort for the agent runs (qwen default: high)")
    parser.add_argument("--limit", type=int, default=None,
                        help="Classify only the first N images")
    parser.add_argument("--samples-per-class", type=int, default=None,
                        help="Deterministically subsample N images per class")
    parser.add_argument("--agents", action="store_true",
                        help="Run under the agent Braintrust account (--agent)")
    parser.add_argument("--research-funding", action="store_true",
                        help="Use the RESEARCH_FUNDING_API_KEY for the agent runs")
    parser.add_argument("--run-votes", action="store_true",
                        help="Execute the agent evals (spends model credits)")
    parser.add_argument("--tally-only", action="store_true",
                        help="Skip running agents; tally from existing manifests")
    args = parser.parse_args()

    if args.temperatures:
        temperatures = tuple(float(x) for x in args.temperatures.split(",") if x.strip())
    else:
        temperatures = DEFAULT_TEMPERATURES[: args.k]
    if len(temperatures) != args.k:
        sys.exit(f"Error: expected {args.k} temperatures, got {len(temperatures)}")

    manifests = [agent_manifest_path(args.prompt_version, i) for i in range(args.k)]

    if args.tally_only:
        # Tally only: reuse existing agent manifests, run nothing.
        pass
    elif args.run_votes:
        for i, temperature in enumerate(temperatures):
            run_agent(args.dataset, args.prompt_version, i, temperature,
                      args.reasoning_effort, args.limit, args.samples_per_class,
                      args.agents, args.research_funding)
    else:
        # Dry run: print what would run (mirrors monte_carlo_verify.py).
        print("Vote agent commands (run with --run-votes to execute):")
        for i, temperature in enumerate(temperatures):
            print(f"\n  python scripts/braintrust/braintrust_openrouter_input.py "
                  f"--dataset {args.dataset} --prompt-version {args.prompt_version} "
                  f"--temperature {temperature} --experiment-name "
                  f"vote_{args.prompt_version}_agent{i} "
                  f"--manifest reports/manifests/vote_{args.prompt_version}_agent{i}.jsonl "
                  f"--scorers none --no-sound")

    missing = [p for p in manifests if not p.exists()]
    if missing:
        sys.exit(f"Error: missing agent manifests: {', '.join(map(str, missing))} "
                 f"(run with --run-votes)")
    tally(manifests, args.prompt_version)


if __name__ == "__main__":
    run()
