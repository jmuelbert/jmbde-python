# -*- coding: utf-8 -*-
"""Test cases for the __main__ module."""
import pytest
from click.testing import CliRunner

# from jmbde import __main__


@pytest.fixture
def runner() -> CliRunner:
    """Fixture for invoking command-line interfaces."""
    return CliRunner()


def test_version(runner: CliRunner) -> None:
    """Test the main version."""
    # response = runner.invoke(__main__.main, ["--version"])
    # assert response.exit_code == 0
    pass
