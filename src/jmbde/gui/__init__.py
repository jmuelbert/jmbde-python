"""The Application class identifier."""
import os

"""The configs."""

BASE_DIR = os.path.join(os.path.dirname(__file__), "..")
IMAGES_DIR = os.path.join(BASE_DIR, "images")
CONF_DIR = os.path.join(BASE_DIR, "conf")
TRANSLATION_DIR = os.path.join(BASE_DIR, "translations")
UI_DIR = os.path.join(BASE_DIR, "ui")

__all__ = ["BASE_DIR", "IMAGES_DIR", "CONF_DIR", "TRANSLATION_DIR", "UI_DIR"]
