#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests for `jmbde-python` package."""
# Third party imports
import jmbde
import pytest


@pytest.fixture
def response() -> None:
    """Sample pytest fixture."""
    # See more at: http://doc.pytest.org/en/latest/fixture.html.

    pass


def content_test(response) -> None:
    """Sample pytest test function with the pytest fixture as an argument."""
    pass


def command_line_interface_test() -> None:
    """Sample pytest test function with the pytest fixture as an argument."""
    pass


def test_main_window(response) -> None:
    assert jmbde.test() == 'Hello'
