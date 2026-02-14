# Ember Cookiecutter Template

Cookiecutter template for modern Python projects with UV, Ruff, mypy, pytest, pre-commit, and typed settings.

## Important

Use Cookiecutter to render this template.
Do not use GitHub's "Use this template" button if you expect variable substitution.

## Quick start

```bash
uvx cookiecutter gh:c4pi/ember
```

Or render from a local clone:

```bash
git clone git@github.com:c4pi/ember.git
cd ember
uvx cookiecutter . --output-dir ../
```

You can also render non-interactively:

```bash
uvx cookiecutter gh:c4pi/ember \
  --no-input \
  project_name="My Service" \
  project_slug=my_service \
  package_name=my_service
```

## What gets generated

The template payload lives in `{{ cookiecutter.project_slug }}/` and renders a project with:

- `src/` package layout
- `pyproject.toml` (Hatchling build, Ruff, mypy, pytest config)
- `tests/` starter tests
- `.pre-commit-config.yaml` and `.secrets.baseline`
- `.github/workflows/ci.yml` starter CI workflow
- `.env.example` + Pydantic settings scaffold

## Local validation

Template quality can be checked with:

```bash
uvx cookiecutter . --no-input --output-dir /tmp/ember-render
python3 -m compileall /tmp/ember-render/my_project/main.py /tmp/ember-render/my_project/src /tmp/ember-render/my_project/tests
```
