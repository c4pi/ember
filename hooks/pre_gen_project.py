import os
import json
from pathlib import Path

def main():
    context_json = os.environ.get('COOKIECUTTER_CONTEXT')
    if context_json:
        context = json.loads(context_json)
        add_keywords = context.get('cookiecutter', {}).get('add_keywords', 'no')
        if add_keywords == 'yes':
            keywords = input('Enter project keywords (comma-separated): ')
            Path('project_keywords.txt').write_text(keywords)

if __name__ == '__main__':
    main()
