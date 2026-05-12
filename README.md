# arXiv 自动驾驶论文抓取与总结网页

Python 脚本负责抓取、分类、翻译总结和导出表格；Flask 网页只读取本地 JSON/CSV 并提供触发按钮。

## 安装

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
Copy-Item .env.example .env
```

在 `.env` 中设置 `GEMINI_API_KEY`，可选设置 `GEMINI_MODEL`、`MAX_RESULTS` 和 `ARXIV_OVERFETCH_FACTOR`。

## 使用

```powershell
python scripts/run_pipeline.py
python app.py
```

如果只想测试本地流程、不调用 Gemini：

```powershell
python scripts/run_pipeline.py --offline
```

网页默认运行在 `http://127.0.0.1:5000`。

## 单独脚本

```powershell
python scripts/fetch_arxiv.py --dry-run
python scripts/fetch_arxiv.py
python scripts/classify_keywords.py
python scripts/summarize_gemini.py
python scripts/export_table.py
```

最终表格保存在 `data/papers.json` 和 `data/papers.csv`。
