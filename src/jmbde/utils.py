#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

BASE_DIR = Path(os.path.dirname(__file__)) / ".."
IMAGES_DIR = BASE_DIR / "images"
CONF_DIR = BASE_DIR / "conf"
TRANSLATION_DIR = BASE_DIR / "translations"
UI_DIR = BASE_DIR / "ui"

__all__ = ["BASE_DIR", "IMAGES_DIR", "CONF_DIR", "TRANSLATION_DIR", "UI_DIR"]
