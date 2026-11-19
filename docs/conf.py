"""Sphinx configuration for the handcalcs-migrate documentation."""

import os
import pathlib
import re

REPO_ROOT = pathlib.Path(__file__).parent.parent
REPO_URL = "https://github.com/connorferster/handcalcs-migrate"

# Read the version from the source rather than importing the package, so the
# docs build needs only the 'doc' dependency group.
_init = (REPO_ROOT / "src" / "handcalcs_migrate" / "__init__.py").read_text()
release = re.search(r'^__version__ = "(.+)"', _init, re.M).group(1)
version = release

project = "handcalcs-migrate"
author = "Connor Ferster"
copyright = "2026, Connor Ferster"

extensions = [
    "myst_parser",
    "sphinx_copybutton",
]

source_suffix = {".md": "markdown"}
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

myst_enable_extensions = ["colon_fence", "deflist"]
myst_heading_anchors = 3

html_theme = "shibuya"
html_title = "handcalcs-migrate"
html_baseurl = os.environ.get(
    "DOCS_URL", "https://handcalcs-migrate.structuralpython.com/"
)

html_context = {
    "source_type": "github",
    "source_user": "connorferster",
    "source_repo": "handcalcs-migrate",
    "source_version": "main",
    "source_docs_path": "/docs/",
}

html_theme_options = {
    "accent_color": "teal",
    "github_url": REPO_URL,
    "nav_links": [
        {"title": "Convert", "url": "converting"},
        {"title": "What changes", "url": "conversions"},
        {"title": "Options", "url": "options"},
        {
            "title": "handcalcs",
            "url": "https://handcalcs.structuralpython.com/",
            "external": True,
        },
    ],
    "globaltoc_expand_depth": 1,
}

copybutton_prompt_text = r"\$ "
copybutton_prompt_is_regexp = True
