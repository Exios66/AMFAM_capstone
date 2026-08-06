"""Build the GitHub wiki from the Quarto site source.

Mirrors the Posit Cloud site as a self-contained wiki at
``Exios66/AMFAM_capstone.wiki.git``. Every page is converted from qmd to
plain markdown (YAML stripped, callouts unwrapped), images are copied into
``assets/``, and the manuscript gets inline ``(Author, Year)`` citations plus
a full APA References section drawn from ``references.bib``.

Usage:
    python scripts/site/build_wiki.py          # clone + build + commit + push
    python scripts/site/build_wiki.py --no-push  # build only
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
WEBSITE = ROOT / "website"
WIKI_BUILD = ROOT / ".wiki-build"
WIKI_REMOTE = "https://github.com/Exios66/AMFAM_capstone.wiki.git"

sys.path.insert(0, str(ROOT))
from src.apa7 import format_stats_apa  # noqa: E402

# ---------------------------------------------------------------------------
# Navigation — mirrors website/_quarto.yml sidebar
# ---------------------------------------------------------------------------

SIDEBAR = [
    ("Home", "Home"),
    ("Headline results", "Headline-results"),
    ("Misclassification appendix", "Misclassifications"),
    ("---", None),
    ("Methods & Reference", None),
    ("  Overview", "Methods-overview"),
    ("  Classes", "Classes"),
    ("  Document processor", "Document-processor"),
    ("  Prompt rules provenance", "Prompt-rules-provenance"),
    ("  CLI commands", "CLI-commands"),
    ("---", None),
    ("Results", None),
    ("  Experiment reports", "Experiment-reports"),
    ("  Experiment log", "Experiment-log"),
    ("  Confusion matrices", "Confusion-matrices"),
    ("  Gemini 800 notes", "Gemini-800-notes"),
    ("  Gemini 160 notes", "Gemini-160-notes"),
    ("---", None),
    ("Prompt Evolution", None),
    ("  Prompt changelog", "Prompt-changelog"),
    ("  Enhancements", "Enhancements"),
    ("---", None),
    ("Cost Analysis", None),
    ("  Cost estimation", "Cost-estimation"),
    ("  Cost projections", "Cost-projections"),
    ("---", None),
    ("Monte Carlo", None),
    ("  Overview", "MC-overview"),
    ("  Ensemble voting", "Ensemble-voting"),
    ("  Routing / abstention", "Routing-abstention"),
    ("  Failure pipeline", "Failure-pipeline"),
    ("  Prompt ablation", "Prompt-ablation"),
    ("  Exemplar mining", "Exemplar-mining"),
    ("  ALE + stop-words", "ALE-stopword"),
    ("  Verification", "Verification"),
    ("  Corpus summary", "Corpus-summary"),
    ("---", None),
    ("Research Memos", None),
    ("  Accuracy arc", "Accuracy-arc"),
    ("  Confidence routing", "Confidence-routing"),
    ("  Cost per image", "Cost-per-image"),
    ("  Ensemble voting", "Ensemble-voting-memo"),
    ("  Exemplar mining", "Exemplar-mining-memo"),
    ("  Failure pipeline", "Failure-pipeline-memo"),
    ("  Generalization falloff", "Generalization-falloff"),
    ("  Hardest classes", "Hardest-classes"),
    ("  Hasty-stop words", "Hasty-stop-words"),
    ("  Model comparison", "Model-comparison"),
    ("---", None),
    ("Interactive", None),
    ("  Cost calculator", "Cost-calculator"),
    ("  Experiment explorer", "Experiment-explorer"),
    ("---", None),
    ("Notebooks", None),
    ("  01 Env setup", "Notebook-01"),
    ("  02 Sampling + Braintrust", "Notebook-02"),
    ("  03 Watchers + evaluators", "Notebook-03"),
    ("  04 Interactive cost", "Notebook-04"),
    ("---", None),
    ("Appendix", None),
    ("  Misclassifications", "Misclassifications"),
    ("---", None),
    ("Chat Examples", "Chats"),
    ("Manuscript", "Manuscript"),
]

# ---------------------------------------------------------------------------
# qmd → wiki md conversion
# ---------------------------------------------------------------------------

YAML_FRONT_RE = re.compile(r"^---\n[\s\S]*?\n---\n?", flags=re.MULTILINE)
CALLOUT_RE = re.compile(r"^:::\s*(\w+)\s*\n([\s\S]*?)^:::\s*$", flags=re.MULTILINE)


def strip_yaml(text: str) -> str:
    return YAML_FRONT_RE.sub("", text)


def unwrap_callouts(text: str) -> str:
    """Convert Quarto callouts (``::: note``) to bold-headed paragraphs."""
    def _replace(m: re.Match) -> str:
        kind = m.group(1).capitalize()
        body = m.group(2).strip()
        return f"**{kind}.** {body}"
    return CALLOUT_RE.sub(_replace, text)


def rewrite_image_paths(text: str) -> str:
    """Rewrite ``../charts/X.svg`` → ``assets/charts/X.svg`` etc."""
    def _img(m: re.Match) -> str:
        alt, path = m.group(1), m.group(2)
        path = path.replace("../charts/", "assets/charts/")
        path = path.replace("../figures/", "assets/figures/")
        path = path.replace("../chat_images/", "assets/chat_images/")
        return f"![{alt}]({path})"
    text = re.sub(r"!\[([^\]]*)\]\(([^)]+\.(?:png|svg|jpg|jpeg))\)", _img, text)
    return text


def rewrite_internal_links(text: str) -> str:
    """Convert ``page.html`` links to wiki ``[[Page]]`` or ``[text](Page)``."""
    def _link(m: re.Match) -> str:
        label, target = m.group(1), m.group(2)
        if target.endswith(".html"):
            wiki_name = Path(target).stem.replace("-", " ").title().replace(" ", "-")
            return f"[{label}]({wiki_name})"
        if target.endswith(".qmd"):
            wiki_name = Path(target).stem.replace("-", " ").title().replace(" ", "-")
            return f"[{label}]({wiki_name})"
        return m.group(0)
    return re.sub(r"\[([^\]]+)\]\(([^)]+\.(?:html|qmd))\)", _link, text)


def convert_qmd(text: str) -> str:
    """Convert a qmd page to wiki-friendly markdown."""
    text = strip_yaml(text)
    text = unwrap_callouts(text)
    text = rewrite_image_paths(text)
    text = rewrite_internal_links(text)
    text = format_stats_apa(text)
    return text


# ---------------------------------------------------------------------------
# BibTeX → APA References
# ---------------------------------------------------------------------------

def parse_bib(path: Path) -> list[dict]:
    """Parse a BibTeX file into a list of entry dicts."""
    text = path.read_text(encoding="utf-8")
    entries = []
    for m in re.finditer(r"@(\w+)\{([^,]+),", text):
        etype, key = m.group(1), m.group(2)
        # Find the matching closing brace for this entry
        start = m.end()
        depth = 1
        i = start
        while i < len(text) and depth > 0:
            if text[i] == "{":
                depth += 1
            elif text[i] == "}":
                depth -= 1
            i += 1
        body = text[start:i - 1]
        fields = {}
        for fm in re.finditer(r"(\w+)\s*=\s*\{((?:[^{}]|\{[^}]*\})*)\}", body):
            fields[fm.group(1).lower()] = fm.group(2).strip()
        entries.append({"type": etype, "key": key, **fields})
    return entries


def format_apa_reference(e: dict) -> str:
    """Format a single bib entry as an APA 7 reference."""
    author = e.get("author", "Unknown")
    year = e.get("year", "n.d.")
    title = e.get("title", "")
    # Strip LaTeX commands from title
    title = re.sub(r"\\[a-z]+\{([^}]*)\}", r"\1", title)
    title = re.sub(r"[{}]", "", title)
    # Clean author: strip outer braces, convert BibTeX "Last, First" to "Last, F."
    author_clean = re.sub(r"[{}]", "", author)

    if e["type"] == "article":
        journal = e.get("journal", "")
        vol = e.get("volume", "")
        pages = e.get("pages", "")
        doi = e.get("doi", "")
        ref = f"{author_clean} ({year}). {title}. *{journal}*"
        if vol:
            ref += f", *{vol}*"
        if pages:
            ref += f", {pages}"
        ref += "."
        if doi:
            ref += f" https://doi.org/{doi}"
        return ref
    elif e["type"] == "inproceedings":
        booktitle = e.get("booktitle", "")
        pages = e.get("pages", "")
        doi = e.get("doi", "")
        ref = f"{author_clean} ({year}). {title}. In *{booktitle}*"
        if pages:
            ref += f" (pp. {pages})"
        ref += "."
        if doi:
            ref += f" https://doi.org/{doi}"
        return ref
    elif e["type"] == "misc":
        how = e.get("howpublished", "")
        note = e.get("note", "")
        ref = f"{author_clean} ({year}). {title}."
        if how:
            ref += f" {how}."
        if note:
            ref += f" {note}."
        return ref
    elif e["type"] == "book":
        publisher = e.get("publisher", "")
        ref = f"{author_clean} ({year}). *{title}*. {publisher}."
        return ref
    else:
        return f"{author_clean} ({year}). {title}."


def build_references_section(bib_path: Path) -> str:
    """Build a References section from references.bib in APA 7 format."""
    entries = parse_bib(bib_path)
    refs = []
    for e in entries:
        refs.append(format_apa_reference(e))
    refs.sort(key=lambda r: r.lower())
    lines = ["\n## References\n"]
    for r in refs:
        lines.append(f"- {r}")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Citation key → inline (Author, Year)
# ---------------------------------------------------------------------------

def build_cite_map(bib_path: Path) -> dict[str, str]:
    """Map ``@key`` → ``(Author, Year)`` for inline citations."""
    entries = parse_bib(bib_path)
    m = {}
    for e in entries:
        author = e.get("author", "Unknown")
        year = e.get("year", "n.d.")
        # Extract last name of first author: handles "{Last, First}" and "Last and ..."
        first_author = author.split(" and ")[0].strip()
        # Strip outer braces if present: {{Raj GV}, Ananth} → {Raj GV}, Ananth
        first_author = first_author.strip("{}")
        if "," in first_author:
            last = first_author.split(",")[0].strip().strip("{}")
        else:
            last = first_author.split()[0].strip("{}")
        m[e["key"]] = f"({last}, {year})"
    return m


def inline_citations(text: str, cite_map: dict[str, str]) -> str:
    """Replace ``[@key]`` and ``[@key1;@key2]`` with ``(Author, Year)`` forms."""
    def _cite(m: re.Match) -> str:
        keys_str = m.group(1)
        keys = [k.strip() for k in keys_str.split(";")]
        parts = []
        for k in keys:
            if k in cite_map:
                parts.append(cite_map[k].strip("()"))
            else:
                parts.append(k)
        if len(parts) == 1:
            return f"({parts[0]})"
        return "(" + "; ".join(parts) + ")"
    return re.sub(r"\[@([^\]]+)\]", _cite, text)


# ---------------------------------------------------------------------------
# Page build
# ---------------------------------------------------------------------------

QMD_PAGES = [
    # (source qmd, wiki page name)
    ("index.qmd", "Home"),
    ("results/headline-results.qmd", "Headline-results"),
    ("methods/overview.qmd", "Methods-overview"),
    ("methods/classes.qmd", "Classes"),
    ("methods/document-processor.qmd", "Document-processor"),
    ("methods/prompt-rules-provenance.qmd", "Prompt-rules-provenance"),
    ("methods/cli-commands.qmd", "CLI-commands"),
    ("results/experiment-reports.qmd", "Experiment-reports"),
    ("results/experiment-log.qmd", "Experiment-log"),
    ("results/confusion-matrices.qmd", "Confusion-matrices"),
    ("results/gemini-800-notes.qmd", "Gemini-800-notes"),
    ("results/gemini-160-notes.qmd", "Gemini-160-notes"),
    ("prompts/prompt-changelog.qmd", "Prompt-changelog"),
    ("prompts/enhancements.qmd", "Enhancements"),
    ("cost/cost-estimation.qmd", "Cost-estimation"),
    ("cost/cost-projections.qmd", "Cost-projections"),
    ("montecarlo/overview.qmd", "MC-overview"),
    ("montecarlo/ensemble-voting.qmd", "Ensemble-voting"),
    ("montecarlo/routing-abstention.qmd", "Routing-abstention"),
    ("montecarlo/failure-pipeline.qmd", "Failure-pipeline"),
    ("montecarlo/prompt-ablation.qmd", "Prompt-ablation"),
    ("montecarlo/exemplar-mining.qmd", "Exemplar-mining"),
    ("montecarlo/ale-stopword.qmd", "ALE-stopword"),
    ("montecarlo/verification.qmd", "Verification"),
    ("montecarlo/corpus-summary.qmd", "Corpus-summary"),
    ("memos/accuracy-arc.qmd", "Accuracy-arc"),
    ("memos/confidence-routing.qmd", "Confidence-routing"),
    ("memos/cost-per-image.qmd", "Cost-per-image"),
    ("memos/ensemble-voting.qmd", "Ensemble-voting-memo"),
    ("memos/exemplar-mining.qmd", "Exemplar-mining-memo"),
    ("memos/failure-pipeline.qmd", "Failure-pipeline-memo"),
    ("memos/generalization-falloff.qmd", "Generalization-falloff"),
    ("memos/hardest-classes.qmd", "Hardest-classes"),
    ("memos/hasty-stop-words.qmd", "Hasty-stop-words"),
    ("memos/model-comparison.qmd", "Model-comparison"),
    ("interactive/cost-calculator.qmd", "Cost-calculator"),
    ("interactive/experiment-explorer.qmd", "Experiment-explorer"),
    ("appendix/misclassifications.qmd", "Misclassifications"),
    ("chats.qmd", "Chats"),
    ("manuscript.qmd", "Manuscript"),
]


def add_footer(text: str) -> str:
    """Append a Posit Cloud + repo footer."""
    footer = (
        "\n\n---\n"
        "*Published via [Posit Cloud](https://connect.posit.cloud/jackjburleson/content/019fd440-9bbf-1a22-cf30-a36183d9c7d4)"
        " · [GitHub repo](https://github.com/Exios66/AMFAM_capstone)*\n"
    )
    return text + footer


def build_wiki_pages(wiki_dir: Path) -> None:
    bib_path = WEBSITE / "references.bib"
    cite_map = build_cite_map(bib_path)

    for qmd_rel, wiki_name in QMD_PAGES:
        src = WEBSITE / qmd_rel
        if not src.exists():
            print(f"  skip (missing): {qmd_rel}")
            continue
        text = src.read_text(encoding="utf-8")
        text = convert_qmd(text)
        # Special: manuscript gets inline citations + references
        if qmd_rel == "manuscript.qmd":
            text = inline_citations(text, cite_map)
            text += build_references_section(bib_path)
        text = add_footer(text)
        target = wiki_dir / f"{wiki_name}.md"
        target.write_text(text, encoding="utf-8")
        print(f"  wrote {wiki_name}.md")


def build_home_md(wiki_dir: Path) -> None:
    """Home.md: index mirror with badges and links."""
    body = """\
# AMFAM Capstone — Automated Document Classification

**Zero-shot, prompt-engineered document classification** via OpenRouter vision models, evaluated on Braintrust against balanced RVL-CDIP slices.

| Metric | Value |
|--------|-------|
| Best slice accuracy | **99.4%** (v11.8, 160-image) |
| Largest held-out | **82.6%** (1,120-image) |
| Pipeline failure | **0.114%** (with fallback) |
| Per-image cost | **≈ $0.0004** |

**Quick links:**
- [Posit Cloud site](https://connect.posit.cloud/jackjburleson/content/019fd440-9bbf-1a22-cf30-a36183d9c7d4)
- [GitHub repo](https://github.com/Exios66/AMFAM_capstone)
- [Manuscript](Manuscript)
- [Headline results](Headline-results)
- [Monte Carlo overview](MC-overview)

*Last updated: 2026-08-05*
"""
    (wiki_dir / "Home.md").write_text(body, encoding="utf-8")
    print("  wrote Home.md")


def build_sidebar_md(wiki_dir: Path) -> None:
    """_Sidebar.md: navigation mirror."""
    lines = []
    for label, target in SIDEBAR:
        if label == "---":
            lines.append("")
        elif target is None:
            lines.append(f"**{label}**")
        else:
            lines.append(f"- [{label}]({target})")
    body = "\n".join(lines) + "\n"
    (wiki_dir / "_Sidebar.md").write_text(body, encoding="utf-8")
    print("  wrote _Sidebar.md")


def copy_assets(wiki_dir: Path) -> None:
    """Copy charts, figures, and chat_images into wiki assets/."""
    import shutil
    for subdir in ("charts", "figures", "chat_images"):
        src_dir = WEBSITE / subdir
        dst_dir = wiki_dir / "assets" / subdir
        if not src_dir.exists():
            continue
        dst_dir.mkdir(parents=True, exist_ok=True)
        for f in src_dir.iterdir():
            if f.is_file():
                shutil.copy2(f, dst_dir / f.name)
        count = len(list(dst_dir.iterdir()))
        print(f"  copied {count} {subdir}/ → assets/{subdir}/")


# ---------------------------------------------------------------------------
# Git operations
# ---------------------------------------------------------------------------

def clone_or_pull_wiki(wiki_dir: Path) -> None:
    if wiki_dir.exists():
        subprocess.run(["git", "pull"], cwd=wiki_dir, check=True, capture_output=True)
        print("  wiki repo pulled")
    else:
        subprocess.run(
            ["git", "clone", WIKI_REMOTE, str(wiki_dir)],
            check=True, capture_output=True,
        )
        print("  wiki repo cloned")


def commit_and_push(wiki_dir: Path) -> None:
    subprocess.run(["git", "add", "-A"], cwd=wiki_dir, check=True, capture_output=True)
    result = subprocess.run(
        ["git", "status", "--porcelain"],
        cwd=wiki_dir, capture_output=True, text=True,
    )
    if not result.stdout.strip():
        print("  no wiki changes to commit")
        return
    subprocess.run(
        ["git", "commit", "-m", "Wiki rebuild: full site mirror with APA formatting + charts"],
        cwd=wiki_dir, check=True, capture_output=True,
    )
    subprocess.run(["git", "push"], cwd=wiki_dir, check=True, capture_output=True)
    print("  wiki committed + pushed")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--no-push", action="store_true", help="Build but don't push")
    args = parser.parse_args()

    wiki_dir = WIKI_BUILD
    wiki_dir.mkdir(parents=True, exist_ok=True)

    print("Cloning/pulling wiki repo…")
    clone_or_pull_wiki(wiki_dir)

    print("Building wiki pages…")
    build_wiki_pages(wiki_dir)

    print("Building Home.md…")
    build_home_md(wiki_dir)

    print("Building _Sidebar.md…")
    build_sidebar_md(wiki_dir)

    print("Copying assets…")
    copy_assets(wiki_dir)

    if not args.no_push:
        print("Committing + pushing…")
        commit_and_push(wiki_dir)
    else:
        print("--no-push: skipping commit/push")

    print("Done.")


if __name__ == "__main__":
    main()
