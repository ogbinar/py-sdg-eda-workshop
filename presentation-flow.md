# Workshop Facilitation Guide

> **Python for Good: Revealing the Philippines Through Data**

This guide is for the facilitator. It covers pacing, what to emphasize, and where things tend to go wrong.

---

## Before the Session

Send participants a message at least one day before asking them to install:

- [Docker Desktop](https://www.docker.com/products/docker-desktop)
- [VS Code](https://code.visualstudio.com/) with the [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)

This removes the biggest time sink on the day. People who show up without Docker will delay the whole room.

Also prepare a fallback pairing plan — for every 10 participants, expect 1–2 who cannot get Docker running on the day. Pair them with a neighbor rather than spending 10 minutes debugging one machine.

---

## Session Overview

| Time | Block | Duration |
|------|-------|----------|
| 0:00 – 0:15 | Setup — dev container | 15 min |
| 0:15 – 0:30 | Data pipeline | 15 min |
| 0:30 – 1:00 | Notebook walkthrough | 30 min |
| 1:00 – 1:20 | Render the report | 20 min |
| 1:20 – 1:40 | Deploy to GitHub Pages | 20 min |
| 1:40 – 2:00 | Open exploration + Q&A | 20 min |

---

## Block by Block

### 0:00 – 0:15 | Setup (15 min)

Get everyone into the dev container. This is the highest-risk part of the session — do it first while participants are still fresh and patient.

**What to do:**

```bash
git clone https://github.com/ogbinar/py-sdg-eda-workshop.git
cd py-sdg-eda-workshop
code .
```

Then: **Reopen in Container** from the VS Code popup or Command Palette.

**What to say:**
> "This will take a few minutes on first run — Docker is building a Python environment with everything pre-installed. You will never need to run `pip install` for this project."

**Verify everyone is in:**

```bash
python --version    # 3.12
quarto --version    # 1.9.35
uv pip list
```

**Watch out for:**
- Docker Desktop not running — ask them to start it and try again
- Dev Containers extension not installed — takes 1 minute to fix
- Windows users on Home edition — Docker requires WSL2, may need extra setup
- Anyone blocked: pair them with a neighbor and move on

---

### 0:15 – 0:30 | Data Pipeline (15 min)

Run the pipeline together and use it to orient participants to the dataset.

```bash
python run_pipeline.py
```

While it runs, open `src/config.py` and walk through it:

- **`COUNTRIES`** — the 10 countries being compared and why they were chosen (ASEAN peers, large emerging economies, advanced economies)
- **`INDICATORS`** — the SDG metrics being tracked (education, internet access, GDP, poverty, life expectancy, etc.)
- **`CORE_INDICATORS` vs `CONTEXT_INDICATORS`** — explain the distinction briefly

**What to say:**
> "The pipeline pulls this data from the World Bank API and saves it locally. We only need to run this once. From here on, everything works offline."

**Key point to land:**
The country and indicator choices are deliberate — the Philippines is being compared to countries at different development stages, not just wealthy nations. That framing matters for how participants will read the charts.

---

### 0:30 – 1:00 | Notebook Walkthrough (30 min)

This is the core of the workshop. Walk through `sdg-eda-notebook-final.ipynb` cell by cell — but do not read every line of code. Focus on what the data is showing.

**Structure your walkthrough in three parts:**

**Part 1 — What the raw data looks like (5 min)**

Show the parquet file loading and the initial DataFrame. Point out missing values — some indicators like `gini_index` and `hospital_beds` have significant gaps. Ask:
> "Why might some countries have more missing data than others?"

This builds data literacy before the charts appear.

**Part 2 — The charts (20 min)**

Spend most of your time here. For each chart, do three things:

1. Read the chart out loud — what is being shown, what the axes mean
2. Ask the room what they notice before explaining anything
3. Anchor on the Philippines line specifically

**Moments where the data tends to surprise people:**

- **Internet access** — the Philippines lags behind Vietnam despite similar GDP per capita. Ask why.
- **Life expectancy vs GDP** — some countries punch above their weight. The Philippines is not always one of them.
- **Education expenditure vs outcomes** — spending more does not always produce better secondary completion rates.
- **CO₂ per capita** — advanced economies look very different here. Opens a conversation about development vs sustainability tradeoffs.

Let the room react. These moments of surprise are the emotional core of the workshop — do not rush past them chasing the schedule.

**Part 3 — Plotly interactivity (5 min)**

Show participants how to use the charts:
- Hover for exact values
- Click legend items to hide/show countries
- Box select or lasso to zoom
- Double-click to reset

Many participants will not know these controls exist.

**What to say:**
> "This is not about politics. Every number here comes from the World Bank's open dataset. The question we are asking is: what can the Philippines learn from countries that are moving faster on these indicators?"

---

### 1:00 – 1:20 | Render the Report (20 min)

Convert the notebook into a publishable HTML report.

```bash
quarto render 
```

**Warn people before they run it:**
> "This will take 2–3 minutes because Quarto is re-executing the entire notebook. It is not frozen — just wait."

While it renders, open `_quarto.yml` and explain each setting:

```yaml
theme: cosmo          # Bootstrap theme — can be changed to flatly, lux, etc.
toc: true             # generates the sidebar table of contents
toc-location: left    # sidebar on the left
code-fold: true       # hides code but makes it expandable
self-contained: true  # everything in one HTML file, no external dependencies
echo: false           # code cells hidden by default in output
```

When it finishes, preview it:

```bash
python -m http.server --directory docs
```

Open [http://localhost:8000](http://localhost:8000) and show the difference between the raw notebook and the report:

- No code visible
- Clean sidebar navigation
- Interactive Plotly charts preserved
- Looks like a proper data report, not a notebook

**What to say:**
> "This is the same analysis you just ran — but now it looks like something you could send to a policymaker or publish on a website. The content is identical. Only the presentation changed."

---

### 1:20 – 1:40 | Deploy to GitHub Pages (20 min)

Get everyone's report live on the internet.

**Prerequisites:**
- Participants need a GitHub account
- They need to have forked the repo (or initialized their own)

**Steps to walk through together:**

```bash
git add docs/
git commit -m "Add rendered report"
git push
```

Then in the GitHub repo settings:

```
Settings → Pages → Source: Deploy from branch
Branch: main → Folder: /docs → Save
```

GitHub Pages takes about 1–2 minutes to go live. While waiting:

> "While GitHub builds your site, talk to the person next to you — what was the most surprising thing you saw in the data?"

When sites start appearing, ask a few participants to share their URL with the room. This is a high-energy moment — something real and shareable now exists that did not exist 2 hours ago.

---

### 1:40 – 2:00 | Open Exploration + Q&A (20 min)

Give participants unstructured time. Suggest a few directions for those who want to go deeper:

**Easy:**
- Change the Quarto theme in `_quarto.yml` (try `flatly`, `lux`, `darkly`) and re-render
- Hover through the charts and find one surprising data point to share

**Medium:**
- Add a new country to `COUNTRIES` in `src/config.py`, re-run the pipeline, re-render
- Change `SNAPSHOT_YEAR` and see how the charts shift

**Harder:**
- Add a new indicator from the World Bank API to `INDICATORS`
- Write a new markdown cell in the notebook with your own interpretation of a chart

Use this time to circulate, answer questions, and help anyone who fell behind catch up on the deploy step.

---

## Common Issues

| Problem | Fix |
|---------|-----|
| Docker not running | Start Docker Desktop, wait for it to initialize, then retry |
| Dev Containers extension missing | Install from VS Code Extensions (`Ctrl+Shift+X`), search "Dev Containers" |
| `quarto render` hangs | Check terminal for errors — usually a missing kernel or broken cell |
| GitHub push blocked | Set up a Personal Access Token: GitHub → Settings → Developer Settings → Tokens |
| Port 8000 already in use | `python -m http.server 8080 --directory docs` |
| Windows Home / no WSL2 | Enable WSL2 via PowerShell: `wsl --install`, restart, retry Docker |

---

## Key Points to Land

These are the ideas worth pausing on — even if time is short:

1. **Reproducibility matters.** Anyone can clone this repo, run three commands, and get the exact same report. That is not common in development analysis.

2. **Open data is not neutral.** The World Bank dataset has gaps, lags, and methodological choices baked in. Point these out — it builds critical thinking.

3. **The Philippines is not just behind.** Find at least one indicator where the Philippines performs well relative to peers and call it out. The goal is honest analysis, not a deficit narrative.

4. **Publishing is part of the work.** A notebook that only runs on your laptop does not exist for anyone else. The GitHub Pages step is not a nice-to-have — it is how analysis becomes communication.