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
"""Tests for `jmbde-python` package."""
import jmbde.models.datacontext as dc


def test_init() -> None:
    """Sample Test."""
    datacontext = dc.DataContext()

    result = datacontext.init()
    assert result
