#
# SPDX-FileCopyrightText: 2023 Jürgen Mülbert <juergen.muelbert@web.de>
#
# SPDX-License-Identifier: EUPL-1.2
#
"""Command-line interface."""
import click


@click.command()
@click.help_option()
def main() -> None:
    print("Hello, world!")


if __name__ == "__main__":
    main()
