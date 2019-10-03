#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Copyright (c) 2019 Jürgen Mülbert. All rights reserved.
#
# Licensed under the EUPL, Version 1.2 or – as soon they
# will be approved by the European Commission - subsequent
# versions of the EUPL (the "Licence");
# You may not use this work except in compliance with the
# Licence.
# You may obtain a copy of the Licence at:
#
# https://joinup.ec.europa.eu/page/eupl-text-11-12
#
# Unless required by applicable law or agreed to in
# writing, software distributed under the Licence is
# distributed on an "AS IS" basis,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
# express or implied.
# See the Licence for the specific language governing
# permissions and limitations under the Licence.
#
# Lizenziert unter der EUPL, Version 1.2 oder - sobald
#  diese von der Europäischen Kommission genehmigt wurden -
# Folgeversionen der EUPL ("Lizenz");
# Sie dürfen dieses Werk ausschließlich gemäß
# dieser Lizenz nutzen.
# Eine Kopie der Lizenz finden Sie hier:
#
# https://joinup.ec.europa.eu/page/eupl-text-11-12
#
# Sofern nicht durch anwendbare Rechtsvorschriften
# gefordert oder in schriftlicher Form vereinbart, wird
# die unter der Lizenz verbreitete Software "so wie sie
# ist", OHNE JEGLICHE GEWÄHRLEISTUNG ODER BEDINGUNGEN -
# ausdrücklich oder stillschweigend - verbreitet.
# Die sprachspezifischen Genehmigungen und Beschränkungen
# unter der Lizenz sind dem Lizenztext zu entnehmen.
#

"""Setuop jmbde application"""

import os
import io
from datetime import datetime as dt
from pathlib import Path  # noqa E402
import versioneer
from setuptools import setup


CURRENT_DIR = Path(__file__).parent
cmdclass = {}

# Allow compilation of Qt .qrc, .ui and .ts files (build_qt command)
try:
    from setup_qt import build_qt

    cmdclass["build_qt"] = build_qt
except ImportError:
    pass


def get_long_description() -> str:
    """Get the text of the README.rst."""
    readme_rst = os.path.join(CURRENT_DIR, "README.rst")

    with io.open(readme_rst, "rt", encoding="utf8") as f:
        readme = f.read()
        return readme


MIN_PY_VERSION = "3.6"
PROJECT_NAME = "JM OpenOrders"
PROJECT_DESCRIPTION = "jmbde is a generator to generate infos for the affected persons"
PROJECT_PACKAGE_NAME = "jmbde"
PROJECT_LICENSE = "EUPL-1.2 "
PROJECT_AUTHOR = "Jürgen Mülbert"
PROJECT_COPYRIGHT = " 2018-{}, {}".format(dt.now().year, PROJECT_AUTHOR)
PROJECT_URL = "https://jmbde.github.io/"
PROJECT_EMAIL = "juergen.muelbert@gmail.com"

PROJECT_GITHUB_USERNAME = "jmuelbert"
PROJECT_GITHUB_REPOSITORY = "jmbde"

PYPI_URL = "https://pypi.python.org/pypi/{}".format(PROJECT_PACKAGE_NAME)
GITHUB_PATH = "{}/{}".format(PROJECT_GITHUB_USERNAME, PROJECT_GITHUB_REPOSITORY)
GITHUB_URL = "https://github.com/{}".format(GITHUB_PATH)

DOWNLOAD_URL = "{}/archive/{}.zip".format(GITHUB_URL, versioneer.get_version())
PROJECT_URLS = {
    "Source Code": "{GITHUB_URL}",
    "Bug Reports": "{}/issues".format(GITHUB_URL),
    "Documentation": "https://readthedocs.org/projects/{}".format(PROJECT_PACKAGE_NAME),
}


PACKAGES = ["jmbde"]
PACKAGE_DATA = {"jmbde": ["forms/*.ui", "*.qrc", "languages/*.ts", "languages/*.qm"]}

OPTIONS = {
    "build_qt": {
        "packages": ["jmbde"],
        "languages": [
            "ar_DZ",
            "bg",
            "ca_ES",
            "cs",
            "de",
            "en_US",
            "en",
            "es_ES",
            "es",
            "fr_FR",
            "fr",
            "he",
            "hu",
            "it",
            "ja",
            "js",
            "nb",
            "nl",
            "pl",
            "pt_PT",
            "pt",
            "ru",
            "tr",
            "uk",
            "uh_TW",
        ],  # optional
        "languages_dir": "languages",  # optional ('languages' is default)
        "bindings": "PySide2",  # optional ('PyQt5' is default)
        "pyrcc": "pyside2-rcc",
        "pyuic": "pyside2-uic",
        "pylupdate": "pyside2-lupdate",
        # "replacement_bindings": "Qt",  # optional (for Qt.py wrapper usage)
    }
}


def parse_requirements(requirements):
    # load from requirements.txt
    with open(requirements) as f:
        lines = [l for l in f]
        # remove spaces
        stripped = map((lambda x: x.strip()), lines)
        # remove comments
        nocomments = filter((lambda x: not x.startswith("#")), stripped)
        # remove empty lines
        reqs = filter((lambda x: x), nocomments)
        return reqs


extras_require = {}

REQUIREMENTS = parse_requirements(os.path.join(CURRENT_DIR, "requirements.txt"))
TESTS_REQUIRES = parse_requirements(os.path.join(CURRENT_DIR, "requirements_dev.txt"))


CMDCLASS = versioneer.get_cmdclass()

setup(
    name=PROJECT_PACKAGE_NAME,
    description=PROJECT_DESCRIPTION,
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    url=PROJECT_URL,
    download_url=DOWNLOAD_URL,
    project_urls=PROJECT_URLS,
    author=PROJECT_AUTHOR,
    author_email=PROJECT_EMAIL,
    packages=PACKAGES,
    package_data=PACKAGE_DATA,
    include_package_data=True,
    zip_safe=False,
    install_requires=REQUIREMENTS,
    python_requires=">={}".format(MIN_PY_VERSION),
    test_suite="tests",
    tests_require=TESTS_REQUIRES,
    entry_points={"gui_scripts": ["jmbde=app.__main__:main"]},
    version=versioneer.get_version(),
    options=OPTIONS,
    cmdclass=CMDCLASS,
)
