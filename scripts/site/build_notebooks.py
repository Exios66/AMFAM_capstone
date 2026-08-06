"""Generate the four capstone walkthrough notebooks as nbformat v4 JSON.

The notebooks are assembled here as Python cell strings so they stay
reviewable and regenerable. Each notebook is written to ``notebooks/`` at the
repo root and mirrored into ``website/notebooks/`` so the Quarto site can
render it as a static appendix page (the site config disables execution, so
rendering never spends model credits).

The notebooks are designed as a **safe read-only demo**: they read real images
and experiment data from the committed Braintrust slice and shipped JSON files,
but they never mutate Braintrust, never append to the experiment log, and the
only OpenRouter spend is a single-image classification in notebook 01.
Mutating steps (dataset upload, full eval runs, the reporting chain) are shown
as print-only previews.

Usage:
    python scripts/site/build_notebooks.py
"""

from __future__ import annotations

import json
import uuid
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
NOTEBOOKS_DIR = ROOT / "notebooks"
SITE_NOTEBOOKS_DIR = ROOT / "website" / "notebooks"

BOOTSTRAP = """\
import sys
from pathlib import Path

ROOT = next(
    p for p in (Path.cwd(), *Path.cwd().parents)
    if (p / "src" / "constants.py").exists()
)
sys.path.insert(0, str(ROOT))
print("Repo root:", ROOT)
"""

CONFIG = """\
from src.braintrust_config import load_braintrust_config
from src.env_utils import require_env

config = load_braintrust_config()      # braintrust.env first, then .env
api_key = require_env("OPENROUTER_API_KEY")[0]

print("project:", config.project_name)
print("project_id:", config.project_id)
print("dataset:", config.dataset_project, "/", config.dataset)
print("model:", config.model)
print("braintrust api_key set:", bool(config.api_key))
print("openrouter api_key set:", bool(api_key))
"""


def code(src: str) -> dict:
    return {
        "cell_type": "code",
        "execution_count": None,
        "id": uuid.uuid4().hex,
        "metadata": {},
        "outputs": [],
        "source": src,
    }


def md(src: str) -> dict:
    return {"cell_type": "markdown", "id": uuid.uuid4().hex, "metadata": {}, "source": src}


def raw(src: str) -> dict:
    return {"cell_type": "raw", "id": uuid.uuid4().hex, "metadata": {}, "source": src}


def notebook(title: str, cells: list[dict]) -> dict:
    frontmatter = raw(f"---\ntitle: {title!r}\n---\n")
    return {
        "cells": [frontmatter, *cells],
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3",
            },
            "language_info": {"name": "python", "version": "3.9"},
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }


def notebook_01() -> dict:
    return notebook(
        "01 · Environment setup & single-image classification",
        [
            md(
                "# 01 · Environment setup & single-image classification\n"
                "\n"
                "This notebook walks the full **first step** of the capstone pipeline:\n"
                "\n"
                "1. Configure OpenRouter + Braintrust credentials.\n"
                "2. Load a document image (from your local RVL-CDIP tree, or fetched from the\n"
                "   committed Braintrust slice).\n"
                "3. Normalize it exactly like the dataset slices (grayscale, 1024x1024, white padding).\n"
                "4. Ask an OpenRouter vision model to classify it, then parse the prediction.\n"
                "\n"
                "Everything reuses the repo's `src/` library rather than reimplementing logic.\n"
                "See `scripts/braintrust/braintrust_openrouter_input.py` for the full eval runner.\n"
            ),
            md(
                "## Prerequisites\n"
                "\n"
                "```bash\n"
                "pip install -r requirements-dev.txt\n"
                "```\n"
                "\n"
                "Two env files (both gitignored) must exist:\n"
                "\n"
                "- `.env` — `OPENROUTER_API_KEY` (and optionally `RESEARCH_FUNDING_API_KEY`).\n"
                "- `braintrust.env` — single source of truth for the Braintrust org/project/dataset/model.\n"
                "\n"
                "Create them from the templates:\n"
                "\n"
                "```bash\n"
                "cp .env.example .env\n"
                "cp braintrust.env.example braintrust.env\n"
                "```\n"
                "\n"
                "`src/braintrust_config.py` loads `braintrust.env` **first** and only falls back to\n"
                "`.env`, so the Braintrust key always resolves to the current account. Always read\n"
                "keys/ids through `config` from `load_braintrust_config()` — never straight from\n"
                "`os.environ` — or a stale `.env` value can silently win.\n"
            ),
            md("## 0. Bootstrap: repo path + credentials"),
            code(BOOTSTRAP),
            code(CONFIG),
            md(
                "## 1. Load a document image\n"
                "\n"
                "Images follow the filename convention `rvl_cdip__{class}__{NNNN}.png`, which embeds the\n"
                "ground-truth class so `extract_class_from_filename()` can recover the label. If you have a\n"
                "local RVL-CDIP tree (`processed_balanced_dataset/images`, `fixed_size_sampled`, a Kaggle\n"
                "download, ...) this notebook uses it. Otherwise it fetches **one real image** from the\n"
                "committed Braintrust slice `fixed_size_sampled`, so the demo always works out of the box."
            ),
            code(
                """\
from src.image_utils import find_images

# EDIT ME: point at your local RVL-CDIP tree if you have one.
image_dir = ROOT / "processed_balanced_dataset" / "images"
paths = find_images(image_dir, recursive=True) if image_dir.exists() else []
print(f"{len(paths)} images found under {image_dir}")

if not paths:
    print("No local tree found - fetching one real image from the committed "
          f"Braintrust slice '{config.dataset}' instead.")
    import tempfile

    import braintrust

    from src.braintrust_utils import fetch_attachment_bytes

    braintrust.login(api_key=config.api_key)
    ds = braintrust.init_dataset(project=config.project_name, name=config.dataset)
    row = next(
        r for r in ds
        if not ((r.get("input") or {}).get("metadata") or {}).get("placeholder", False)
        and (r.get("input") or {}).get("image") is not None
    )
    att = (row["input"] or {})["image"]
    raw = fetch_attachment_bytes(config.api_key, att.reference, config.org_id, config.api_base)
    expected = row.get("expected") or "unknown"
    _tmp = Path(tempfile.mkdtemp(prefix="rvl_cdip_nb01_"))
    image_path = _tmp / f"rvl_cdip__{expected}__0001.png"
    image_path.write_bytes(raw)
    print("Fetched:", att.reference.get("filename", image_path.name),
          f"({len(raw):,} bytes)")

image_path = paths[0] if paths else image_path
print("Using:", image_path)
"""
            ),
            code(
                """\
from IPython.display import Image as IPImage, display


def extract_class_from_filename(filename: str) -> str:
    # Recover the ground-truth class from 'rvl_cdip__{class}__{NNNN}.png'.
    parts = filename.split("__")
    return parts[1] if len(parts) >= 3 else "?"


display(IPImage(filename=str(image_path), width=360))
print("Filename:", image_path.name)
expected = extract_class_from_filename(image_path.name)
print("Ground-truth class:", expected)
"""
            ),
            md(
                "## 2. Normalize to the standard representation\n"
                "\n"
                "Every dataset slice stores **grayscale 1024x1024 PNGs with white padding** that\n"
                "preserves the aspect ratio (`src/image_utils.resize_with_padding`). Normalizing a\n"
                "single image the same way means a standalone classification matches what the eval\n"
                "runner would see."
            ),
            code(
                """\
from PIL import Image

from src.image_utils import resize_with_padding

img = Image.open(image_path).convert("L")
normalized = resize_with_padding(img, (1024, 1024), fill=255)
print("Normalized size:", normalized.size, "| mode:", normalized.mode)
display(normalized)
"""
            ),
            md(
                "## 3. Build the request payload\n"
                "\n"
                "`src/openrouter_utils.build_vision_messages` packs the prompt text + base64 image into\n"
                "an OpenAI-style `messages` payload. Use the repo's current default prompt\n"
                "(`get_prompt(DEFAULT_PROMPT_VERSION)` = v17.2) rather than a hardcoded string."
            ),
            code(
                """\
from src.image_utils import encode_image_base64
from src.openrouter_utils import build_vision_messages
from src.prompts import DEFAULT_PROMPT_VERSION, get_prompt

prompt = get_prompt(DEFAULT_PROMPT_VERSION)
image_b64 = encode_image_base64(image_path)
messages = build_vision_messages(prompt, image_b64, image_format="png")

print("Prompt version:", DEFAULT_PROMPT_VERSION, "| chars:", len(prompt))
print("Message role:", messages[0]["role"], "| content parts:", len(messages[0]["content"]))
"""
            ),
            md(
                "## 4. Classify (spends OpenRouter credits)\n"
                "\n"
                "The one-liner `classify_image()` uses the module's pinned prompt (v14). To classify\n"
                "with the **current default prompt** (v17.2), send the payload built above directly and\n"
                "parse the answer with `clean_prediction()` / `extract_runner_up()`.\n"
                "\n"
                "> This is the **only** cell in the notebook suite that spends model credits — roughly\n"
                "> $0.0004 per image at qwen3.7-flash rates. Everything else in the four notebooks is\n"
                "> read-only or print-only."
            ),
            code(
                """\
from src.openrouter_classifier import classify_image

result = classify_image(api_key, image_path, model=config.model)
print("model:", result["model"])
print("classification:", result["classification"])
print("status:", result["status"])
print("usage:", result.get("usage"))
print("exact_match:", result["classification"] == expected)
"""
            ),
            code(
                """\
import requests

from src.openrouter_classifier import clean_prediction, extract_runner_up
from src.openrouter_utils import OPENROUTER_API_URL

payload = {
    "model": config.model,
    "messages": build_vision_messages(prompt, image_b64),
    "max_tokens": 4096,
    "temperature": 0.1,
}
resp = requests.post(
    OPENROUTER_API_URL,
    headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
    json=payload,
    timeout=120,
)
resp.raise_for_status()
data = resp.json()
raw = data["choices"][0]["message"].get("content") or ""
print("raw tail:", raw[-300:])
print("clean_prediction:", clean_prediction(raw))
print("runner_up:", extract_runner_up(raw))
print("usage:", data.get("usage"))
"""
            ),
            md(
                "## Next\n"
                "\n"
                "Notebook **02 · Balanced sampling & Braintrust upload** turns this single-image flow\n"
                "into a deterministic, class-balanced dataset slice ready to be uploaded to Braintrust\n"
                "and queued as a full eval run."
            ),
        ],
    )


def notebook_02() -> dict:
    return notebook(
        "02 · Balanced sampling, Braintrust upload & queuing a run",
        [
            md(
                "# 02 · Balanced sampling, Braintrust upload & queuing a run\n"
                "\n"
                "This notebook builds a **deterministic, class-balanced dataset slice** exactly the way\n"
                "the slice builders do (`scripts/braintrust/create_braintrust_800_dataset.py`):\n"
                "\n"
                "1. Sample `N` images per class from the committed Braintrust slice.\n"
                "2. De-duplicate in **rendered-pixel space** (hash the normalized PNG, never raw bytes).\n"
                "3. Normalize each image to a grayscale 1024x1024 PNG and show the exact upload payload.\n"
                "4. Show the eval-run command the slice builders queue (preview only — no credits spent).\n"
                "\n"
                "To keep this site build clean, the upload and eval steps are **print-only previews**;\n"
                "set `RUN_UPLOAD = True` (or run the printed commands) to actually create the slice and\n"
                "queue a run."
            ),
            md("## 0. Bootstrap: repo path + credentials"),
            code(BOOTSTRAP),
            code(CONFIG),
            md(
                "## 1. Sampling parameters\n"
                "\n"
                "`N_PER_CLASS` and `SEED` are your spec: the same seed + source always reproduces the\n"
                "same slice. The slice has `16 * N_PER_CLASS` rows (each of the 16 classes in\n"
                "`src.constants.DOCUMENT_CLASSES`)."
            ),
            code(
                """\
from src.constants import DOCUMENT_CLASSES

N_PER_CLASS = 2   # EDIT: images per class -> 16 * N_PER_CLASS total rows
SEED = 42         # EDIT: deterministic sampling seed
print(f"{N_PER_CLASS} per class x {len(DOCUMENT_CLASSES)} classes = {N_PER_CLASS * len(DOCUMENT_CLASSES)} rows")
"""
            ),
            md(
                "## 2. Balanced sample from the committed Braintrust slice\n"
                "\n"
                "The committed slice is already deterministic and pixel-deduped, so drawing the first\n"
                "`N_PER_CLASS` rows per class reproduces a stable sample with no local RVL-CDIP tree\n"
                "required. Each row's PNG attachment is downloaded directly (`fetch_attachment_bytes`),\n"
                "mirroring how the production slice builders pull images."
            ),
            code(
                """\
from io import BytesIO

import braintrust

from src.braintrust_utils import fetch_attachment_bytes


def sample_balanced_from_braintrust(n_per_class: int):
    braintrust.login(api_key=config.api_key)
    ds = braintrust.init_dataset(project=config.project_name, name=config.dataset)
    counts = {cls: 0 for cls in DOCUMENT_CLASSES}
    selected: list[tuple[str, bytes, str]] = []
    for row in ds:
        if all(counts[cls] >= n_per_class for cls in DOCUMENT_CLASSES):
            break
        meta = (row.get("input") or {}).get("metadata") or {}
        att = (row.get("input") or {}).get("image")
        if meta.get("placeholder") or att is None:
            continue
        cls = row.get("expected")
        if cls not in counts or counts[cls] >= n_per_class:
            continue
        counts[cls] += 1
        raw = fetch_attachment_bytes(config.api_key, att.reference, config.org_id, config.api_base)
        fn = att.reference.get("filename") or f"rvl_cdip__{cls}__{counts[cls]:04d}.png"
        selected.append((cls, raw, fn))
    return selected


selected = sample_balanced_from_braintrust(N_PER_CLASS)
print(f"{len(selected)} images sampled ({N_PER_CLASS}/class x {len(DOCUMENT_CLASSES)} classes)")
for cls, raw, fn in selected[:6]:
    print(" ", cls, fn, f"({len(raw):,} bytes)")
"""
            ),
            md(
                "## 3. Normalize + pixel-hash de-duplication\n"
                "\n"
                "De-duplication is enforced on the **normalized rendered PNG**, so identical images from\n"
                "different files cannot slip past. Each image is rendered to a grayscale 1024x1024 PNG\n"
                "first, hashed, and skipped if the hash was already accepted."
            ),
            code(
                """\
import hashlib
from io import BytesIO

from PIL import Image

from src.image_utils import resize_with_padding


def to_png_bytes(img: Image.Image, target_size=(1024, 1024)) -> bytes:
    img = img.convert("L")
    img = resize_with_padding(img, target_size, fill=255)
    buf = BytesIO()
    img.save(buf, format="PNG")
    return buf.getvalue()


def pixel_hash(png_bytes: bytes) -> str:
    return hashlib.sha256(png_bytes).hexdigest()


cls, raw, fn = selected[0]
png = to_png_bytes(Image.open(BytesIO(raw)))
print(cls, fn, "->", len(png), "bytes, hash", pixel_hash(png)[:16])
"""
            ),
            md(
                "## 4. Prepare the upload payload (preview only)\n"
                "\n"
                "The upload matches the documented pattern used by every slice builder:\n"
                "`braintrust.login` -> `init_dataset` -> `insert` with an `Attachment` payload -> "
                "`flush`/`close`. An existing dataset with the same name is deleted first so re-runs\n"
                "are safe. This demo **builds the exact row payloads** (real normalized PNGs + pixel\n"
                "hashes) but keeps `RUN_UPLOAD = False` so re-running the notebook never creates junk\n"
                "datasets in Braintrust."
            ),
            code(
                """\
from io import BytesIO

from PIL import Image

# Build the exact row payloads the slice builders upload (no network calls).
used: set[str] = set()
rows: list[tuple[str, bytes, str]] = []
for cls, raw, _src_fn in selected:
    png = to_png_bytes(Image.open(BytesIO(raw)))
    h = pixel_hash(png)
    if h in used:
        continue
    used.add(h)
    rows.append((cls, png, f"rvl_cdip__{cls}__{len(rows) + 1:04d}.png"))

print(f"{len(rows)} unique normalized images ready (after pixel-hash dedup)")

# --- Preview of the upload. Set RUN_UPLOAD = True to actually create the   ---
# --- dataset in Braintrust (idempotent: a same-named dataset is deleted    ---
# --- first, so re-runs are safe).                                          ---
RUN_UPLOAD = False
if RUN_UPLOAD:
    import braintrust
    from braintrust import Attachment

    from src.braintrust_utils import delete_dataset_by_name

    dataset_name = f"notebook_balanced_{N_PER_CLASS}"
    braintrust.login(api_key=config.api_key)
    delete_dataset_by_name(config.api_key, config.project_id, dataset_name, config.api_base)
    dataset = braintrust.init_dataset(project_id=config.project_id, name=dataset_name)
    for cls, png, fn in rows:
        dataset.insert(
            input={
                "image": Attachment(data=png, filename=fn, content_type="image/png"),
                "metadata": {"class": cls, "placeholder": False},
            },
            expected=cls,
            metadata={"source": "notebook-balanced-sample", "seed": SEED, "n_per_class": N_PER_CLASS},
        )
    dataset.flush()
    dataset.close()
    print(f"Uploaded {len(rows)} unique images -> dataset '{dataset_name}'")
else:
    print("Upload skipped (RUN_UPLOAD = False). Set RUN_UPLOAD = True to upload "
          f"{N_PER_CLASS * len(DOCUMENT_CLASSES)} rows to Braintrust.")
"""
            ),
            md(
                "## 5. Queue an eval run against the slice (preview only)\n"
                "\n"
                "Preflight validates prompt + dataset (**spends no credits**), then the eval runner\n"
                "(`braintrust_openrouter_input.py`) executes the slice and streams results into both\n"
                "Braintrust and a local JSONL manifest. That second step spends OpenRouter credits\n"
                "(~$0.0004/image), so this demo only prints the commands."
            ),
            code(
                """\
# Preview of the slice-builder workflow. Executing the eval spends OpenRouter
# credits, so this demo only prints the exact commands to run.
dataset_name = f"notebook_balanced_{N_PER_CLASS}"
experiment_name = f"notebook_{config.model.replace('/', '_')}_v17.2_{dataset_name}"

print("$ python scripts/braintrust/preflight_eval.py \\\\")
print(f"      --dataset {dataset_name} --prompt-version v17.2")
print()
print("$ python scripts/braintrust/braintrust_openrouter_input.py \\\\")
print(f"      --dataset {dataset_name} --prompt-version v17.2 \\\\")
print(f"      --model {config.model} --experiment-name {experiment_name} \\\\")
print(f"      --manifest reports/manifests/{experiment_name}.jsonl")
"""
            ),
            md(
                "## Next\n"
                "\n"
                "Notebook **03 · Watchers, evaluators & full experiment launch** covers preflight,\n"
                "monitoring a run from the manifest, crash-proof resume, and the post-run scoring/\n"
                "reporting chain."
            ),
        ],
    )


def notebook_03() -> dict:
    return notebook(
        "03 · Watchers, evaluators & launching a full experiment",
        [
            md(
                "# 03 · Watchers, evaluators & launching a full experiment\n"
                "\n"
                "Once `.env` / `braintrust.env` are configured, this notebook shows the complete\n"
                "experiment lifecycle used by the production scripts:\n"
                "\n"
                "1. **Preflight** — validate prompt + dataset with zero model credits.\n"
                "2. **Evaluators** — the three Braintrust scorers registered by the runner.\n"
                "3. **Launch** — start a full experiment run (shown as a print-only preview).\n"
                "4. **Watchers** — monitor progress from a completed run's JSONL manifest.\n"
                "5. **Report** — the post-run scoring/reporting commands (print-only).\n"
            ),
            md("## 0. Bootstrap: repo path + credentials"),
            code(BOOTSTRAP),
            code(CONFIG),
            md(
                "## 1. Preflight (zero credits)\n"
                "\n"
                "`preflight_eval.py` checks that the prompt version resolves and the dataset is\n"
                "reachable under the current credentials **without sending any model request**.\n"
                "Run it before any eval to catch setup problems early."
            ),
            code(
                """\
import subprocess
import sys


def run_script(rel_script: str, *args: str) -> None:
    cmd = [sys.executable, str(ROOT / "scripts" / rel_script), *args]
    print("$", " ".join(cmd))
    subprocess.run(cmd, cwd=ROOT, check=True)


run_script("braintrust/preflight_eval.py", "--dataset", config.dataset, "--prompt-version", "v17.2")
"""
            ),
            md(
                "## 2. Evaluators registered by the runner\n"
                "\n"
                "The eval runner wraps the OpenAI client with `braintrust.wrap_openai()` and runs\n"
                "`braintrust.Eval(..., scores=[...])`. Exactly three scorers are registered:\n"
                "\n"
                "- **`exact_match`** — `output.strip().lower() == expected_class`, scored 1.0/0.0.\n"
                "- **`failure`** — rows whose output starts with `ERROR: ` (count as misses too).\n"
                "- **`cost`** — each row's actual billed USD from OpenRouter's `usage.cost`.\n"
                "\n"
                "Near-miss (runner-up == expected while predicted != expected) is **not** a Braintrust\n"
                "scorer — it is computed locally from the runner-up line the manifest records, by\n"
                "`score_manifest.py`.\n"
                "\n"
                "Abridged registration from `braintrust_openrouter_input.py`:\n"
                "\n"
                "```python\n"
                "from braintrust import Eval, wrap_openai\n"
                "from openai import OpenAI\n"
                "\n"
                "client = wrap_openai(OpenAI(base_url=OPENROUTER_BASE_URL, api_key=key))\n"
                "\n"
                "Eval(\n"
                "    dataset=dataset_rows,\n"
                "    task=classify_row,          # returns (output, metadata) per row\n"
                "    scores=[exact_match, failure, cost],\n"
                "    metadata={\"model\": model, \"prompt_version\": prompt_version},\n"
                "    max_concurrency=8,\n"
                ")\n"
                "```\n"
            ),
            md(
                "## 3. Launch a full experiment (preview only)\n"
                "\n"
                "Launching the runner against the configured dataset writes every completed row to a\n"
                "**local JSONL manifest** (the durable checkpoint) as well as Braintrust, so the run\n"
                "survives crashes, Braintrust limits, and quota errors. A full 160-image run spends\n"
                "OpenRouter credits (~$0.0004/image), so this demo only prints the launch command."
            ),
            code(
                """\
experiment_name = f"notebook_full_{config.model.replace('/', '_')}_v17.2"
manifest = ROOT / "reports" / "manifests" / f"{experiment_name}.jsonl"

cmd = [
    sys.executable,
    str(ROOT / "scripts" / "braintrust" / "braintrust_openrouter_input.py"),
    "--dataset", config.dataset,
    "--prompt-version", "v17.2",
    "--model", config.model,
    "--experiment-name", experiment_name,
    "--manifest", str(manifest),
]
print("$", " ".join(cmd))
print("\\n(Not launched: a full 160-image run would spend OpenRouter credits.)")
"""
            ),
            md(
                "## 4. Watch a run from the manifest\n"
                "\n"
                "Each manifest record carries a `status` (`completed` / `error` / `empty`) plus\n"
                "`runner_up` and `cost`; the eval runner retries transient provider failures up to\n"
                "`MAX_TRIES=3`, growing `max_tokens` toward `MAX_TOKENS_CAP=32768` on length caps.\n"
                "Here we count statuses from a **completed** run's manifest shipped with the repo\n"
                "(`reports/manifests/eval_v17_v1.jsonl`) — read-only."
            ),
            code(
                """\
import json

from pathlib import Path


def manifest_status_counts(path: Path) -> dict:
    counts: dict[str, int] = {}
    if not path.exists():
        return {"(manifest not created yet)": 0}
    for line in path.read_text().splitlines()[1:]:
        if not line.strip():
            continue
        rec = json.loads(line)
        status = rec.get("status", "empty")
        counts[status] = counts.get(status, 0) + 1
    return counts


# A completed run's manifest, shipped with the repo (read-only demo).
manifest = ROOT / "reports" / "manifests" / "eval_v17_v1.jsonl"
print("Watching:", manifest.name)
manifest_status_counts(manifest)
"""
            ),
            md(
                "## 5. Crash-proof resume\n"
                "\n"
                "If a run dies (crash, Braintrust cap, quota 403), re-invoke the runner through\n"
                "`resume_until_complete.py` until `--expected-rows` unique filenames have a final\n"
                "status. Completed rows are skipped; failed/error rows are re-attempted. On completion\n"
                "it auto-scores the manifest locally with `score_manifest.py` (no Braintrust scorer\n"
                "credits). For production, `run_eval_queue.py` chains multiple jobs sequentially with\n"
                "preflight checks and manifest verification between jobs."
            ),
            code(
                """\
# Illustrative: re-invokes the runner until every row is finished.
# Expected rows must equal the dataset slice size (fixed_size_sampled = 160).
cmd = [
    sys.executable,
    str(ROOT / "scripts" / "braintrust" / "resume_until_complete.py"),
    "--dataset", config.dataset,
    "--prompt-version", "v17.2",
    "--model", config.model,
    "--max-tokens", "8192",
    "--experiment-name", "qwen3.7-flash_v17_v1",
    "--manifest", str(manifest),
    "--expected-rows", "160",
]
print("$", " ".join(cmd))
# subprocess.run(cmd, cwd=ROOT, check=True)   # uncomment to run
"""
            ),
            md(
                "## 6. Post-run scoring & reporting (preview only)\n"
                "\n"
                "The full reporting chain (also wired in `scripts/braintrust/`) against the completed\n"
                "`qwen3.7-flash_v17_v1` manifest above:\n"
                "\n"
                "1. `score_manifest.py` — local scoring from the manifest, no Braintrust credits.\n"
                "2. `summarize_braintrust_experiment.py` — per-image OK/MISS summary + exact_match.\n"
                "3. `braintrust_report.py` — accuracy, confusion matrix (PNG+MD), misclassification\n"
                "   reasoning, cost breakdown (adjust `--input-price`/`--output-price` to the current\n"
                "   OpenRouter model rates).\n"
                "4. `braintrust_metrics_visual.py` — per-class chart + heatmap, and appends the\n"
                "   experiment to `docs/experiments/experiment_log.md`.\n"
                "\n"
                "These scripts write files into `reports/` and append to `docs/experiments/experiment_log.md`,\n"
                "so this demo prints the commands instead of running them."
            ),
            code(
                """\
print("$ python scripts/braintrust/score_manifest.py --manifest", manifest)
print("$ python scripts/braintrust/summarize_braintrust_experiment.py --experiment qwen3.7-flash_v17_v1")
print("$ python scripts/braintrust/braintrust_report.py \\\\")
print(f"      --experiment qwen3.7-flash_v17_v1 --model {config.model} --prompt-version v17.2 \\\\")
print(f"      --dataset {config.dataset} --images-per-class 10 \\\\")
print("      --input-price 0.03 --output-price 0.13")
print("$ python scripts/braintrust/braintrust_metrics_visual.py qwen3.7-flash_v17_v1")
"""
            ),
            md(
                "## Recap\n"
                "\n"
                "1. Preflight validates prompt + dataset with zero credits.\n"
                "2. The runner registers `exact_match`, `failure`, and `cost` scorers.\n"
                "3. A full run writes every row to the local manifest as well as Braintrust.\n"
                "4. Watch progress from the manifest; resume with `resume_until_complete.py`.\n"
                "5. Score locally, then generate the summary / report / charts / experiment log.\n"
                "\n"
                "Inspect individual row traces in the Braintrust UI (each span carries `raw_response`,\n"
                "`reasoning`, `model`, `prompt_version`, `filename`, and error rows add `error`/`attempts`)."
            ),
        ],
    )


def notebook_04() -> dict:
    return notebook(
        "04 · Interactive data layer: cost calculator & experiment explorer",
        [
            md(
                "# 04 · Interactive data layer: cost calculator & experiment explorer\n"
                "\n"
                "The site's two interactive pages — the **Cost Calculator** and the **Experiment\n"
                "Explorer** — are pure client-side browsers over committed JSON files in\n"
                "`website/data/`. This notebook is a **read-only** tour of that data layer: no API\n"
                "calls, no model credits, nothing is written back. Every number shown here is exactly\n"
                "what the interactive pages display in the browser.\n"
                "\n"
                "Data files (`scripts/site/build_site.py` regenerates them from the committed markdown\n"
                "reports):\n"
                "\n"
                "- `experiments.json` — every recorded eval run.\n"
                "- `per-class-accuracy.json` — per-class correctness per report.\n"
                "- `cost-models.json` — measured per-model pricing + scale-up projections.\n"
                "- `confusion-matrices.json` — confusion heatmap matrices per run.\n"
            ),
            md("## 0. Bootstrap: repo path"),
            code(BOOTSTRAP),
            md("## 1. Load the committed data layer"),
            code(
                """\
import json

data_dir = ROOT / "website" / "data"
experiments = json.loads((data_dir / "experiments.json").read_text())
per_class = json.loads((data_dir / "per-class-accuracy.json").read_text())
cost_models = json.loads((data_dir / "cost-models.json").read_text())
confusions = json.loads((data_dir / "confusion-matrices.json").read_text())

print("experiments.json      :", len(experiments["experiments"]), "runs")
print("per-class-accuracy.json:", len(per_class), "reports")
print("cost-models.json      :", len(cost_models["models"]), "models")
print("confusion-matrices.json:", len(confusions), "runs")
"""
            ),
            md("## 2. Summary statistics (what the explorer's summary strip shows)"),
            code(
                """\
runs = experiments["experiments"]
models = {r["model_short"] for r in runs}
total_images = sum(r.get("images") or 0 for r in runs)
best = max(runs, key=lambda r: r.get("accuracy") or 0)

print(f"{len(runs)} runs | {len(models)} models | {total_images:,} images classified")
print(f"Best run: {best['model_short']} · {best['prompt_version']} · "
      f"{best['accuracy'] * 100:.1f}% ({best.get('correct')}/{best.get('total')}) "
      f"on {best.get('dataset', '')[:40]}")
"""
            ),
            md("## 3. Top runs by exact-match accuracy"),
            code(
                """\
top = sorted(runs, key=lambda r: r.get("accuracy") or 0, reverse=True)[:8]
print(f"{'model':<28} {'prompt':<8} {'imgs':>5} {'acc%':>6}  {'correct':>7}")
print("-" * 64)
for r in top:
    print(f"{r['model_short']:<28} {r['prompt_version']:<8} {r.get('images', 0):>5} "
          f"{(r.get('accuracy') or 0) * 100:>6.1f}  {r.get('correct', 0):>7}")
"""
            ),
            md(
                "## 4. Per-class accuracy for the 1,120-image run\n"
                "\n"
                "The explorer's **per-class picker** is fed by `per-class-accuracy.json`, keyed by\n"
                "report. This reproduces the chart for the largest held-out run"
            ),
            code(
                """\
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

report_key = "qwen3.7-flash_v11.8_1600_balanced_1120_final"
classes = per_class[report_key]
items = sorted(classes.items(), key=lambda kv: kv[1]["accuracy"])

fig, ax = plt.subplots(figsize=(10, 6))
names = [c for c, _ in items]
vals = [v["accuracy"] * 100 for _, v in items]
colors = ["#2a9d8f" if v >= 90 else "#e9c46a" if v >= 70 else "#e76f51" for v in vals]
ax.barh(names, vals, color=colors)
ax.axvline(82.6, color="#264653", linestyle="--", lw=1)
ax.text(82.6, -0.8, " overall 82.6%", color="#264653", fontsize=9)
ax.set_xlim(0, 100)
ax.set_xlabel("Exact-match accuracy (%)")
ax.set_title("Per-class accuracy — qwen3.7-flash v11.8 on the 1,120-image slice")
ax.grid(axis="x", alpha=0.25)
plt.tight_layout()
plt.show()
"""
            ),
            md(
                "## 5. Cost projections (what the cost calculator's sliders drive)\n"
                "\n"
                "`cost-models.json` records each model's measured per-image billing and the linear\n"
                "scale-up to 800 / 25,000 / 320,000 images. The cheapest model wins by an order of\n"
                "magnitude."
            ),
            code(
                """\
print(f"{'model':<34} {'$/image':>9} {'800':>8} {'25,000':>9} {'320,000':>10}")
print("-" * 74)
for m in sorted(cost_models["models"], key=lambda m: m["actual_cost_per_image"]):
    p = m.get("projections", {}) or {}
    proj = {label: p.get(str(n)) or (m["actual_cost_per_image"] * n)
            for label, n in (("800", 800), ("25,000", 25000), ("320,000", 320000))}
    print(f"{m['model']:<34} {m['actual_cost_per_image']:>9.4f} "
          f"{proj['800']:>8.2f} {proj['25,000']:>9.2f} {proj['320,000']:>10.2f}")
"""
            ),
            md(
                "## Recap\n"
                "\n"
                "1. The interactive pages are thin browsers over committed JSON — no API access.\n"
                "2. `experiments.json` powers the runs table, filters, and accuracy-by-model/prompt/size views.\n"
                "3. `per-class-accuracy.json` + `confusion-matrices.json` power the per-class and confusion pickers.\n"
                "4. `cost-models.json` drives the cost calculator's projections.\n"
                "\n"
                "Reproduce any chart on the site from this data — every number traces back to a\n"
                "committed markdown report in `docs/experiments/` and `reports/`."
            ),
        ],
    )


def write_notebook(path: Path, nb: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(nb, indent=1) + "\n", encoding="utf-8")
    print(f"wrote {path} ({len(nb['cells'])} cells)")


def main() -> None:
    for name, builder in [
        ("01_env_setup_and_single_image.ipynb", notebook_01),
        ("02_balanced_sampling_and_braintrust_upload.ipynb", notebook_02),
        ("03_watchers_evaluators_full_experiment.ipynb", notebook_03),
        ("04_interactive_cost_and_experiments.ipynb", notebook_04),
    ]:
        nb = builder()
        write_notebook(NOTEBOOKS_DIR / name, nb)
        write_notebook(SITE_NOTEBOOKS_DIR / name, nb)


if __name__ == "__main__":
    main()
