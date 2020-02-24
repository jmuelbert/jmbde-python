# -*- coding: utf-8 -*-
# Standard library imports
import logging
import os


class Logger:
    def __init__(self) -> None:
        self.create_log()

    def create_log(self) -> logging.Logger:
        """
        For debugging and informational purposes.
        """
        self.ensure_log_folder_exists()
        log = logging.getLogger("jmbde_debug")

        if not self.logger_exists(log):
            handler = logging.FileHandler(self.create_log_filename())
            formatter = logging.Formatter(
                "%(asctime)s %(levelname)s %(message)s")
            handler.setFormatter(formatter)
            log.addHandler(handler)
            log.setLevel(logging.DEBUG)

        return log

    @staticmethod
    def logger_exists(log) -> bool:
        if len(log.handlers) > 0:
            return True
        else:
            return False

    @staticmethod
    def ensure_log_folder_exists() -> None:
        if not os.path.exists(os.path.join(os.path.expanduser("~"),
                                           "jmbde", "log")):
            os.makedirs(os.path.join(os.path.expanduser("~"), "jmbde", "log"))

    @staticmethod
    def create_log_filename() -> str:
        return os.path.join(os.path.expanduser("~"), "jmbde",
                            "log", "jmbde_debug.log")