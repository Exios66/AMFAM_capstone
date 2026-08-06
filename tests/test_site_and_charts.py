"""Posit-site integrity, Quarto asset, and SVG legibility tests.

All checks run offline against committed files — no network, no model credits.

- ``TestSvgLegibility`` — every committed chart/figure SVG is well-formed and
  free of text-text collisions (estimated glyph boxes, anchor-aware, rotated /
  off-canvas / duplicate text excluded as phantom geometry).
- ``TestQuartoAssets`` — ``_quarto.yml`` pages exist, front-matter ``resources``
  resolve, interactive widget assets (vis-network, theme switcher) exist, and
  the committed site JSON data layer has the expected structure.
- ``TestSiteIntegrity`` — internal markdown links resolve, cited bibliography
  keys exist, and SCSS theme tokens are balanced.
"""

import json
import re
import xml.etree.ElementTree as ET
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
WEBSITE = ROOT / "website"

SVG_PATHS = sorted(WEBSITE.glob("charts/*.svg")) + sorted(WEBSITE.glob("figures/*.svg"))
QMD_PATHS = sorted(WEBSITE.rglob("*.qmd"))

OVERLAP_THRESHOLD = 0.45
CHAR_WIDTH_FACTOR = 0.58


# ---------------------------------------------------------------------------
# SVG text-collision scanner (calibrated against the committed corpus: zero
# genuine collisions; rotated axis titles, off-canvas mirrored ticks, and
# duplicate same-position text are phantom geometry).
# ---------------------------------------------------------------------------

_FS_PATTERNS = (
    re.compile(r'font-size="([\d.]+)(?:px)?"'),
    re.compile(r"font: ?([\d.]+)px"),
)


def _svg_texts(svg: str) -> tuple[float, float, list[dict]]:
    canvas = re.search(r'viewBox="([\d.]+) ([\d.]+) ([\d.]+) ([\d.]+)"', svg)
    W, H = (float(canvas.group(3)), float(canvas.group(4))) if canvas else (640.0, 480.0)
    texts = []
    for m in re.finditer(r"<text[^>]*>(.*?)</text>", svg, re.S):
        outer = m.group(0)
        xm = re.search(r'x="(-?[\d.]+)"', outer)
        ym = re.search(r'y="(-?[\d.]+)"', outer)
        if not xm or not ym:
            continue
        fs = 10.0
        for pat in _FS_PATTERNS:
            fm = pat.search(outer)
            if fm:
                fs = float(fm.group(1))
                break
        am = re.search(r'text-anchor="(\w+)"|text-anchor:\s*(\w+)', outer)
        anchor = (am.group(1) or am.group(2)) if am else "start"
        rm = re.search(r"rotate\((-?[\d.]+)", outer)
        deg = float(rm.group(1)) if rm else 0.0
        inner = m.group(1)
        tspans = re.findall(
            r'<tspan[^>]*x="(-?[\d.]+)"[^>]*y="(-?[\d.]+)"[^>]*>(.*?)</tspan>', inner, re.S
        )
        if not tspans:
            content = re.sub(r"<[^>]+>", "", inner)
            tspans = [(xm.group(1), ym.group(1), content)]
        for tx, ty, content in tspans:
            content = (
                content.replace("&#39;", "'").replace("&amp;", "&")
                .replace("&gt;", ">").replace("&lt;", "<").strip()
            )
            if not content:
                continue
            texts.append(dict(x=float(tx), y=float(ty), fs=fs, anchor=anchor, rot=deg, text=content))
    return W, H, texts


def _text_box(t: dict) -> tuple[float, float, float, float]:
    w = len(t["text"]) * t["fs"] * CHAR_WIDTH_FACTOR
    h = t["fs"] * 1.25
    x, y = t["x"], t["y"]
    if t["anchor"] == "middle":
        x -= w / 2
    elif t["anchor"] == "end":
        x -= w
    return (x, y - h, x + w, y + 0.2 * h)


def _box_overlap(a, b):
    ax0, ay0, ax1, ay1 = a
    bx0, by0, bx1, by1 = b
    ox = min(ax1, bx1) - max(ax0, bx0)
    oy = min(ay1, by1) - max(ay0, by0)
    if ox <= 0 or oy <= 0:
        return 0.0
    return ox * oy / min((ax1 - ax0) * (ay1 - ay0), (bx1 - bx0) * (by1 - by0))


def _svg_collisions(svg: str) -> list[tuple[float, str, float, float, str, float, float]]:
    W, H, texts = _svg_texts(svg)
    texts = [
        t for t in texts
        if abs(t["rot"]) <= 0.5 and 0 <= t["x"] < W and 0 <= t["y"] < H
    ]
    seen, uniq = set(), []
    for t in texts:
        key = (round(t["x"], 1), round(t["y"], 1), t["text"])
        if key in seen:
            continue
        seen.add(key)
        uniq.append(t)
    collisions = []
    for i in range(len(uniq)):
        for j in range(i + 1, len(uniq)):
            ov = _box_overlap(_text_box(uniq[i]), _text_box(uniq[j]))
            if ov > OVERLAP_THRESHOLD:
                a, b = uniq[i], uniq[j]
                collisions.append((ov, a["text"], a["x"], a["y"], b["text"], b["x"], b["y"]))
    return collisions


class TestSvgLegibility:
    @pytest.mark.parametrize("path", SVG_PATHS, ids=lambda p: p.name)
    def test_svg_is_wellformed(self, path):
        ET.fromstring(path.read_text(encoding="utf-8"))

    @pytest.mark.parametrize("path", SVG_PATHS, ids=lambda p: p.name)
    def test_svg_has_viewbox(self, path):
        svg = path.read_text(encoding="utf-8")
        m = re.search(r'viewBox="(-?[\d.]+) (-?[\d.]+) (-?[\d.]+) (-?[\d.]+)"', svg)
        assert m, "missing viewBox"
        w, h = float(m.group(3)), float(m.group(4))
        assert w > 0 and h > 0

    @pytest.mark.parametrize("path", SVG_PATHS, ids=lambda p: p.name)
    def test_no_text_text_collisions(self, path):
        collisions = _svg_collisions(path.read_text(encoding="utf-8"))
        assert not collisions, (
            f"{len(collisions)} text-text collisions: "
            + "; ".join(
                f"'{a}'@({ax:.0f},{ay:.0f}) x '{b}'@({bx:.0f},{by:.0f}) ({ov:.2f})"
                for ov, a, ax, ay, b, bx, by in sorted(collisions, reverse=True)[:5]
            )
        )


class TestQuartoAssets:
    def test_quarto_yml_parses(self):
        cfg = yaml.safe_load((WEBSITE / "_quarto.yml").read_text(encoding="utf-8"))
        assert isinstance(cfg, dict)
        assert cfg.get("project", {}).get("type") == "website"

    def test_navbar_pages_exist(self):
        cfg = yaml.safe_load((WEBSITE / "_quarto.yml").read_text(encoding="utf-8"))
        missing = []

        def visit(items):
            for item in items or []:
                if isinstance(item, str) and item.endswith(".qmd"):
                    if not (WEBSITE / item).exists():
                        missing.append(item)
                elif isinstance(item, dict):
                    href = item.get("href", "")
                    if href.endswith(".qmd") and not (WEBSITE / href).exists():
                        missing.append(href)
                    visit(item.get("menu"))

        visit(cfg["website"]["navbar"]["left"])
        visit(cfg["website"]["navbar"]["right"])
        assert not missing, f"navbar pages missing: {missing}"

    def test_front_matter_resources_exist(self):
        missing = []
        for qmd in QMD_PATHS:
            text = qmd.read_text(encoding="utf-8")
            m = re.search(r"^---\n(.*?)\n---", text, re.S | re.M)
            if not m:
                continue
            try:
                fm = yaml.safe_load(m.group(1)) or {}
            except yaml.YAMLError:
                continue
            for res in fm.get("resources") or []:
                target = (qmd.parent / str(res)).resolve()
                if not target.exists():
                    missing.append(f"{qmd.name}: {res}")
        assert not missing, f"missing resources: {missing}"

    def test_interactive_widget_assets_exist(self):
        expected = [
            WEBSITE / "assets/js/vis-network.min.js",
            WEBSITE / "assets/js/d3.v7.min.js",
            WEBSITE / "charts/phrase_net_differential.json",
            WEBSITE / "charts/scattertext_style.json",
            WEBSITE / "assets/js/theme-switch.js",
            WEBSITE / "assets/html/theme-head.html",
            WEBSITE / "assets/css/custom.scss",
            WEBSITE / "assets/img/favicon.svg",
        ]
        missing = [str(p.relative_to(ROOT)) for p in expected if not p.exists()]
        assert not missing, f"missing interactive assets: {missing}"

    def test_phrase_net_graph_structure(self):
        graph = json.loads((WEBSITE / "charts/phrase_net_differential.json").read_text())
        assert isinstance(graph.get("nodes"), list) and graph["nodes"]
        assert isinstance(graph.get("edges"), list) and graph["edges"]
        node_keys = {"id", "fail", "ok", "share"}
        edge_keys = {"from", "to", "z", "fail", "ok", "in_cycle", "bias"}
        for node in graph["nodes"]:
            assert node_keys <= set(node), f"node missing keys: {node}"
        for edge in graph["edges"]:
            assert edge_keys <= set(edge), f"edge missing keys: {edge}"
        # The interactive widget shows BOTH sides of the coin: failure-biased
        # and success-biased differential edges (plus structural loops).
        biases = {e["bias"] for e in graph["edges"]}
        assert biases == {"fail", "ok"}, f"expected both edge biases, got {biases}"
        assert any(n["fail"] > n["ok"] for n in graph["nodes"]), "no failure-biased nodes"
        assert any(n["ok"] > n["fail"] for n in graph["nodes"]), "no success-biased nodes"

    def test_scattertext_json_structure(self):
        grid = json.loads((WEBSITE / "charts/scattertext_style.json").read_text())
        points = grid.get("points")
        assert isinstance(points, list) and points
        assert 2000 <= len(points) <= 3000, f"unexpected point count: {len(points)}"
        keys = {"word", "fail", "ok", "freq_fail", "freq_ok", "z", "leak"}
        for p in points:
            assert keys <= set(p), f"point missing keys: {p}"
            assert isinstance(p["word"], str) and p["word"]
            assert p["fail"] >= 0 and p["ok"] >= 0
            # raw per-million frequencies; the widget clamps to the 0.3–10^4
            # grid at render time (out-of-grid words pin to the edge)
            assert 0 < p["freq_fail"] < 1e6 and 0 < p["freq_ok"] < 1e6
        assert any(p["leak"] for p in points), "no prompt-leaked words marked"
        assert any(p["z"] > 0.5 for p in points) and any(p["z"] < -0.5 for p in points)

    def test_phrase_net_widget_tooltips_are_dom_elements(self):
        # vis-network 9.1.9 renders STRING tooltips via innerText, so HTML
        # markup shows literally (e.g. "<b>60</b>"); element titles are
        # appended as DOM and render formatted. Tooltips must go through
        # tooltipHtml(), never be raw HTML strings.
        html = (WEBSITE / "assets/html/phrase-net.html").read_text(encoding="utf-8")
        assert "function tooltipHtml(html)" in html
        assert "el.innerHTML = html" in html
        assert html.count("title: tooltipHtml(") == 2, "node + edge titles must be DOM elements"
        for m in re.finditer(r"title:\s*([^,()]+)", html):
            assert "tooltipHtml" in m.group(1), f"raw tooltip title: {m.group(1)}"

    def test_website_data_json_structure(self):
        expected = {
            "chat-examples.json": {"correct", "misclassified", "generated_at"},
            "cost-models.json": {"models", "meta"},
            "experiments.json": {"experiments", "meta"},
        }
        for name, keys in expected.items():
            data = json.loads((WEBSITE / "data" / name).read_text())
            assert keys <= set(data), f"{name} missing keys {keys - set(data)}"
        for name in ("confusion-matrices.json", "per-class-accuracy.json"):
            data = json.loads((WEBSITE / "data" / name).read_text())
            assert data, f"{name} is empty"

    def test_chat_examples_records_have_required_fields(self):
        data = json.loads((WEBSITE / "data" / "chat-examples.json").read_text())
        required = {"filename", "expected", "predicted", "reasoning", "image"}
        for bucket in ("correct", "misclassified"):
            records = data.get(bucket) or []
            assert records, f"no records in chat-examples.{bucket}"
            for record in records:
                assert required <= set(record), f"record missing keys: {record}"


class TestSiteIntegrity:
    @staticmethod
    def _resolve(link: str, qmd_dir: Path) -> bool:
        target = link.split("#")[0]
        if not target:
            return True
        candidate = qmd_dir / target
        if candidate.exists():
            return True
        if candidate.suffix in (".html", ".qmd"):
            return candidate.with_suffix(".html").exists() or candidate.with_suffix(".qmd").exists()
        return False

    def test_internal_links_resolve(self):
        broken = []
        for qmd in QMD_PATHS:
            text = qmd.read_text(encoding="utf-8")
            for m in re.finditer(r"\[[^\]]*\]\(([^)\s]+)(?: \"[^\"]*\")?\)", text):
                link = m.group(1)
                if link.startswith(("http://", "https://", "mailto:", "{{<", "#", "<")):
                    continue
                if not self._resolve(link, qmd.parent):
                    broken.append(f"{qmd.name}: {link}")
        assert not broken, f"broken internal links: {broken[:10]}"

    def test_images_resolve(self):
        broken = []
        for qmd in QMD_PATHS:
            text = qmd.read_text(encoding="utf-8")
            for m in re.finditer(r"!\[[^\]]*\]\(([^)\s]+)\)", text):
                img = m.group(1)
                if img.startswith(("http://", "https://", "data:")):
                    continue
                if not self._resolve(img, qmd.parent):
                    broken.append(f"{qmd.name}: {img}")
        assert not broken, f"broken images: {broken[:10]}"

    def test_bib_citations_exist(self):
        bib = (WEBSITE / "references.bib").read_text(encoding="utf-8")
        keys = set(re.findall(r"@\w+\{([\w:\-\.]+),", bib))
        missing = set()
        for qmd in QMD_PATHS:
            text = qmd.read_text(encoding="utf-8")
            for cited in re.findall(r"(?<![\w/])@([a-zA-Z][a-zA-Z0-9:_\-]*)", text):
                # Skip Quarto cross-refs, CSS media queries, and library@version syntax.
                if cited.startswith(("fig-", "tbl-", "sec-")) or cited in ("media", "acc"):
                    continue
                if cited not in keys:
                    missing.add(f"{qmd.name}: @{cited}")
        assert not missing, f"cited keys missing from references.bib: {missing}"

    def test_scss_theme_tokens_are_balanced(self):
        scss = (WEBSITE / "assets/css/custom.scss").read_text(encoding="utf-8")
        used = set(re.findall(r"var\((--[\w-]+)", scss))
        defined = set(re.findall(r"(--[\w-]+)\s*:", scss))
        missing = used - defined
        assert not missing, f"undefined theme tokens: {sorted(missing)}"


class TestNotebookPages:
    """The four site notebooks must stay valid nbformat v4 and keep their cell
    sources in the spec-standard LIST form.

    Quarto's notebook reader mis-parses single-string sources: it strips the
    in-cell newlines, flattening every markdown/code cell into one run-on block
    (headings swallow paragraphs, lists lose their numbering, code loses its
    line breaks) — the "notebook display mess" regression. The generator
    (``scripts/site/build_notebooks.py``) always emits list-form sources, and
    each notebook's opening raw cell carries Quarto title/subtitle frontmatter.
    """

    NOTEBOOK_NAMES = [
        "01_env_setup_and_single_image",
        "02_balanced_sampling_and_braintrust_upload",
        "03_watchers_evaluators_full_experiment",
        "04_interactive_cost_and_experiments",
    ]

    @pytest.fixture(scope="class", params=NOTEBOOK_NAMES)
    def notebook(self, request):
        path = WEBSITE / "notebooks" / f"{request.param}.ipynb"
        assert path.exists(), f"missing notebook: {path}"
        # Load the raw JSON: nbformat.read(as_version=4) normalizes list-form
        # sources to strings, but the *file* must carry list sources for
        # Quarto to render cells without flattening them.
        import nbformat

        nb = json.loads(path.read_text(encoding="utf-8"))
        nbformat.validate(nb)
        return nb

    def test_sources_are_lists(self, notebook):
        # Guards the Quarto flattening bug: single-string sources lose their
        # newlines and every cell renders as a run-on block.
        for cell in notebook["cells"]:
            assert isinstance(cell["source"], list), (
                f"{cell['cell_type']} cell source must be a list of lines"
            )
            assert all(isinstance(ln, str) for ln in cell["source"])

    def test_first_cell_is_raw_frontmatter(self, notebook):
        first = notebook["cells"][0]
        assert first["cell_type"] == "raw"
        text = "".join(first["source"])
        assert re.search(r"^---\s*$", text, re.M), "frontmatter must open with ---"
        assert re.search(r"^title:\s*['\"]?", text, re.M), "frontmatter must carry a title"
        assert re.search(r"^subtitle:\s*['\"]?", text, re.M), "frontmatter must carry a subtitle"

    def test_opening_markdown_cell_is_framed(self, notebook):
        cells = [c for c in notebook["cells"] if c["cell_type"] == "markdown"]
        assert cells, "notebook has no markdown cells"
        opening = "".join(cells[0]["source"])
        # The generator strips the duplicated H1 and prepends a static-render
        # note, so the first markdown content is a framing callout.
        assert "Static render" in opening

    def test_site_and_repo_notebooks_match(self):
        for name in self.NOTEBOOK_NAMES:
            site = (WEBSITE / "notebooks" / f"{name}.ipynb").read_bytes()
            repo = (ROOT / "notebooks" / f"{name}.ipynb").read_bytes()
            assert site == repo, f"site/repo notebooks out of sync: {name}"
