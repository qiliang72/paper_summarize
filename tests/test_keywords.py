import sys
from types import SimpleNamespace

from paper_app.config import load_config
from paper_app.keyword_utils import find_keyword_matches, keyword_matches
from scripts.fetch_arxiv import _set_request_timeout, build_query, fetch_papers


def test_keyword_matching_is_case_and_separator_insensitive():
    assert keyword_matches("This is an End to End autonomous driving method.", "end-to-end")
    assert keyword_matches("We use a vision language model.", "vision-language model")
    assert keyword_matches("VLM planning for self driving.", "vlm")
    assert keyword_matches("An E2E planner for driving.", "e2e")


def test_short_acronyms_require_word_boundaries():
    assert keyword_matches("RL improves the planner.", "RL")
    assert not keyword_matches("A world model improves the planner.", "RL")


def test_configured_domain_keywords_exclude_ad_abbreviation():
    config = load_config()

    assert find_keyword_matches("AD planning benchmark", config.domain_keywords) == []
    assert find_keyword_matches("End-to-end autonomous driving planner.", config.domain_keywords) == [
        "autonomous driving",
        "end-to-end",
    ]


def test_topic_keyword_variants_return_canonical_labels():
    config = load_config()

    text = "Vision-language models and LVLMs use reinforcement learning and RL."

    assert find_keyword_matches(text, config.topic_keywords) == ["VLM", "RL"]


def test_distillation_typo_variant_is_not_configured():
    config = load_config()

    assert keyword_matches("Policy distillation for driving.", "distillation")
    assert find_keyword_matches("Policy distrillation for driving.", config.topic_keywords) == []


def test_end_to_end_variants_return_canonical_domain_label():
    config = load_config()

    assert find_keyword_matches("End to end planning.", config.domain_keywords) == ["end-to-end"]
    assert find_keyword_matches("E2E planning.", config.domain_keywords) == ["end-to-end"]


def test_fetch_query_requires_all_domain_groups_and_any_topic_group():
    query = build_query()

    assert '(ti:"autonomous driving"' in query
    assert ') AND (ti:"end-to-end"' in query
    assert '(ti:"VLM"' in query
    assert ') OR (ti:"world model"' in query
    assert 'ti:"AD"' not in query
    assert 'abs:"AD"' not in query
    assert "distrillation" not in query


def test_fetch_papers_caps_page_size_to_fetch_limit(monkeypatch):
    captured = {}

    class FakeSession:
        def get(self, url, **kwargs):
            return None

    class FakeClient:
        def __init__(self, page_size, delay_seconds, num_retries):
            captured["page_size"] = page_size
            captured["delay_seconds"] = delay_seconds
            captured["num_retries"] = num_retries
            self._session = FakeSession()

        def results(self, search):
            captured["max_results"] = search.max_results
            return []

    class FakeSearch:
        def __init__(self, query, max_results, sort_by, sort_order):
            self.query = query
            self.max_results = max_results
            self.sort_by = sort_by
            self.sort_order = sort_order

    fake_arxiv = SimpleNamespace(
        Client=FakeClient,
        Search=FakeSearch,
        SortCriterion=SimpleNamespace(SubmittedDate="submitted"),
        SortOrder=SimpleNamespace(Descending="descending"),
    )
    monkeypatch.setitem(sys.modules, "arxiv", fake_arxiv)
    monkeypatch.setenv("MAX_RESULTS", "1")
    monkeypatch.setenv("ARXIV_OVERFETCH_FACTOR", "1")

    assert fetch_papers() == []
    assert captured["page_size"] == 1
    assert captured["max_results"] == 1
    assert captured["num_retries"] == 1


def test_set_request_timeout_adds_default_timeout():
    captured = {}

    class FakeSession:
        def get(self, url, **kwargs):
            captured["url"] = url
            captured["kwargs"] = kwargs

    client = SimpleNamespace(_session=FakeSession())

    _set_request_timeout(client, 12.5)
    client._session.get("https://export.arxiv.org/api/query", headers={"user-agent": "test"})

    assert captured["kwargs"]["timeout"] == 12.5
