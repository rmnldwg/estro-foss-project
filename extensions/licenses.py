"""Extensions for dynamic license choices and full license info."""

import os

import requests
from jinja2.ext import Extension

GH_API_URL = "https://api.github.com/licenses"


def _assemble_headers() -> dict:
    """Assemble headers for GitHub's REST API."""
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }

    if "GITHUB_TOKEN" in os.environ:
        github_token = os.environ["GITHUB_TOKEN"]
        headers["Authorization"] = f"Bearer {github_token}"

    return headers


def fetch_common_licenses() -> list[dict]:
    """Fetch commonly used licenses from GitHub's REST API."""
    response = requests.get(
        url=GH_API_URL,
        headers=_assemble_headers(),
        timeout=10,
    )
    response.raise_for_status()
    return response.json()


def fetch_full_license(key: str) -> dict:
    """Fetch full license info from GitHub's REST API."""
    response = requests.get(
        url=f"{GH_API_URL}/{key}",
        headers=_assemble_headers(),
        timeout=10,
    )
    response.raise_for_status()
    return response.json()


class LicenseChoiceExtension(Extension):
    """Jinja2 extension to provide license choices."""

    def __init__(self, environment):
        super().__init__(environment)
        environment.globals["common_licenses"] = fetch_common_licenses()
        environment.globals["fetch_full_license"] = fetch_full_license
