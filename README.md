# pycon-sdg-eda

> **Python for Good: Revealing the Philippines Through Data**
> An SDG exploratory data analysis notebook rendered as an interactive HTML report and deployed via GitHub Pages.

**Live example deployment:**  
https://ogbinar.com/py-sdg-eda-workshop/

---

## Overview

This project pulls SDG indicator data, analyzes it in a Jupyter notebook, and publishes it as a clean interactive HTML report using Quarto. The full workflow runs inside a dev container so anyone can reproduce it without manual environment setup.

---

## Prerequisites

- [Docker](https://www.docker.com/products/docker-desktop)
- [VS Code](https://code.visualstudio.com/) with the [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)

That's it. Python, Quarto, and all dependencies are handled inside the container.

---

## Getting Started

### 1. Open in Dev Container

Clone the repo and open it in VS Code:

```bash
git clone <your-repo-url>
cd pycon-sdg-eda
code .
```

When VS Code opens, click **"Reopen in Container"** in the bottom-right popup — or use the Command Palette:

```
Ctrl+Shift+P → Dev Containers: Open Folder in Container
```

VS Code will build the Docker image and install all dependencies automatically. This takes a few minutes on first run.

Verify the environment is ready:

```bash
python --version    # 3.12
quarto --version    # 1.9.35
uv pip list         # your project deps
```

---

## Workflow

### 2. Run the Data Pipeline

Pulls and processes SDG indicator data:

```bash
python run_pipeline.py
```

This produces the source data consumed by the notebook.

---

### 3. Inspect the Notebook (optional)

Open the notebook in VS Code or Jupyter to review or edit analysis:

```bash
jupyter notebook sdg-eda-notebook-final.ipynb
```

---

### 4. Render the HTML Report

Quarto executes the notebook and outputs a self-contained HTML report to `docs/index.html`:

```bash
quarto render sdg-eda-notebook-final.ipynb
```

Output is controlled by `_quarto.yml`:
- Theme: Bootstrap Cosmo
- Sidebar table of contents
- Code hidden by default
- Self-contained single HTML file

---

### 5. Preview Locally

Serve the output and open it in your browser:

```bash
python -m http.server --directory docs
```

Then visit: [http://localhost:8000](http://localhost:8000)

---

### 6. Deploy to GitHub Pages

Commit the `docs/` folder and push:

```bash
git add docs/
git commit -m "Update report"
git push
```

Then enable GitHub Pages in your repo:

```
Settings → Pages → Source: Deploy from branch → Branch: main → Folder: /docs
```

Your report will be live at:
```
https://<your-username>.github.io/<your-repo>/
```

---

## Project Structure

```
pycon-sdg-eda/
├── .devcontainer/
│   ├── Dockerfile            # Python 3.12 + Quarto + uv
│   └── devcontainer.json     # VS Code dev container config
├── docs/
│   └── index.html            # Generated report (committed to git)
├── _quarto.yml               # Quarto render config
├── run_pipeline.py           # Data extraction pipeline
├── sdg-eda-notebook-final.ipynb  # Main analysis notebook
├── pyproject.toml            # Python dependencies
└── uv.lock                   # Pinned dependency lock file
```

---

## Reproducibility

Dependencies are managed with [uv](https://github.com/astral-sh/uv). The `uv.lock` file pins the full dependency tree.

To sync your environment manually:

```bash
uv sync --frozen
```