# SPDX-FileCopyRightText: 2023 Jürgen Mülbert <juergen.muelbert@web.de>
#
# SPDX-License-Identifier: EUPL-1.2

"""Sphinx configuration."""
from datetime import datetime

PROJECT = "jmbde-python"
AUTHOR = "Jürgen Mülbert"
COPYRIGHT = f"{datetime.now().year}, {AUTHOR}"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
language = "en"
html_theme = "furo"
autodoc_typehints = "description"
myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "substitution",
]
