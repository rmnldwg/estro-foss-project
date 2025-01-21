"""Slugify a project name to be a valid Python package name."""

from jinja2.ext import Extension
from slugify import slugify


def python_compatible_slug(text: str) -> str:
    """Slugify a string to be a valid Python package name."""
    return slugify(
        text=text,
        separator="_",
    )


class SlugifyFilterExtension(Extension):
    """Slugify a project name to be a valid Python package name."""

    def __init__(self, environment):
        super().__init__(environment)
        environment.filters["slugify"] = python_compatible_slug
