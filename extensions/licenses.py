"""Extensions for dynamic license choices and full license info."""

import os
from typing import Literal

import requests
from jinja2.ext import Extension

GH_API_URL = "https://api.github.com/licenses"
CC_URL = "https://creativecommons.org/licenses"


def _create_github_headers() -> dict:
    """Assemble headers for GitHub's REST API."""
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }

    if "GITHUB_TOKEN" in os.environ:
        github_token = os.environ["GITHUB_TOKEN"]
        headers["Authorization"] = f"Bearer {github_token}"

    return headers


def fetch_common_software_licenses() -> list[dict]:
    """Fetch commonly used licenses from GitHub's REST API."""
    response = requests.get(
        url=GH_API_URL,
        headers=_create_github_headers(),
        timeout=10,
    )
    response.raise_for_status()
    return response.json()


def get_creative_commons_licenses() -> list[dict]:
    """Get Creative Commons licenses."""
    return [
        {"key": "cc-by", "name": "CC BY",},
        {"key": "cc-by-sa", "name": "CC BY-SA",},
        {"key": "cc-by-nd", "name": "CC BY-ND",},
        {"key": "cc-by-nc", "name": "CC BY-NC",},
        {"key": "cc-by-nc-sa", "name": "CC BY-NC-SA",},
        {"key": "cc-by-nc-nd", "name": "CC BY-NC-ND",},
    ]


def fetch_license_options(usage: Literal["software", "dataset"]) -> list[dict]:
    """Fetch commonly used licenses from GitHub's REST API or list CC licenses."""
    if usage == "software":
        return fetch_common_software_licenses()

    if usage == "dataset":
        return get_creative_commons_licenses()

    raise ValueError(f"Invalid usage: {usage}")


def is_cc_license(key: str) -> bool:
    """Check if a license is a Creative Commons license."""
    return key.startswith("cc-")


def fetch_license_body(key: str) -> dict:
    """Fetch full license info from GitHub's REST API or Creative Commons."""
    if not is_cc_license(key):
        response = requests.get(
            url=f"{GH_API_URL}/{key}",
            headers=_create_github_headers(),
            timeout=10,
        )
        response.raise_for_status()
        return response.json()["body"]

    short_key = key.replace("cc-", "")
    response = requests.get(
        url=f"{CC_URL}/{short_key}/4.0/legalcode.txt",
        timeout=10,
    )
    response.raise_for_status()
    return response.text


class LicenseChoiceExtension(Extension):
    """Jinja2 extension to provide license choices."""

    def __init__(self, environment):
        super().__init__(environment)
        environment.globals["fetch_license_options"] = fetch_license_options
        environment.globals["fetch_license_body"] = fetch_license_body
