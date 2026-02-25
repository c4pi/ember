import json
from pathlib import Path

KEYWORDS_PLACEHOLDER = "# __COOKIECUTTER_KEYWORDS__"
ADD_KEYWORDS = "{{ cookiecutter.add_keywords }}"
LICENSE_CHOICE = "{{ cookiecutter.license }}"


def format_keywords_line(raw_keywords: str) -> str:
    keywords = [keyword.strip() for keyword in raw_keywords.split(",") if keyword.strip()]
    if not keywords:
        return ""
    quoted_keywords = ", ".join(json.dumps(keyword) for keyword in keywords)
    return f"keywords = [{quoted_keywords}]"


def main() -> None:
    if LICENSE_CHOICE != "MIT":
        license_path = Path("LICENSE")
        if license_path.exists():
            license_path.unlink()

    if ADD_KEYWORDS != "yes":
        return

    pyproject_path = Path("pyproject.toml")
    pyproject_content = pyproject_path.read_text()
    if KEYWORDS_PLACEHOLDER not in pyproject_content:
        return

    try:
        raw_keywords = input("Enter project keywords (comma-separated, optional): ").strip()
    except EOFError:
        raw_keywords = ""

    keywords_line = format_keywords_line(raw_keywords)
    pyproject_content = pyproject_content.replace(KEYWORDS_PLACEHOLDER, keywords_line)
    pyproject_path.write_text(pyproject_content)


if __name__ == "__main__":
    main()
