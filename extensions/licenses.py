"""Inject all licenses found on https://choosealicense.com into the Jinja2 context."""

from copier_templates_extensions import ContextHook
from github import Github


class LicenseChoiceUpdater(ContextHook):
    """Inject licenses found on https://choosealicense.com into the Jinja2 context."""

    def hook(self, context: dict) -> dict:
        """Update the context with licenses found on https://choosealicense.com."""
        g = Github()
        licenses = g.get_repo("github/choosealicense.com").get_dir_contents("licenses")
        context["licenses"] = [license.name for license in licenses]
        return context
