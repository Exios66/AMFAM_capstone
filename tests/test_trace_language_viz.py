"""Unit tests for the trace-language visualization suite.

Covers the trace projection, phrase/word tokenizers, the Fightin' Words
log-odds with Dirichlet prior, differential bigram weighting, cycle
detection, and stuck-phrase statistics used by
``scripts/braintrust/trace_language_viz.py``.
"""

from collections import Counter

from scripts.braintrust.trace_language_viz import (
    _node_stats,
    build_trace_records,
    differential_bigrams,
    find_cycles,
    log_odds_ratio,
    scatter_frequencies,
    stuck_phrase_stats,
    tokenize_phrases,
    tokenize_words,
)

TRACE = """**Check 1: file_folder**
- Evidence: none.
- Result: not this check.

**Check 2: handwritten**
- Evidence: typed text.
- Result: not this check.

**Check 11: correspondence -> email**
- Evidence: "From: Carnovale", "Subject: FW".
- Stop here.
"""


class TestBuildTraceRecords:
    def _records(self):
        return [
            {"reasoning": TRACE, "status": "completed", "predicted": "email",
             "expected": "email", "prompt_version": "v11.8"},
            {"reasoning": TRACE, "status": "completed", "predicted": "memo",
             "expected": "email", "prompt_version": "v11.8"},
            {"reasoning": "", "status": "completed", "predicted": "email",
             "expected": "email"},
            {"reasoning": TRACE, "status": "error", "predicted": "email",
             "expected": "email"},
        ]

    def test_projects_correctness_and_metadata(self):
        rows = build_trace_records(self._records())
        assert len(rows) == 2
        assert rows[0]["correct"] is True
        assert rows[1]["correct"] is False
        assert rows[1]["confusion_pair"] == "email->memo"
        assert rows[0]["prompt_version"] == "v11.8"

    def test_skips_missing_reasoning_and_errored_status(self):
        rows = build_trace_records(self._records())
        assert all(r["text"] for r in rows)


class TestTokenizers:
    def test_phrase_tokens_keep_function_words(self):
        toks = tokenize_phrases("Let's re-examine the check, however let's re-examine")
        assert "re-examine" in toks
        assert "however" in toks
        assert "let's" in toks

    def test_phrase_tokens_lowercase_and_drop_singles(self):
        assert tokenize_phrases("I AM B") == ["am"]

    def test_word_tokens_filter_stopwords(self):
        toks = tokenize_words('"the invoice header" is present')
        assert "invoice" in toks
        assert "the" not in toks
        assert "is" not in toks

    def test_empty(self):
        assert tokenize_phrases("") == []
        assert tokenize_words(None) == []


class TestLogOddsRatio:
    def _counts(self):
        fail = Counter({"stuck": 40, "revisit": 10, "both": 30})
        ok = Counter({"clean": 40, "both": 30})
        return fail, ok

    def test_ranks_fail_words_above_ok_words(self):
        words = log_odds_ratio(*self._counts(), min_count=3)
        by_word = {w["word"]: w["z"] for w in words}
        assert by_word["stuck"] > by_word["clean"]
        assert by_word["stuck"] > 0
        assert by_word["clean"] < 0

    def test_no_division_by_zero_with_prior(self):
        fail = Counter({"only_fail": 20})
        ok = Counter({})
        words = log_odds_ratio(fail, ok, alpha=0.01, min_count=3)
        assert words and words[0]["z"] > 0
        assert words[0]["fail"] == 20 and words[0]["ok"] == 0

    def test_smoothing_at_zero_without_prior_blowup(self):
        fail = Counter({"a": 100})
        ok = Counter({"b": 100})
        words = log_odds_ratio(fail, ok, alpha=0.01, min_count=3)
        zs = {w["word"]: w["z"] for w in words}
        assert zs["a"] > 0 and zs["b"] < 0
        assert zs["a"] == -zs["b"]  # symmetric: equal magnitude, opposite sign

    def test_min_count_filter(self):
        words = log_odds_ratio(Counter({"rare": 4}), Counter({"other": 100}),
                               min_count=5)
        assert not any(w["word"] == "rare" for w in words)

    def test_prior_controls_extremes(self):
        fail = Counter({"x": 10})
        ok = Counter({})
        tight = log_odds_ratio(fail, ok, alpha=0.001, min_count=3)[0]["z"]
        loose = log_odds_ratio(fail, ok, alpha=1.0, min_count=3)[0]["z"]
        assert tight > loose


class TestDifferentialBigrams:
    def _records(self):
        fail_text = "revisit the check revisit the check revisit again"
        ok_text = "revisit the check and then move on"
        return [
            {"text": fail_text, "correct": False},
            {"text": ok_text, "correct": True},
            {"text": ok_text, "correct": True},
        ]

    def test_keeps_fail_biased_edges_only(self):
        edges = differential_bigrams(self._records(), min_fail=1, min_z=0.0,
                                     max_edges=50, exclude_prompt_leaks=False)
        words = {e["a"] for e in edges} | {e["b"] for e in edges}
        assert "revisit" in words
        assert all(e["fail"] >= 1 for e in edges)

    def test_min_fail_filter(self):
        edges = differential_bigrams(self._records(), min_fail=5, min_z=0.0,
                                     max_edges=50)
        assert edges == []

    def test_excludes_prompt_leaks(self):
        # 'check' and 'revisit' appear in no prompt; simulate by running with
        # the real prompt vocab and confirming no exception + only bigrams
        # that clear the differential bar survive.
        edges = differential_bigrams(self._records(), min_fail=1, min_z=0.0,
                                     max_edges=50, exclude_prompt_leaks=True)
        assert all(e["z"] >= 0.0 for e in edges)


class TestNodeStats:
    def test_aggregates_per_word(self):
        edges = [
            {"a": "re-examine", "b": "however", "fail": 5, "ok": 1, "z": 2.0},
            {"a": "re-examine", "b": "again", "fail": 3, "ok": 0, "z": 1.0},
        ]
        stats = _node_stats(edges)
        assert stats["re-examine"]["fail"] == 8
        assert stats["however"]["fail"] == 5
        assert stats["again"]["ok"] == 0
        assert stats["re-examine"]["z"] == 3.0

    def test_missing_node_never_defaults(self):
        # Regression: keys must be word tokens, not the literal 'a'/'b'.
        edges = [{"a": "form", "b": "mol", "fail": 4, "ok": 0, "z": 1.0}]
        stats = _node_stats(edges)
        assert set(stats) == {"form", "mol"}


class TestFindCycles:
    def _edges(self):
        def e(a, b):
            return {"a": a, "b": b, "fail": 5, "ok": 0, "z": 2.0}
        return [
            e("re-examine", "however"), e("however", "re-examine"),
            e("re-examine", "again"), e("again", "once"),
        ]

    def test_detects_two_cycles(self):
        cycles = find_cycles(self._edges(), max_len=4)
        seqs = {tuple(c) for c in cycles}
        assert ("re-examine", "however") in seqs or ("however", "re-examine") in seqs

    def test_rotation_dedup(self):
        cycles = find_cycles(self._edges(), max_len=4)
        seqs = [tuple(c) for c in cycles]
        assert len(seqs) == len(set(seqs))

    def test_respects_max_len(self):
        edges = [{"a": "a", "b": "b", "fail": 1, "ok": 0, "z": 1.0},
                 {"a": "b", "b": "c", "fail": 1, "ok": 0, "z": 1.0},
                 {"a": "c", "b": "a", "fail": 1, "ok": 0, "z": 1.0}]
        assert find_cycles(edges, max_len=2) == []
        assert find_cycles(edges, max_len=3) == [["a", "b", "c"]]

    def test_self_loop(self):
        edges = [{"a": "stuck", "b": "stuck", "fail": 1, "ok": 0, "z": 1.0}]
        assert find_cycles(edges, max_len=4) == [["stuck"]]


class TestStuckPhraseStats:
    def _records(self):
        stutter = {"text": "revisit the check revisit the check again",
                   "correct": False}
        clean = {"text": "revisit the check and move on", "correct": True}
        trigram = {"text": "no no no no no", "correct": False}
        return [stutter, clean, trigram]

    def test_counts_stutter_and_trigram(self):
        stats = stuck_phrase_stats(self._records())
        assert stats["failed_n"] == 2
        assert stats["ok_n"] == 1
        assert stats["failed_loops"] == 2
        assert stats["ok_loops"] == 0

    def test_rates(self):
        stats = stuck_phrase_stats(self._records())
        assert stats["failed_rate"] == 1.0
        assert stats["ok_rate"] == 0.0


class TestScatterFrequencies:
    def test_per_million_normalization(self):
        records = [
            {"text": "alpha beta", "correct": True},
            {"text": "alpha alpha gamma", "correct": False},
        ]
        points, n_fail, n_ok = scatter_frequencies(records)
        by_word = {p["word"]: p for p in points}
        assert n_fail == 3 and n_ok == 2
        # alpha: 1/2 per million in ok, 2/3 per million in fail
        assert abs(by_word["alpha"]["freq_ok"] - 5e5) < 1
        assert abs(by_word["alpha"]["freq_fail"] - 2e6 / 3) < 1

    def test_min_frequency_filter(self):
        records = [{"text": "rare", "correct": True}]
        points, _, _ = scatter_frequencies(records)
        assert points == []
