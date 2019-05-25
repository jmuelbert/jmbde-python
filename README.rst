 jmbde
============

..  image:: https://img.shields.io/badge/license-EUPL-blue.svg
    :alt: GitHub license
    :target: https://joinup.ec.europa.eu/page/eupl-text-11-12
..  image:: https://img.shields.io/badge/code%20style-pep8-green.svg
    :alt: PEP8
    :target: https://www.python.org/dev/peps/pep-0008/

..  image:: https://ci.appveyor.com/api/projects/status/vmqd5y83u390tsrg?svg=true
    :alt: Build status
    :target: https://ci.appveyor.com/project/jmuelbert/jmbde-python

.. image:: https://travis-ci.org/jmuelbert/jmbde-python.svg?branch=master
    :alt: Build Status
    :target: https://travis-ci.org/jmuelbert/jmbde-python


jmbde is a program to collect data for the IT. The database contains employees, departments, functions, phones, mobiles, computers, printers, faxes and accounts.

jmbde use the cross-platform framework [Qt](http://www.qt.io/download-open-source/) with the PySide2 Extension,
which means it works with the most operating systems.

Supported Platforms
-------------------

The standalone binary packages support the following platforms:

* macOS 10.10 or later
* Windows 7 or later
* Linux

Sources
-------

The master branch represents the latest pre-release code.

* [Releases](https://github.com/jmuelbert/jmbde-python/releases)

* [Milestones](https://github.com/jmuelbert/jmbde-python/milestones)

Requests and Bug reports
-------------------------

* [GitHub issues (preferred)](https://github.com/jmuelbert/jmbde-python/issues)

Questions or Comments
---------------------

Wiki
----

* [Main Page](https://github.com/jmuelbert/jmbde-python/wiki)
* [User Manual](http://jmuelbert.github.io/jmbde-python/)

Resources and translations
--------------------------

In order to ease the development process, the Qt Creator project ``app.pro`` is
provided. You can open it to edit the UI files or to manage resources.
Translations can be edited using Qt Linguist, part of the Qt SDK. In order to
build the translations, you will need to have the ``lrelease`` command on your
``PATH`` or set its full path to the ``LRELEASE_BIN`` environment variable.
UI files, translations and resources can be built like this::

    python setup.py build_res

Note that this command is automatically run before running ``sdist`` and
``bdist_app`` commands.

Compiled application
--------------------

You can generate a *compiled* application so that end-users do not need to
install anything. You can tweak some settings on the ``app.spec`` file. It can
be generated like this::

    python setup.py bdist_app

Documentation
-------------

Sphinx_ is used for documentation purposes. You can tweak its configuration in
``docs/conf.py`` and the documentation can be built like this::

    python setup.py build_docs

Linting
-------

Flake8 is a great tool to check for style issues, unused imports and similar
stuff. You can tweak ``.flake8`` to ignore certain types of errors, increase the
maximum line length, etc. You can run it like this::

    flake8 app

License
-------

jmbde is free software; you can redistribute ot and/or modify ir under the terms
of the [European Public License Version 1.2](https://joinup.ec.europa.eu/page/eupl-text-11-12).
Please read the [LICENSE](https://github.com/jmuelbert/jmbde-python/blob/master/LICENSE) for additional information.

EUPL-1.2 © [Jürgen Mülbert](https:/github.com/jmuelbert/jmbde-python)

[Return to top](#top)
