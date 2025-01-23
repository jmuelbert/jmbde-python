#!/usr/bin/env python3

"""
Settings Management Module for JMBDE

This module handles application settings and configuration management
for the JMBDE application.

Copyright (C) 2018-2024 Jürgen Mülbert
License: GPL-3.0
"""

import json
import logging
from pathlib import Path
from typing import Any, Optional

from pydantic import BaseModel, Field, ValidationError
from PySide6.QtCore import Property, QObject, Signal, Slot

from jmbde.utils.exceptions import ConfigurationError

# Initialize logger
logger = logging.getLogger(__name__)


class DatabaseSettings(BaseModel):
    """Database configuration settings."""

    path: Path = Field(default=Path.home() / ".jmbde" / "data" / "jmbde.db")
    backup_path: Path = Field(default=Path.home() / ".jmbde" / "backups")
    backup_count: int = Field(default=5, ge=1, le=20)
    auto_backup: bool = Field(default=True)


class UISettings(BaseModel):
    """User interface settings."""

    theme: str = Field(default="light")
    language: str = Field(default="en")
    font_size: int = Field(default=12, ge=8, le=24)
    window_width: int = Field(default=1024, ge=800)
    window_height: int = Field(default=768, ge=600)
    show_toolbar: bool = Field(default=True)
    show_statusbar: bool = Field(default=True)


class ApplicationSettings(BaseModel):
    """General application settings."""

    company_name: str = Field(default="")
    department: str = Field(default="")
    admin_email: str = Field(default="")
    auto_update: bool = Field(default=True)
    update_check_interval: int = Field(default=7, ge=1)  # days
    log_level: str = Field(default="INFO")
    debug_mode: bool = Field(default=False)


class Settings(QObject):
    """
    Settings management class for JMBDE application.

    Handles loading, saving, and accessing application settings
    with Qt property bindings for QML integration.
    """

    # Qt Signals for settings changes
    settingsChanged = Signal()
    themeChanged = Signal(str)
    languageChanged = Signal(str)

    def __init__(self, config_path: Optional[Path] = None) -> None:
        """
        Initialize Settings manager.

        Args:
        ----
            config_path: Optional custom path for settings file

        """
        super().__init__()
        self._config_path = config_path or Path.home() / ".jmbde" / "config.json"
        self._config_path.parent.mkdir(parents=True, exist_ok=True)

        # Initialize settings with defaults
        self._database = DatabaseSettings()
        self._ui = UISettings()
        self._application = ApplicationSettings()

        logger.info(f"Settings initialized with config path: {self._config_path}")

    def load(self) -> None:
        """
        Load settings from configuration file.

        Raises
        ------
            ConfigurationError: If loading or parsing settings fails

        """
        try:
            if self._config_path.exists():
                config_data = json.loads(self._config_path.read_text())

                # Load and validate each settings section
                self._database = DatabaseSettings(**config_data.get("database", {}))
                self._ui = UISettings(**config_data.get("ui", {}))
                self._application = ApplicationSettings(
                    **config_data.get("application", {}),
                )

                logger.info("Settings loaded successfully")
                self.settingsChanged.emit()
            else:
                logger.info("No existing configuration found, using defaults")
                self.save()  # Save defaults
        except (json.JSONDecodeError, ValidationError) as e:
            logger.error(f"Failed to load settings: {e}")
            raise ConfigurationError(f"Invalid configuration file: {e}") from e
        except Exception as e:
            logger.error(f"Unexpected error loading settings: {e}")
            raise ConfigurationError(f"Failed to load settings: {e}") from e

    def save(self) -> None:
        """
        Save current settings to configuration file.

        Raises
        ------
            ConfigurationError: If saving settings fails

        """
        try:
            config_data = {
                "database": self._database.dict(),
                "ui": self._ui.dict(),
                "application": self._application.dict(),
            }

            # Convert Path objects to strings for JSON serialization
            config_data["database"]["path"] = str(config_data["database"]["path"])
            config_data["database"]["backup_path"] = str(
                config_data["database"]["backup_path"],
            )

            self._config_path.write_text(
                json.dumps(config_data, indent=4, sort_keys=True),
            )
            logger.info("Settings saved successfully")
        except Exception as e:
            logger.error(f"Failed to save settings: {e}")
            raise ConfigurationError(f"Failed to save settings: {e}") from e

    # Qt Property Getters/Setters for QML binding
    @Property(str)
    def theme(self) -> str:
        """Get current theme."""
        return self._ui.theme

    @theme.setter
    def theme(self, value: str) -> None:
        """Set current theme."""
        if value != self._ui.theme:
            self._ui.theme = value
            self.themeChanged.emit(value)
            self.save()

    @Property(str)
    def language(self) -> str:
        """Get current language."""
        return self._ui.language

    @language.setter
    def language(self, value: str) -> None:
        """Set current language."""
        if value != self._ui.language:
            self._ui.language = value
            self.languageChanged.emit(value)
            self.save()

    # Slot methods for QML interaction
    @Slot(str, result=Any)
    def getValue(self, key: str) -> Any:
        """
        Get setting value by key path.

        Args:
        ----
            key: Dot-notation path to setting (e.g., 'ui.font_size')

        Returns:
        -------
            Setting value or None if not found

        """
        try:
            section, setting = key.split(".")
            if section == "database":
                return getattr(self._database, setting)
            elif section == "ui":
                return getattr(self._ui, setting)
            elif section == "application":
                return getattr(self._application, setting)
            return None
        except Exception as e:
            logger.error(f"Failed to get setting {key}: {e}")
            return None

    @Slot(str, Any)
    def setValue(self, key: str, value: Any) -> None:
        """
        Set setting value by key path.

        Args:
        ----
            key: Dot-notation path to setting
            value: New value to set

        """
        try:
            section, setting = key.split(".")
            if section == "database":
                setattr(self._database, setting, value)
            elif section == "ui":
                setattr(self._ui, setting, value)
            elif section == "application":
                setattr(self._application, setting, value)
            self.save()
            self.settingsChanged.emit()
        except Exception as e:
            logger.error(f"Failed to set setting {key}: {e}")

    @Slot()
    def resetToDefaults(self) -> None:
        """Reset all settings to default values."""
        try:
            self._database = DatabaseSettings()
            self._ui = UISettings()
            self._application = ApplicationSettings()
            self.save()
            self.settingsChanged.emit()
            logger.info("Settings reset to defaults")
        except Exception as e:
            logger.error(f"Failed to reset settings: {e}")

    def get_database_path(self) -> Path:
        """Get the configured database path."""
        return self._database.path

    def get_backup_path(self) -> Path:
        """Get the configured backup path."""
        return self._database.backup_path

    def get_log_level(self) -> str:
        """Get the configured logging level."""
        return self._application.log_level

    def is_debug_mode(self) -> bool:
        """Check if debug mode is enabled."""
        return self._application.debug_mode
