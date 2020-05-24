# -*- coding: utf-8 -*-
""" Test suite for the api module.

The script can be executed on its own or incorporated into a larger test suite.
However the tests are run, be aware of which version of the module is actually
being tested. If the library is installed in site-packages, that version takes
precedence over the version in this project directory. Use a virtualenv test
environment or setuptools develop mode to test against the development version.

"""
import pytest
<<<<<<< Updated upstream

from jmopenorders.api.hello import Hello  # tests __all__
from jmopenorders.api.report import Report
=======
from jmopenorders.api.hello import hello  # tests __all__
from jmopenorders.api.report import report
>>>>>>> Stashed changes


def test_Hello():
    """ Test the hello() function.

    """
    assert Hello() == "Hello, World!"
    return


def test_Hello_name():
    """ Test the hello() function with a name.

    """
    assert Hello("foo") == "Hello, foo!"
    return


def test_Report():
    """ Test the report() function.

    """
    assert Report() == "Hello, names.csv!"
    return


def test_Report_name():
    """ Test the report() function with a name.

    """
    assert Report("foo") == "Hello, foo!"
    return


# Make the script executable.

if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__]))
