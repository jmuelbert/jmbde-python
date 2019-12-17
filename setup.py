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
"""Setup jmbde application"""
import codecs
import os

from setuptools import find_packages
from setuptools import setup

version = '0.2.0'
here = os.path.abspath(os.path.dirname(__file__))


def read(*parts: str) -> str:
    # intentionally *not* adding an encoding option to open, See:
    #   https://github.com/pypa/virtualenv/issues/201#issuecomment-3145690
    with codecs.open(os.path.join(here, *parts), 'r') as fp:
        return fp.read()


long_description = read('README.rst')

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


def parse_requirements(requirements: str):
    """ load requirements from a pip requirements file """
    # load from requirements.txt
    with open(os.path.join(here, requirements), "r") as f:
        lines = [l for l in f]
        # remove spaces
        stripped = map((lambda x: x.strip()), lines)
        # remove comments
        nocomments = filter((lambda x: not x.startswith("#")), stripped)
        # remove empty lines
        reqs = filter((lambda x: x), nocomments)
        return reqs


REQUIREMENTS = parse_requirements(os.path.join(here, "requirements.txt"))
TESTS_REQUIRES = parse_requirements(os.path.join(here, "requirements_dev.txt"))

setup(
    name="jmbde",
    version=version,
    description="A generator to generate infos for the affected persons.",
    long_description=long_description,

    license='EUPL-1.2',
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: European Union Public Licence 1.2 " +
        "(EUPL 1.2)",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Office/Business",
    ],
    url='https://github.com/jmuelbert/jmbde-python',
    download_url='https://github.com/jmuelbert/jmbde-python/archiv/' +
        version + ".zip",
    project_urls={
        'Source Code': 'https://github.com/jmuelbert/jmbde-python',
        'Bug Reports': 'https://github.com/jmuelbert/jmbde-python/issues',
        'Documentation': 'https://jmbde-python.readthedocs.io/en/latest/'
    },
    keywords='jmbde, bde, business tool, qt5, python',

    author='Jürgen Mülbert',
    author_email='juergen.muelbert@gmail.com',

    install_requirements=REQUIREMENTS,
    package_dir={'': 'src'},
    packages=find_packages(
        'src',
        exclude=["contrib", "docs", "tests*", "tasks"],
    ),
    entry_points={
        'console_scripts':
        ['jmbde=jmbde.cli:main'],
        "gui_scripts":
        ["jmbde=app.__main__:main"]
    },
    zip_safe=False,
    python_requires='>=3.5.*',
)
