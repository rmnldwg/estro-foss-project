"""Allows the user to get the current year in Jinja2."""

from datetime import datetime

from jinja2.ext import Extension


def get_current_year() -> int:
    """Get the current year."""
    return datetime.now().year


class YearExtension(Extension):
    """Jinja2 extension to provide the current year."""

    def __init__(self, environment):
        super().__init__(environment)
        environment.globals["current_year"] = get_current_year()
