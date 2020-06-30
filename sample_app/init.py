#!/usr/bin/env python
import os
import sys
from sample_app import sample_data

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sample_project.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError("Couldn't import Django.") from exc

    execute_from_command_line(["manage.py", "makemigrations"])
    execute_from_command_line(["manage.py", "migrate"])
    sample_data.generate()

if __name__ == '__main__':
    main()
