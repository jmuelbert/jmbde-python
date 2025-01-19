#!/usr/bin/env python
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

from glob import glob
import os
import shutil
from subprocess import Popen

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
for f in glob(f"{resources_dir}/forms/*.ui"):
    print(
        "-g python",
        f"-o {source_dir}{package}/ui/ui_{os.path.basename(f[:-3])}.py {f}",
    )
    Popen(
        [
            "uic",
            "-g python",
            f"-o {source_dir}{package}/ui/ui_{os.path.basename(f[:-3])}.py {f}",
        ],
    )

print("Updating translations...")
Popen(["lupdate", "jmbde.pro"])
lang_files = " ".join(
    f"{resources_dir}/translations/{package}_{lang}.ts" for lang in languages
)
Popen(["pyside2-lupdate", f"{source_dir}{package}/*.py -ts {lang_files}"])
Popen(["lrelease", f"{resources_dir}/translations/*.ts"])

print("Rebuilding PyQt resource files in source directory...")
for f in glob(f"{source_dir}/*.qrc"):
    Popen(
        [
            "rcc",
            f" -g python -o {package}/resources/qrc_{os.path.basename(f[:-4])}.py {f}",
        ],
    )

print("Rebuilding PyQt resource files in resources_dir directory...")
for f in glob(f"{resources_dir}/*.qrc"):
    Popen(
        [
            "rcc",
            f" -g python --verbose -o {source_dir}{package}/qrc_{os.path.basename(f[:-4])}.py {f}",
        ],
    )

print("Regenerating .pyc files...")
shutil.rmtree(f"{package}/__pycache__", ignore_errors=True)
for f in glob(f"{package}/*.pyc"):
    os.remove(f)
__import__(f"{package}.__main__")
