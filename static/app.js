const state = {
  papers: [],
};

const rows = document.querySelector("#paperRows");
const emptyState = document.querySelector("#emptyState");
const searchInput = document.querySelector("#searchInput");
const topicFilter = document.querySelector("#topicFilter");
const categoryFilter = document.querySelector("#categoryFilter");
const sortSelect = document.querySelector("#sortSelect");
const runButton = document.querySelector("#runButton");
const statusText = document.querySelector("#statusText");

function text(value) {
  return String(value ?? "");
}

function list(value) {
  return Array.isArray(value) ? value : [];
}

function chipList(items) {
  if (!items.length) return '<span class="chip">无</span>';
  return items.map((item) => `<span class="chip">${escapeHtml(item)}</span>`).join("");
}

function escapeHtml(value) {
  return text(value)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#039;");
}

function truncate(value, maxLength = 220) {
  const clean = text(value).trim();
  if (clean.length <= maxLength) return clean;
  return `${clean.slice(0, maxLength).trim()}...`;
}

function populateFilters() {
  const topics = new Set();
  const categories = new Set();
  state.papers.forEach((paper) => {
    list(paper.topic_keywords).forEach((item) => topics.add(item));
    list(paper.arxiv_categories).forEach((item) => categories.add(item));
  });

  topicFilter.innerHTML = '<option value="">全部主题</option>';
  [...topics].sort().forEach((item) => {
    topicFilter.insertAdjacentHTML("beforeend", `<option value="${escapeHtml(item)}">${escapeHtml(item)}</option>`);
  });

  categoryFilter.innerHTML = '<option value="">全部分类</option>';
  [...categories].sort().forEach((item) => {
    categoryFilter.insertAdjacentHTML("beforeend", `<option value="${escapeHtml(item)}">${escapeHtml(item)}</option>`);
  });
}

function filteredPapers() {
  const query = searchInput.value.trim().toLowerCase();
  const topic = topicFilter.value;
  const category = categoryFilter.value;
  const direction = sortSelect.value;

  return state.papers
    .filter((paper) => {
      const haystack = [
        paper.title,
        paper.abstract_en,
        paper.abstract_zh,
        paper.summary_zh,
        ...list(paper.domain_keywords),
        ...list(paper.topic_keywords),
      ].join(" ").toLowerCase();
      return !query || haystack.includes(query);
    })
    .filter((paper) => !topic || list(paper.topic_keywords).includes(topic))
    .filter((paper) => !category || list(paper.arxiv_categories).includes(category))
    .sort((a, b) => {
      const left = Date.parse(a.published || "") || 0;
      const right = Date.parse(b.published || "") || 0;
      return direction === "asc" ? left - right : right - left;
    });
}

function renderInfo(paper, date) {
  return `
    <div class="meta-stack">
      <span class="date">${escapeHtml(date)}</span>
      <div class="chips compact">${chipList(list(paper.arxiv_categories))}</div>
      <div class="links inline-links">
        <a href="${escapeHtml(paper.arxiv_url)}" target="_blank" rel="noreferrer">arXiv</a>
        <a href="${escapeHtml(paper.pdf_url)}" target="_blank" rel="noreferrer">PDF</a>
      </div>
    </div>
  `;
}

function renderAbstract(paper) {
  const abstract = paper.abstract_zh || paper.abstract_en || "";
  if (!abstract) return '<span class="muted">无摘要</span>';
  return `
    <details class="abstract-fold">
      <summary>${escapeHtml(truncate(abstract))}</summary>
      <p>${escapeHtml(abstract)}</p>
    </details>
  `;
}

function render() {
  const papers = filteredPapers();
  rows.innerHTML = "";
  emptyState.hidden = papers.length > 0;

  papers.forEach((paper) => {
    const tr = document.createElement("tr");
    const date = paper.published ? new Date(paper.published).toLocaleDateString("zh-CN") : "";
    tr.innerHTML = `
      <td class="title">${escapeHtml(paper.title)}</td>
      <td class="info">${renderInfo(paper, date)}</td>
      <td class="keyword-cell"><div class="chips">${chipList(list(paper.topic_keywords))}</div></td>
      <td class="abstract">${renderAbstract(paper)}</td>
      <td class="short-summary">${escapeHtml(paper.summary_zh || "")}</td>
    `;
    rows.appendChild(tr);
  });
}

async function loadPapers() {
  const response = await fetch("/api/papers");
  state.papers = await response.json();
  populateFilters();
  render();
}

async function loadStatus() {
  const response = await fetch("/api/status");
  const status = await response.json();
  const updated = status.updated_at ? ` · ${new Date(status.updated_at).toLocaleString("zh-CN")}` : "";
  statusText.textContent = `${status.status}: ${status.message || ""}${updated}`;
  runButton.disabled = status.status === "running";
  if (status.status === "success") {
    await loadPapers();
  }
}

async function runPipeline() {
  runButton.disabled = true;
  const response = await fetch("/api/run", { method: "POST" });
  if (!response.ok && response.status !== 409) {
    statusText.textContent = "error: 无法启动更新任务。";
  }
  await loadStatus();
}

[searchInput, topicFilter, categoryFilter, sortSelect].forEach((element) => {
  element.addEventListener("input", render);
});
runButton.addEventListener("click", runPipeline);

loadPapers();
loadStatus();
setInterval(loadStatus, 3000);
