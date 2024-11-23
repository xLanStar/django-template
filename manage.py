#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""

import os
import sys


class DjangoImportError(ImportError):
    """Exception raised when Django is not installed."""

    def __init__(
        self,
        message: str = "Couldn't import Django. Ensure it's installed and available on your PYTHONPATH. Did you forget to activate a virtual environment?",
    ) -> None:
        """Initialize the exception."""
        super().__init__(message)


def main() -> None:
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise DjangoImportError from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
