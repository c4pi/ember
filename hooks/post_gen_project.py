from pathlib import Path


def main() -> None:
    if "{{ cookiecutter.license }}" == "MIT":
        return

    license_path = Path("LICENSE")
    if license_path.exists():
        license_path.unlink()


if __name__ == "__main__":
    main()
