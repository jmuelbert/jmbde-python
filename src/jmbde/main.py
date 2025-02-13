#!/usr/bin/env python3

"""
Main entry point for the JMBDE application.
Allows running the application in different modes (CLI, GUI, API).
"""

import logging
import sys
from pathlib import Path

import click

from jmbde.__main__ import main as gui_main
from jmbde.api.server import start_api_server
from jmbde.core.db_handler import DBHandler

logger = logging.getLogger(__name__)


@click.command()
@click.option(
    "--mode",
    type=click.Choice(["gui", "api"], case_sensitive=False),
    default="gui",
    help="Run mode (GUI or API).",
)
@click.option(
    "--db-path",
    type=click.Path(),
    default="data/jmbde.db",
    help="Database file path",
)
def main(mode: str, db_path: str):
    """Start the JMBDE application in the specified mode."""
    try:
        db_handler = DBHandler(Path(db_path))

        if mode == "gui":
            logger.info("Starting JMBDE GUI...")
            gui_main(db_handler)
        elif mode == "api":
            logger.info("Starting JMBDE API server...")
            start_api_server(db_handler)
        else:
            logger.error(f"Unknown mode: {mode}")
            sys.exit(1)
    except Exception as e:
        logger.error(f"Application error: {e}")
        sys.exit(1)
    finally:
        if "db_handler" in locals():
            db_handler.cleanup()


if __name__ == "__main__":
    main()
