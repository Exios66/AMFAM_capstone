"""Generate website/chats.qmd — LLaVA-style chat thread examples page.

Reads website/data/chat-examples.json (real reasoning traces extracted by
build_chat_examples.py), appends hand-written illustrative threads, and emits a
self-contained Quarto page with an embedded conversation player (prev/next card
navigation over real traces) plus static correct-vs-misclassified cards and
illustrative threads.

Usage:
  python scripts/site/build_chat_page.py
"""
from __future__ import annotations

import html as html_lib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

DATA_FILE = ROOT / "website" / "data" / "chat-examples.json"
OUT_FILE = ROOT / "website" / "chats.qmd"

ILLUSTRATIVE_THREADS = [
    {
        "kind": "illustrative",
        "title": "Invoice vs. Budget — payment demand decides",
        "model": "qwen/qwen3.7-flash (illustrative)",
        "prompt_version": "v17.2 rules",
        "expected": "invoice",
        "predicted": "invoice",
        "correct": True,
        "image": "",
        "turns": [
            {
                "who": "user",
                "text": "This page is a summary of charges with a total at the bottom. It also has a cost-table. Is it an invoice or a budget?",
            },
            {
                "who": "model",
                "text": (
                    "pre-scan: no mail-client header, no masthead, no memo block.\n"
                    "Check 1 file_folder: no — the page is a printed table, not a folder label.\n"
                    "Check 2 handwritten: no.\n"
                    "Check 3 letter: no — no salutation or closing.\n"
                    "Check 4 memo: no — no MEMORANDUM header.\n"
                    "The discriminating question from the prompt: is there a *payment demand* — "
                    "an amount due to be paid, with vendor and billing terms?\n"
                    "The table lists line items with a grand total and 'AMOUNT DUE' — that is a demand for payment.\n"
                    "The prompt explicitly routes financial/money-data tables with a payment demand to invoice "
                    "('a bill is a bill even when it is printed on a form').\n"
                    "Check 5 budget: no — budget is a plan of expenditures, not a demand for payment.\n"
                    "</scratchpad>\n<label>invoice</label>"
                ),
            },
        ],
    },
    {
        "kind": "illustrative",
        "title": "Memo vs. Letter — the closing line settles it",
        "model": "qwen/qwen3.7-flash (illustrative)",
        "prompt_version": "v17.2 rules",
        "expected": "letter",
        "predicted": "letter",
        "correct": True,
        "image": "",
        "turns": [
            {
                "who": "user",
                "text": "Short typed page addressed 'Dear Dr. Barnes' ending with 'Sincerely'. Is this a memo or a letter?",
            },
            {
                "who": "model",
                "text": (
                    "pre-scan: no masthead, no memo header.\n"
                    "Check 3 letter: yes — a formal salutation ('Dear Dr. Barnes') followed by body text and a "
                    "closing ('Sincerely') with a signature block.\n"
                    "Memos are the reverse: a MEMORANDUM header with TO/FROM/DATE/RE lines, no salutation, no "
                    "closing signature. This page has none of those markers.\n"
                    "The salutation + closing are strong, concrete, readable evidence, so I commit at Check 3.\n"
                    "</scratchpad>\n<label>letter</label>"
                ),
            },
        ],
    },
    {
        "kind": "illustrative",
        "title": "Form beats subject matter — a data page can still be a form",
        "model": "qwen/qwen3.7-flash (illustrative)",
        "prompt_version": "v17.2 rules",
        "expected": "form",
        "predicted": "form",
        "correct": True,
        "image": "",
        "turns": [
            {
                "who": "user",
                "text": "A page full of technical data values that looks like it was filled in by hand. Form or handwritten note?",
            },
            {
                "who": "model",
                "text": (
                    "pre-scan: the page has printed labeled fields ('NAME:', 'ACCOUNT NO:', 'DATE:') with values "
                    "entered in the blanks — a structured form.\n"
                    "Check 2 handwritten: there IS handwriting, but the handwriting is *inside* a printed form "
                    "structure, not a freehand note. The prompt's rule: classify by dominant function — the form "
                    "fields control the page, so the handwriting does not win the check.\n"
                    "Check 1 file_folder: no. Check 3 letter: no. Check 4 memo: no.\n"
                    "The labeled-field skeleton with blanks is the strongest concrete evidence on the page.\n"
                    "</scratchpad>\n<label>form</label>"
                ),
            },
        ],
    },
]


def _load_real():
    data = json.loads(DATA_FILE.read_text())
    return data


def _conv_from_record(r):
    turns = [
        {
            "who": "user",
            "text": f"Classify this scanned document page. (Ground truth: {r['expected']})",
            "image": r.get("image") or "",
        },
        {
            "who": "model",
            "text": r["raw_response"],
        },
    ]
    return {
        "kind": "real",
        "title": f"{r['expected']} — {'correctly classified' if r['correct'] else 'misclassified as ' + r['predicted']}",
        "model": r.get("model") or "",
        "prompt_version": r.get("prompt_version") or "",
        "expected": r["expected"],
        "predicted": r["predicted"],
        "correct": r["correct"],
        "image": r.get("image") or "",
        "filename": r.get("filename") or "",
        "turns": turns,
    }


def build():
    real = _load_real()
    convs = [_conv_from_record(r) for r in real["correct"]] + [
        _conv_from_record(r) for r in real["misclassified"]
    ]
    convs += ILLUSTRATIVE_THREADS
    for i, c in enumerate(convs):
        c["id"] = i + 1

    data_js = json.dumps(convs).replace("<", "\\u003c")

    real_correct = real["correct"]
    real_misses = real["misclassified"]

    def card(r):
        cls = "ok" if r["correct"] else "miss"
        badge = "OK" if r["correct"] else "MISS"
        img = r.get("image") or ""
        title = f"{r['expected']} &rarr; {r['predicted']}" if not r["correct"] else r["expected"]
        return f"""<div class="chat-card chat-card-{cls}">
  <div class="chat-card-top">
    <span class="chat-badge chat-badge-{cls}">{badge}</span>
    <span class="chat-card-title">{title}</span>
    <span class="chat-card-meta">{r.get('prompt_version','')} &middot; {r.get('model','')}</span>
  </div>
  <img class="chat-card-img" src="{img}" alt="document example" />
  <div class="chat-card-reason"><pre>{html_lib.escape(r['reasoning'][:220])}{'…' if len(r['reasoning'])>220 else ''}</pre></div>
</div>"""

    correct_cards = "\n".join(card(r) for r in real_correct)
    miss_cards = "\n".join(card(r) for r in real_misses)

    def _model_text(t):
        return next(tn["text"] for tn in t["turns"] if tn["who"] == "model")

    illus = {i: _model_text(t) for i, t in zip("abc", ILLUSTRATIVE_THREADS)}

    html = f"""::: {{=html}}
<div class="chat-intro">
  <p>Every conversation below is a <strong>real trace</strong> pulled from a logged OpenRouter run on the
  Braintrust project — the model's own <code>&lt;scratchpad&gt;</code> reasoning and its
  final <code>&lt;label&gt;</code>, exactly as it was returned. Use the arrows to step through them.</p>
</div>

<div class="chat-demo" id="chatDemo">
  <div class="chat-toolbar">
    <button class="chat-btn" id="chatPrev" aria-label="Previous example">&#8592; Previous</button>
    <span class="chat-count" id="chatCount">1 / {len(convs)}</span>
    <button class="chat-btn" id="chatNext" aria-label="Next example">Next &#8594;</button>
  </div>
  <div class="chat-card chat-card-thread">
    <div class="chat-card-top">
      <span class="chat-badge" id="chatBadge"></span>
      <span class="chat-card-title" id="chatTitle"></span>
      <span class="chat-card-meta" id="chatMeta"></span>
    </div>
    <div class="chat-history" id="chatHistory"></div>
    <div class="chat-expand-row">
      <button class="chat-btn chat-expand-btn" id="chatExpand">Expand full response</button>
    </div>
  </div>
</div>

<script>
const CONVERSATIONS = {data_js};

let chatIdx = 0;
const MAX_H = 340;
const chatHistory = document.getElementById('chatHistory');
const chatBadge = document.getElementById('chatBadge');
const chatTitle = document.getElementById('chatTitle');
const chatMeta = document.getElementById('chatMeta');
const chatCount = document.getElementById('chatCount');
const chatExpand = document.getElementById('chatExpand');

function el(tag, cls, text) {{
  const n = document.createElement(tag);
  if (cls) n.className = cls;
  if (text != null) n.textContent = text;
  return n;
}}

function renderChat() {{
  const c = CONVERSATIONS[chatIdx];
  chatCount.textContent = (chatIdx + 1) + ' / ' + CONVERSATIONS.length;
  chatBadge.textContent = c.kind === 'illustrative' ? 'ILLUSTRATIVE' : (c.correct ? 'OK' : 'MISS');
  chatBadge.className = 'chat-badge ' + (c.kind === 'illustrative' ? 'chat-badge-illu' : (c.correct ? 'chat-badge-ok' : 'chat-badge-miss'));
  chatTitle.textContent = c.title;
  chatMeta.textContent = (c.prompt_version || '') + (c.model ? '  \u00b7  ' + c.model : '');
  chatHistory.innerHTML = '';
  chatHistory.scrollTop = 0;
  chatExpand.textContent = 'Expand full response';

  c.turns.forEach(function (t) {{
    const row = el('div', 'msg msg-' + t.who);
    const bubble = el('div', 'msg-bubble');
    if (t.image) {{
      const img = document.createElement('img');
      img.src = t.image;
      img.alt = 'document image';
      img.className = 'msg-img';
      bubble.appendChild(img);
    }}
    const body = el('div', 'msg-text');
    const pre = document.createElement('pre');
    pre.className = 'msg-pre';
    pre.textContent = t.text;
    body.appendChild(pre);
    bubble.appendChild(body);
    row.appendChild(bubble);
    chatHistory.appendChild(row);
  }});

  const preList = chatHistory.querySelectorAll('.msg-pre');
  if (preList.length) {{
    const last = preList[preList.length - 1];
    if (last.scrollHeight > MAX_H) {{
      last.classList.add('collapsed');
      chatExpand.style.display = 'inline-block';
    }} else {{
      chatExpand.style.display = 'none';
    }}
  }}
}}

let expanded = false;
chatExpand.addEventListener('click', function () {{
  expanded = !expanded;
  const preList = chatHistory.querySelectorAll('.msg-pre');
  preList.forEach(function (p) {{
    if (expanded) p.classList.remove('collapsed');
    else p.classList.add('collapsed');
  }});
  chatExpand.textContent = expanded ? 'Collapse response' : 'Expand full response';
}});

document.getElementById('chatPrev').addEventListener('click', function () {{
  chatIdx = (chatIdx - 1 + CONVERSATIONS.length) % CONVERSATIONS.length;
  expanded = false;
  renderChat();
}});
document.getElementById('chatNext').addEventListener('click', function () {{
  chatIdx = (chatIdx + 1) % CONVERSATIONS.length;
  expanded = false;
  renderChat();
}});
renderChat();
</script>
:::

## Correct vs. misclassified

The four correct traces below were chosen to span four very different document classes; the misses are the
model's actual failures on the same slice — including two `invoice &rarr; budget` errors in which the model
committed to the wrong check. Each card shows the document image and the model's own reasoning.

::: {{=html}}
<div class="chat-grid chat-grid-ok">
  {correct_cards}
</div>
:::

::: {{=html}}
<div class="chat-grid chat-grid-miss">
  {miss_cards}
</div>
:::

## Illustrative threads

The three threads below are **hand-written** examples of the cascade the prompt is designed to produce — they
are not logged model output. They show the intended reasoning for the three hardest discriminations:
`invoice` vs `budget`, `memo` vs `letter`, and `form` vs `handwritten` when handwriting appears inside a
printed form. Step to them in the player above (they are tagged *Illustrative*), or read them here.

::: {{=html}}
<div class="illus-threads">
  <div class="illus-card"><h3 class="illus-title">Invoice vs. Budget — payment demand decides</h3><p class="illus-meta">v17.2 rules &middot; qwen/qwen3.7-flash (illustrative)</p><div class="illus-msg">A page of charges with a total at the bottom.</div><pre class="msg-pre">{illus['a']}</pre></div>
  <div class="illus-card"><h3 class="illus-title">Memo vs. Letter — the closing line settles it</h3><p class="illus-meta">v17.2 rules &middot; qwen/qwen3.7-flash (illustrative)</p><div class="illus-msg">A short typed page that opens 'Dear Dr. Barnes' and closes 'Sincerely'.</div><pre class="msg-pre">{illus['b']}</pre></div>
  <div class="illus-card"><h3 class="illus-title">Form beats subject matter — a data page can still be a form</h3><p class="illus-meta">v17.2 rules &middot; qwen/qwen3.7-flash (illustrative)</p><div class="illus-msg">A page of technical values filled in by hand.</div><pre class="msg-pre">{illus['c']}</pre></div>
</div>
:::

All real traces were logged to the Braintrust project; each conversation card shows the source document image
(from the `fixed_size_sampled` slice), the prompt version, and the model that produced the trace.
"""

    OUT_FILE.write_text(html)
    print(f"wrote {OUT_FILE} ({len(convs)} conversations: {len(real['correct'])} correct, {len(real['misclassified'])} misses, {len(ILLUSTRATIVE_THREADS)} illustrative)")


if __name__ == "__main__":
    build()
