"""Add filter to split variables into a list."""

from jinja2.ext import Extension


def split_filter(value: str, separator: str) -> list[str]:
    """Split a string into a list of strings."""
    return [item.strip() for item in value.split(separator)]


class SplitFilterExtension(Extension):
    """Split variables into a list."""

    def __init__(self, environment):
        super().__init__(environment)
        environment.filters["split"] = split_filter
