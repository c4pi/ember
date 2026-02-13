#!/usr/bin/env python3
"""Entrypoint: UV/venv friendly. Run with `uv run python main.py` or `python main.py`."""

from {{ cookiecutter.package_name }}.settings import get_settings


def main() -> None:
    settings = get_settings()
    print(f"app_env={settings.app_env} debug={settings.debug} log_level={settings.log_level}")


if __name__ == "__main__":
    main()
