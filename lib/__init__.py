"""Shared helpers for the Facebook Pages Skills bundle.

MCP calls are made by the agent host, not by this Python package. The package
only contains deterministic helpers that are useful to runtimes that load the
skills as Markdown.
"""
from .url_parser import parse_facebook_url
from .approval import render_approval_card
from .apify_client import ApifyClient, ApifyError, ApifyAuthError

__all__ = [
    "parse_facebook_url",
    "render_approval_card",
    "ApifyClient",
    "ApifyError",
    "ApifyAuthError",
]
