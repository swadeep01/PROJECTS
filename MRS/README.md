# Movie Recommendation Script (mrs.py)

This repository contains a simple content-based movie recommendation script `mrs.py` that uses TF-IDF on movie overviews and cosine similarity to recommend similar films.

Getting started

1. Install Python 3.8+ and create a virtual environment (recommended):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. Download the dataset:

Place `tmdb_5000_movies.csv` next to `mrs.py` (same directory). You can find the dataset from the original source or elsewhere — the script expects a CSV with `title` and `overview` columns.

4. Run the script:

```powershell
python mrs.py
```

What I added

- `requirements.txt` — minimal dependencies the script uses.
- `README.md` — quick usage instructions and dataset note.

Notes about committing & pushing

- I can initialize a Git repo and push to `https://github.com/swadeep01/PROJECTS.git`, but pushing requires `git` to be installed locally and authentication to GitHub (PAT or `gh auth login`). If you want, install Git and re-run the push, or I can walk you through generating a PAT or using SSH.
