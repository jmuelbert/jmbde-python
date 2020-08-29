#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#   jmbde a BDE Tool for datacontext
#   Copyright (C) 2018-2020  Jürgen Mülbert
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
"""The qt ui builder."""
import os
import shutil
import subprocess
from glob import glob

package = "jmbde"
resources_dir = "resources"
source_dir = "src/"
languages = [
    "ar_DZ",
    "bg",
    "ca_ES",
    "cs",
    "de",
    "en",
    "en_US",
    "es",
    "fr",
    "he",
    "hu",
    "it",
    "ja",
    "js",
    "nb",
    "nl",
    "pl",
    "pt",
    "pt_PT",
    "ru",
    "tr",
    "uk",
    "zh_CN",
    "zh_TW",
]

print("Rebuilding PyQt UI files...")
for f in glob("{}/forms/*.ui".format(resources_dir)):
    print(
        "-g python",
        "-o {}{}/ui/ui_{}.py {}".format(
            source_dir, package, os.path.basename(f[:-3]), f
        ),
    )
    subprocess.call(
        [
            "uic",
            "-g python",
            "-o {}{}/ui/ui_{}.py {}".format(
                source_dir, package, os.path.basename(f[:-3]), f
            ),
        ]
    )

print("Updating translations...")
subprocess.run(["lupdate", "jmbde.pro"])
lang_files = " ".join(
    "{}/translations/{}_{}.ts".format(resources_dir, package, lang)
    for lang in languages
)
subprocess.run(
    ["pyside2-lupdate", "{}{}/*.py -ts {}".format(source_dir, package, lang_files)]
)
subprocess.run(["lrelease", "{}/translations/*.ts".format(resources_dir)])

print("Rebuilding PyQt resource files in source directory...")
for f in glob("{}/*.qrc".format(source_dir)):
    subprocess.run(
        [
            "rcc",
            " -g python -o {}/resources/qrc_{}.py {}".format(
                package, os.path.basename(f[:-4]), f
            ),
        ],
    )

print("Rebuilding PyQt resource files in resources_dir directory...")
for f in glob("{}/*.qrc".format(resources_dir)):
    subprocess.run(
        [
            "rcc",
            " -g python --verbose -o {}{}/qrc_{}.py {}".format(
                source_dir, package, os.path.basename(f[:-4]), f
            ),
        ],
    )

print("Regenerating .pyc files...")
shutil.rmtree("{}/__pycache__".format(package), ignore_errors=True)
for f in glob("{}/*.pyc".format(package)):
    os.remove(f)
__import__("{}.__main__".format(package))
