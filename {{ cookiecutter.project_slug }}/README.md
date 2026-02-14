# {{ cookiecutter.project_name }}

{{ cookiecutter.description }}

## Requirements

- Python {{ cookiecutter.python_version }}+
- [UV](https://docs.astral.sh/uv/) (recommended)

## Quick start

```bash
uv sync
cp .env.example .env
uv run {{ cookiecutter.package_name }} --help
uv run pytest
```

## Project structure

```
{{ cookiecutter.project_slug }}/
├── .env.example
├── .gitignore
├── .pre-commit-config.yaml
├── .secrets.baseline
├── .github/
│   └── workflows/
│       └── ci.yml
├── README.md
├── LICENSE               # when license=MIT
├── main.py
├── pyproject.toml
├── src/
│   └── {{ cookiecutter.package_name }}/
│       ├── __init__.py
│       ├── cli.py
│       └── settings.py
└── tests/
    ├── __init__.py
    └── test_{{ cookiecutter.package_name }}.py
```

## Development commands

| Command | Description |
|--------|-------------|
| `uv sync --all-extras --dev` | Install runtime and dev dependencies |
| `uv run ruff check .` | Lint |
| `uv run mypy src` | Type-check |
| `uv run pytest -q` | Run tests |
| `uv run pre-commit run --all-files` | Run all pre-commit hooks |

## Settings

The default configuration lives in `src/{{ cookiecutter.package_name }}/settings.py` and is loaded from `.env`.

1. Copy `.env.example` to `.env`.
2. Adjust values for your environment.

## CI

A starter GitHub Actions workflow is included at `.github/workflows/ci.yml`.
It runs lint, type-checking, and tests on Linux, macOS, and Windows on push/PR.

## License
{% if cookiecutter.license == "MIT" %}
MIT (see `LICENSE`).
{% else %}
No license file is included by default.
{% endif %}
