from pathlib import Path

from scripts.export_markdown import export_markdown, render_markdown


def test_render_markdown_includes_latest_version_and_old_version_link():
    markdown = render_markdown(
        [
            {
                "arxiv_id": "2604.28111v2",
                "title": "New Paper",
                "arxiv_url": "https://arxiv.org/abs/2604.28111v2",
                "pdf_url": "https://arxiv.org/pdf/2604.28111v2",
                "summary_zh": "中文总结",
                "older_versions": [
                    {
                        "arxiv_id": "2604.28111v1",
                        "version": 1,
                        "arxiv_url": "https://arxiv.org/abs/2604.28111v1",
                    }
                ],
            }
        ]
    )

    assert "New Paper" in markdown
    assert '<a href="https://arxiv.org/abs/2604.28111v1">v1</a>' in markdown
    assert "<table" in markdown
    assert '<col style="width: 34%;">' in markdown


def test_export_markdown_writes_fixed_markdown_path_and_latest_tables(tmp_path: Path):
    store_path = tmp_path / "papers_store.json"
    markdown_path = tmp_path / "docs" / "index.md"
    json_path = tmp_path / "papers.json"
    csv_path = tmp_path / "papers.csv"
    store_path.write_text(
        """
[
  {"arxiv_id": "2604.28111v1", "title": "Old", "arxiv_url": "https://arxiv.org/abs/2604.28111v1"},
  {"arxiv_id": "2604.28111v2", "title": "New", "arxiv_url": "https://arxiv.org/abs/2604.28111v2"}
]
""",
        encoding="utf-8",
    )

    exported = export_markdown(store_path, markdown_path, json_path, csv_path)

    assert markdown_path.exists()
    assert json_path.exists()
    assert csv_path.exists()
    assert [paper["arxiv_id"] for paper in exported] == ["2604.28111v2"]
    assert "旧版" in markdown_path.read_text(encoding="utf-8")
