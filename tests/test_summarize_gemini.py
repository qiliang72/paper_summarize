import sys
from types import SimpleNamespace

from scripts import summarize_gemini
from scripts.summarize_gemini import summarize_papers


def test_summarize_skips_existing_summary():
    papers = [{"abstract_zh": "中文摘要", "summary_zh": "中文总结"}]

    summarized = summarize_papers(papers, offline=True)

    assert summarized[0]["abstract_zh"] == "中文摘要"
    assert summarized[0]["summary_zh"] == "中文总结"


def test_summarize_offline_adds_fallback_summary():
    papers = [{"abstract_en": "This paper studies autonomous driving with VLM planning."}]

    summarized = summarize_papers(papers, offline=True)

    assert "Gemini 总结暂不可用" in summarized[0]["summary_zh"]


def test_summarize_without_api_key_records_error(monkeypatch):
    monkeypatch.delenv("GEMINI_API_KEY", raising=False)
    papers = [{"abstract_en": "This paper studies autonomous driving with VLM planning."}]

    summarized = summarize_papers(papers, offline=False)

    assert summarized[0]["summary_error"] == "GEMINI_API_KEY is not set; used fallback summary."
    assert "Gemini 总结暂不可用" in summarized[0]["summary_zh"]


def test_summarize_disables_api_after_two_consecutive_failures(monkeypatch):
    calls = []

    class FakeGenai:
        class Client:
            def __init__(self, api_key):
                self.api_key = api_key

    def fail_summary(client, model, paper):
        calls.append(paper["arxiv_id"])
        raise RuntimeError("429 RESOURCE_EXHAUSTED")

    monkeypatch.setenv("GEMINI_API_KEY", "test-key")
    monkeypatch.setitem(sys.modules, "google", SimpleNamespace(genai=FakeGenai))
    monkeypatch.setattr(summarize_gemini, "summarize_one", fail_summary)

    papers = [
        {"arxiv_id": "1v1", "abstract_en": "one"},
        {"arxiv_id": "2v1", "abstract_en": "two"},
        {"arxiv_id": "3v1", "abstract_en": "three"},
    ]

    summarized = summarize_papers(
        papers,
        offline=False,
        delay_seconds=0,
        retry_count=0,
        failure_threshold=2,
        verbose=False,
    )

    assert calls == ["1v1", "2v1"]
    assert summarized[2]["summary_error"] == "Gemini API skipped after 2 consecutive failures in this run."
    assert summarized[2].get("summary_zh", "") == ""
