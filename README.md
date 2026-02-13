# Ember Cookiecutter Template

Ember is a Cookiecutter template for modern Python 3.14 projects. The actual
Cookiecutter payload lives under `{{ cookiecutter.project_slug }}/`, matching the
structure shown inside that folder’s README.

## Quick start

```bash
cd ~/dev/ember
cookiecutter . --output-dir=../
```

Cookiecutter will ask for fields like `project_name`, `project_slug`, and
`package_name`. You can pass them non-interactively as well:

```bash
cookiecutter . \
  --output-dir=../ \
  --no-input \
  project_name=STTC \
  project_slug=sttc \
  package_name=sttc
```

This command produced the `~/dev/sttc` example project currently checked in on
my machine.

## Template contents

The template files live in `{{ cookiecutter.project_slug }}/` and already use
Cookiecutter variables everywhere (README, pyproject, main.py, src/tests, etc.).
When you render, Cookiecutter copies that directory, substituting the values you
provided for the placeholders.

## Rendering tips

- Use `--overwrite-if-exists` if you’re re-generating into an existing folder.
- The generated project inherits the README from `{{ cookiecutter.project_slug }}/`,
  so end users still get full documentation in their scaffolded repo.
- After rendering, run `uv sync`, `uv run pytest`, and `uv run pre-commit run --all-files`
  inside the new project to bootstrap dependencies and verify the hooks.

Happy scaffolding!
