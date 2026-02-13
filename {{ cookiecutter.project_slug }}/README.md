# {{ cookiecutter.project_name }}

Python project template: UV/venv friendly, Pydantic BaseSettings, pre-commit (Ruff, mypy, detect-secrets, etc.), package stub, and tests. Cookiecutter template.

## Requirements

- Python {{ cookiecutter.python_version }}+
- [UV](https://docs.astral.sh/uv/) (recommended) or standard venv

## Quick start

```bash
# Clone or create repo, then from project root:
uv sync
cp .env.example .env
uv run python main.py
uv run pytest
```

## Using Ember as a Cookiecutter template

1. Clone this repository somewhere on your machine (e.g., `~/dev/ember`).
2. Run Cookiecutter against the template root (this directory) and choose your
   project metadata. You can let Cookiecutter ask you interactively or pass
   the values on the command line.

Example (rendering the **STTC** project we generated earlier):

```bash
cd ~/dev/ember
cookiecutter . \
  --output-dir=../ \
  --no-input \
  project_name=STTC \
  project_slug=sttc \
  package_name=sttc
```

The scaffold is created at `../sttc`, ready for `uv sync`, git init, etc. Use
`--overwrite-if-exists` if you are re-rendering into an existing folder.

## Structure

```
{{ cookiecutter.project_slug }}/
├── .env.example
├── .gitignore
├── .pre-commit-config.yaml
├── .secrets.baseline
├── README.md
├── main.py
├── pyproject.toml
├── src/
│   └── {{ cookiecutter.package_name }}/
│       ├── __init__.py
│       └── settings.py
└── tests/
    ├── __init__.py
    └── test_{{ cookiecutter.package_name }}.py
```

## Settings

- **settings.py** uses Pydantic `BaseSettings`; config is loaded from `.env`.
- Copy `.env.example` to `.env` and adjust. Do not commit `.env`.

## Pre-commit

Install hooks:

```bash
uv run pre-commit install
uv run pre-commit run --all-files
```

Hooks: Ruff, mypy, detect-secrets, check-added-large-files, check-merge-conflict, check-toml, check-yaml, end-of-file-fixer, trailing-whitespace, debug-statements.

## Documentation references

Project conventions follow these docs (in the parent `dev/` directory):

- **pyproject.toml-ruff-defaults.txt** — Ruff config baseline (target-version, lint rules, format).
- **python-code-style.mdc** — Code style: no docstrings, pathlib only, compact formatting.
- **python-error-and-logging.mdc** — Error handling and logging (f-strings, minimal try/except).

Paths from this repo: `../pyproject.toml-ruff-defaults.txt`, `../python-code-style.mdc`, `../python-error-and-logging.mdc`.

## Commands

| Command | Description |
|--------|-------------|
| `uv sync` | Install dependencies (and dev deps) |
| `uv run python main.py` | Run entrypoint |
| `uv run pytest` | Run tests |
| `uv run pre-commit run --all-files` | Run all pre-commit hooks |
| `uv run mypy src` | Type-check |
| `uv run ruff check .` | Lint |

## License

MIT (or your choice).
