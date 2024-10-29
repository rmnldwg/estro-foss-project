"""Add context hook to split authors into a list."""

from copier_templates_extensions import ContextHook


class SplitAuthorsUpdater(ContextHook):
    """Split authors into a list."""

    def hook(self, context):
        """Split authors into a list."""
        authors = context["authors"]
        return {
            "authors": [author.strip() for author in authors.split(",")],
            "test": "ladida",
        }
