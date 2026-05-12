from paper_app.paper_store import latest_papers_with_versions, merge_new_papers, split_arxiv_id


def test_split_arxiv_id_extracts_base_and_version():
    assert split_arxiv_id("2604.28111v2") == ("2604.28111", 2)
    assert split_arxiv_id("custom-id") == ("custom-id", None)


def test_merge_new_papers_skips_duplicate_full_arxiv_id():
    existing = [{"arxiv_id": "2604.28111v1", "title": "Old"}]
    incoming = [{"arxiv_id": "2604.28111v1", "title": "Changed"}]

    merged, added = merge_new_papers(existing, incoming)

    assert added == []
    assert len(merged) == 1
    assert merged[0]["title"] == "Old"


def test_merge_new_papers_keeps_new_version_without_overwriting_old_version():
    existing = [{"arxiv_id": "2604.28111v1", "title": "Old"}]
    incoming = [{"arxiv_id": "2604.28111v2", "title": "New"}]

    merged, added = merge_new_papers(existing, incoming)

    assert [paper["arxiv_id"] for paper in added] == ["2604.28111v2"]
    assert {paper["arxiv_id"] for paper in merged} == {"2604.28111v1", "2604.28111v2"}


def test_latest_papers_show_only_newest_version_with_old_version_links():
    papers = [
        {
            "arxiv_id": "2604.28111v1",
            "title": "Old",
            "updated": "2026-05-01T00:00:00+00:00",
            "arxiv_url": "https://arxiv.org/abs/2604.28111v1",
        },
        {
            "arxiv_id": "2604.28111v2",
            "title": "New",
            "updated": "2026-05-02T00:00:00+00:00",
            "arxiv_url": "https://arxiv.org/abs/2604.28111v2",
        },
    ]

    latest = latest_papers_with_versions(papers)

    assert len(latest) == 1
    assert latest[0]["arxiv_id"] == "2604.28111v2"
    assert [paper["arxiv_id"] for paper in latest[0]["older_versions"]] == ["2604.28111v1"]
