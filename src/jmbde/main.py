#!/usr/bin/env python3

"""
Main entry point for the JMBDE application.
Allows running the application in different modes (CLI, GUI, API).
"""

import logging
import sys

import click

from jmbde.__main__ import main as gui_main
from jmbde.api.server import start_api_server

logger = logging.getLogger(__name__)


@click.command()
@click.option(
    "--mode",
    type=click.Choice(["gui", "api"], case_sensitive=False),
    default="gui",
    help="Run mode (GUI or API).",
)
def main(mode: str):
    """Start the JMBDE application in the specified mode."""
    if mode == "gui":
        logger.info("Starting JMBDE GUI...")
        gui_main()
    elif mode == "api":
        logger.info("Starting JMBDE API server...")
        start_api_server()
    else:
        logger.error(f"Unknown mode: {mode}")
        sys.exit(1)


if __name__ == "__main__":
    main()
