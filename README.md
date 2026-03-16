# Python for Good: Revealing the Philippines Through Data

> A hands-on workshop using Python to compare the Philippines' SDG performance with other nations — and publishing the results as an interactive web report.

**Live report:** https://ogbinar.github.io/py-sdg-eda-workshop

**PythonAsia 2026** · Sunday, March 22 · 1:15 PM · Yuchengco Hall 5F, Room Y509

---

## What is this workshop about?

This workshop is part of the **PythonAsia 2026 Conference**. It demonstrates how Python can strengthen data literacy, promote transparency, and help citizens better understand how the Philippines compares with the rest of the world — and what insights can guide future progress.

The analysis explores several Sustainable Development Goal (SDG) indicators, including education and internet access, comparing the Philippines with regional peers and selected benchmark countries.

This workshop is not about politics. Instead, it focuses on how open data and simple analytical tools can be used responsibly to explore national development and ask better questions about the challenges we face.

In this 2-hour workshop, you will use Python and open global datasets to:

- Clean and explore cross-country SDG data
- Compare the Philippines against Southeast Asian and global peers
- Visualize patterns, gaps, and standout practices
- Publish your findings as an interactive web report

No prior data science experience is required — just basic Python familiarity.

---

## What you will learn

- **Data literacy** — how to read and interpret global SDG indicators
- **Critical thinking** — how to do fair country-to-country comparisons
- **Responsible analytics** — how to avoid misleading conclusions
- **Reproducible workflows** — how to share open, transparent analysis using Python

By the end, you will have built a reusable **SDG Comparison Notebook** and published it as a live website.

---

## Prerequisites

You only need two things installed on your computer:

- [Docker Desktop](https://www.docker.com/products/docker-desktop) — runs the project environment
- [VS Code](https://code.visualstudio.com/) with the [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)

Python, Quarto, and all libraries are handled automatically inside the container — you do not need to install anything else.

---

## Getting started

### Step 1 — Clone the repo

```bash
git clone https://github.com/ogbinar/py-sdg-eda-workshop.git
cd py-sdg-eda-workshop
code .
```

### Step 2 — Open in dev container

When VS Code opens, you will see a popup in the bottom right:

```
"Folder contains a Dev Container configuration file. Reopen in Container?"
```

Click **Reopen in Container**. VS Code will build the environment automatically. This takes a few minutes the first time.

You can also trigger it manually:
```
Ctrl+Shift+P → Dev Containers: Open Folder in Container
```

### Step 3 — Verify everything is working

Open the terminal inside VS Code and run:

```bash
python --version    # should show 3.12
quarto --version    # should show 1.9.35
uv pip list         # should list all project dependencies
```

---

## Workshop workflow

Once your environment is ready, the full workflow is four steps:

### 1. Fetch the data

This pulls SDG indicator data from the World Bank API and saves it locally:

```bash
python run_pipeline.py
```

Output is saved to `data/raw/` and `data/curated/`.

---

### 2. Explore the notebook

Open the analysis notebook to review the charts and findings:

```bash
jupyter notebook sdg-eda-notebook-final.ipynb
```

This is where the SDG comparison happens — cleaning data, building charts, and drawing insights about the Philippines vs regional peers.

---

### 3. Render the report

Convert the notebook into a clean interactive HTML report:

```bash
quarto render 
```

Output goes to `docs/index.html`. Rendering settings are in `_quarto.yml`:
- Bootstrap Cosmo theme
- Sidebar table of contents
- Code cells hidden
- Self-contained single HTML file

---

### 4. Preview locally

Serve the report in your browser before publishing:

```bash
python -m http.server --directory docs
```

Then open: [http://localhost:8000](http://localhost:8000)

---

## Publishing to GitHub Pages

When you are happy with the report, deploy it as a live website:

```bash
git add docs/
git commit -m "Update report"
git push
```

Then enable GitHub Pages in your repository settings:

```
Settings → Pages → Source: Deploy from branch → Branch: main → Folder: /docs → Save
```

Your report will be live at:
```
https://<your-username>.github.io/<your-repo>/
```

---

## Project structure

```
py-sdg-eda-workshop/
│
├── .devcontainer/
│   ├── Dockerfile                    # Python 3.12 + Quarto + uv
│   └── devcontainer.json             # VS Code dev container config
│
├── data/
│   ├── raw/                          # Raw CSVs from World Bank API
│   └── curated/                      # Cleaned parquet files
│
├── docs/
│   └── index.html                    # Generated report (deployed to GitHub Pages)
│
├── src/
│   ├── config.py                     # Country and indicator configuration
│   ├── extract.py                    # World Bank API data fetching
│   ├── transform.py                  # Data cleaning and reshaping
│   └── pipeline.py                   # Orchestrates extract + transform
│
├── _quarto.yml                       # Quarto render settings
├── run_pipeline.py                   # Entry point: runs the data pipeline
├── sdg-eda-notebook-final.ipynb      # Main analysis notebook
├── pyproject.toml                    # Python dependency declarations
└── uv.lock                           # Pinned full dependency tree
```

---

## Architecture

| Step | Tool | Output |
|------|------|--------|
| 1. Fetch data | `run_pipeline.py` | `data/raw/`, `data/curated/*.parquet` |
| 2. Analyse | `sdg-eda-notebook-final.ipynb` | EDA + Plotly charts + markdown narrative |
| 3. Render | `quarto render` + `_quarto.yml` | `docs/index.html` |
| 4. Preview | `python -m http.server` | localhost:8000 |
| 5. Deploy | `git push` → GitHub Pages | live public URL |

---

## Tech stack

| Layer | Technology |
|-------|-----------|
| Language | Python 3.12 |
| Data | pandas, fastparquet |
| Visualisation | Plotly |
| Notebook | Jupyter |
| Rendering | Quarto |
| Styling | Bootstrap 5 (Cosmo theme), sidebar TOC |
| Dependency management | uv + uv.lock |
| Dev environment | Docker dev container (VS Code) |
| Hosting | GitHub Pages (`/docs` folder) |

---

## Reproducibility

Dependencies are managed with [uv](https://github.com/astral-sh/uv). The `uv.lock` file pins the full dependency tree so everyone gets the exact same environment.

To sync your environment manually:

```bash
uv sync --frozen
```

 
