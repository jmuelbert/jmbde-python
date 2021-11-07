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
# Standard library imports
"""The Extension for the python standard logger."""
import logging
import os


class Logger:
    """The extension class for the python logger."""

    def __init__(self) -> None:
        """The class initializer."""
        self.create_log()

    def create_log(self) -> logging.Logger:
        """For debugging and informational purposes.

        Returns:
            The logger.
        """
        self.ensure_log_folder_exists()
        log = logging.getLogger("jmbde_debug")

        if not self.logger_exists(log):
            handler = logging.FileHandler(self.create_log_filename())
            formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
            handler.setFormatter(formatter)
            log.addHandler(handler)
            log.setLevel(logging.DEBUG)

        return log

    @staticmethod
    def logger_exists(log: logging.Logger) -> bool:
        """Check the the logger exists.

        Args:
            log: The existing logger

        Returns:
            return true when the logger exists.
        """
        if len(log.handlers) > 0:
            return True
        else:
            return False

    @staticmethod
    def ensure_log_folder_exists() -> None:
        """Check the log folder exists.

        If the folder not exists then create them.
        """
        if not os.path.exists(os.path.join(os.path.expanduser("~"), "jmbde", "log")):
            os.makedirs(os.path.join(os.path.expanduser("~"), "jmbde", "log"))

    @staticmethod
    def create_log_filename() -> str:
        """Set the logging filename.

        Returns:
            A string with the filename for the logger.
        """
        return os.path.join(os.path.expanduser("~"), "jmbde", "log", "jmbde_debug.log")
