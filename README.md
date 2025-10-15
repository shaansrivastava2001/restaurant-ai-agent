# Vector AI Agent

This repository contains a small Python project that builds a vector store and runs an LLM-based agent using local data.

Key files
- `app.py` — main application / runner
- `vector.py` — vector store creation and utilities
- `realistic_restaurant_reviews.csv` — dataset (tracked by default)
- `chroma_langchain_db/` — local Chroma vector DB (ignored by default)
- `requirements.txt` — Python dependencies

Quick start

1. Create and activate a virtual environment (recommended):

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python app.py
```

Notes

- The repository ignores the `chroma_langchain_db/` directory and `chroma.sqlite3` by default because the Chroma store contains large binary files specific to your environment. If you want to track a snapshot of the DB, remove those lines from `.gitignore`.

- `realistic_restaurant_reviews.csv` is present in the repo root. If you prefer to keep datasets out of version control, move it to a `data/` directory and add it to `.gitignore`.

Development tips

- Use `pip install -e .` or add a `pyproject.toml` / `setup.cfg` if you convert this into an installable package.
- Consider adding `pre-commit` hooks to block secrets and large files.

License

Add a LICENSE file if you plan to open-source the code.
