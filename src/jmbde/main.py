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
"""JMBDe app."""
import click
import logging
from jmbde import create_app

@click.command()
@click.version_option()
def main() -> None:
    """The Application main function."""
    app = create_app()
    app.run()


if __name__ == "__main__":
    main(prog_name="jmbde-python")
    logger = logging.getLogger(__name__)
    logger.info("Operation completed successfully")  # pragma: no cover
