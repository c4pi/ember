from {{ cookiecutter.package_name }} import __version__
from {{ cookiecutter.package_name }}.settings import Settings, get_settings


def test_version() -> None:
    assert __version__ == "{{ cookiecutter.version }}"


def test_settings_defaults() -> None:
    s = Settings()
    assert s.app_env == "development"
    assert s.debug is False
    assert s.log_level == "INFO"


def test_get_settings() -> None:
    s = get_settings()
    assert isinstance(s, Settings)
