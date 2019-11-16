jmbde
=====

.. image:: https://img.shields.io/pypi/v/jmbde-python.svg
        :target: https://pypi.python.org/pypi/jmbde-python/
        :alt: PyPi

.. image:: https://img.shields.io/pypi/wheel/jmbde-python.svg
        :target: https://pypi.python.org/pypi/jmbde-python/
        :alt: Wheel

.. image:: https://img.shields.io/pypi/pyversions/jmbde-python.svg
        :target: https://pypi.python.org/pypi/jmbde-python/
        :alt: PyPi-Versions

.. image:: https://pyup.io/repos/github/jmuelbert/jmbde-python/shield.svg
     :target: https://pyup.io/repos/github/jmuelbert/jmbde-python/
     :alt: Updates

.. image:: https://pyup.io/repos/github/jmuelbert/jmbde-python/python-3-shield.svg
     :target: https://pyup.io/repos/github/jmuelbert/jmbde-python/
     :alt: Python 3

..  image:: https://img.shields.io/badge/license-EUPL-blue.svg
    :alt: GitHub license
    :target: https://joinup.ec.europa.eu/page/eupl-text-11-12

.. image:: https://travis-ci.org/jmuelbert/jmbde-python.svg?branch=master
    :alt: Build Status
    :target: https://travis-ci.org/jmuelbert/jmbde-python

..  image:: https://ci.appveyor.com/api/projects/status/vmqd5y83u390tsrg?svg=true
    :alt: Build status
    :target: https://ci.appveyor.com/project/jmuelbert/jmbde-python

jmbde is a program to collect data for the IT. The database contains employees, departments, functions, phones, mobiles, computers, printers, faxes and accounts.

jmbde use the cross-platform frameworks `python <https://www.python.org>`_
and `QT <https://www.qt.io>`_
with the `PySide2 <https://pypi.org/project/PySide2/>`_.
which means it works with the most operating systems.

Sources
-------

The master branch represents the latest pre-release code.

- `Releases <https://github.com/jmuelbert/jmbde-python/releases>`_.

- `Milestones <https://github.com/jmuelbert/jmbde-python/milestones>`_.

Requests and Bug reports
-------------------------

- `GitHub issues (preferred) <https://github.com/jmuelbert/jmbde-python/issues>`_.

Questions or Comments
---------------------

Wiki
----

- `Main Page <https://github.com/jmuelbert/jmbde-python/wiki>`_.
- `User Manual <http://jmuelbert.github.io/jmbde-python/>`_.

Installing
----------

An install script is preferred. You can you the latest release or build the newest version with the command:

    ``./setup.py setup_qt sdist``

or
    ``python setup.py setup_qt sdist``

This build an python installer

Resources and translations
--------------------------

In order to ease the development process, the Qt Creator project ``app.pro`` is
provided. You can open it to edit the UI files or to manage resources.
Translations can be edited using Qt Linguist, part of the Qt SDK. In order to
build the translations, you will need to have the ``lrelease`` command on your
``PATH`` or set its full path to the ``LRELEASE_BIN`` environment variable.
UI files, translations and resources can be built like this::

    ``python setup.py setup_qt sdist bdist_wheel``

Note that this command is automatically run before running ``sdist`` and
``bdist_app`` commands.

Compiled application
--------------------

You can generate a *compiled* application so that end-users do not need to
install anything. You can tweak some settings on the ``app.spec`` file. It can
be generated like this::

    ``python pyinstaller``

Documentation
-------------

`Sphinx <https://sphinx.readthedocs.io/en/master/>`_ is used for documentation purposes. You can tweak its configuration in
``docs/conf.py`` and the documentation can be built like this::

    ``cd docs``
    ``pip install -r requirements.txt```
    or
    ``conda create -n build_docs -f environment.yml```
    ``conda activate build_docs```
    The docs can you build with the command:
    ``make html`` to build the web documentation


License
-------

openorders is free software; you can redistribute ot and/or modify ir under the terms
of the `European Public License Version 1.2 <https://joinup.ec.europa.eu/page/eupl-text-11-12>`_.
Please read the `<https://github.com/jmuelbert/jmbde-python/blob/master/LICENSE>`_ for additional information.

EUPL-1.2 © Jürgen Mülbert
