#!/usr/bin/python3
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
"""The Application class identifier."""
import os

"""The configs."""

BASE_DIR = os.path.join(os.path.dirname(__file__), "..")
IMAGES_DIR = os.path.join(BASE_DIR, "images")
CONF_DIR = os.path.join(BASE_DIR, "conf")
TRANSLATION_DIR = os.path.join(BASE_DIR, "translations")
UI_DIR = os.path.join(BASE_DIR, "ui")

__all__ = ["BASE_DIR", "IMAGES_DIR", "CONF_DIR", "TRANSLATION_DIR", "UI_DIR"]
