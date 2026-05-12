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
