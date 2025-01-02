#
# SPDX-FileCopyrightText: 2023 Jürgen Mülbert <juergen.muelbert@web.de>
#
# SPDX-License-Identifier: EUPL-1.2
#
#
"""Tests for `jmbde_python` package."""

import pytest
from click.testing import CliRunner

from jmbde import __main__


@pytest.fixture
def runner() -> CliRunner:
    """Fixture for invoking command-line interfaces."""
    return CliRunner()


def test_main_succeeds(runner: CliRunner) -> None:
    """It exits with a status code of zero"""
    result = runner.invoke(__main__.main)
    assert result.exit_code == 0
