# arXiv 自动驾驶论文抓取与总结网页

Python 脚本负责手动抓取 arXiv 基础信息、增量补齐中文翻译和总结，并导出本地表格与 `docs/index.md`。Flask 网页读取本地 JSON，并可触发“补摘要 + 导出”，不会自动抓取 arXiv。

## 安装

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
Copy-Item .env.example .env
```

在 `.env` 中设置 `GEMINI_API_KEY`，可选设置 `GEMINI_MODEL`、`MAX_RESULTS` 和 `ARXIV_OVERFETCH_FACTOR`。

## 使用

手动发现并追加新论文基础信息：

```powershell
python scripts/update_paper_base.py
```

日常流程只补齐缺失中文字段并导出最新页面：

```powershell
python scripts/run_pipeline.py
```

如果只想测试本地流程、不调用 Gemini：

```powershell
python scripts/run_pipeline.py --offline
```

网页默认运行在 `http://127.0.0.1:5000`：

```powershell
python app.py
```

## 单独脚本

```powershell
python scripts/update_paper_base.py --dry-run
python scripts/update_paper_base.py
python scripts/fill_summaries.py
python scripts/export_markdown.py
```

长期论文列表保存在 `data/papers_store.json`。最新版展示表格保存在 `data/papers.json` 和 `data/papers.csv`，Markdown 页面保存在 `docs/index.md`。
