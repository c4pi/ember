#!/usr/bin/env python3
"""Entrypoint for local runs: `uv run python main.py`."""

from {{ cookiecutter.package_name }}.cli import main

if __name__ == "__main__":
    main()
