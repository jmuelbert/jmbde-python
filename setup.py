#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

import re
import os
from subprocess import check_call

from setuptools import setup, find_packages, Command
from setuptools.command.sdist import sdist

cmdclass = {}

try:
    from pyqt_distutils.build_ui import build_ui
    cmdclass = {'build_ui': build_ui}
except ImportError:
    cmdclass = {}

try:
    from sphinx.setup_command import BuildDoc
    cmdclass['build_docs'] = BuildDoc
except ImportError:
    pass


with open('jmbde/__init__.py') as f:
    _version = re.search(r'__version__\s+=\s+\'(.*)\'', f.read()).group(1)

with open("README.rst") as readme_file:
    readme = readme_file.read()

setup(
    name='jmbde',
    description="JMBde is a tool for collect data for a company",
    long_description=readme,
    version=_version,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: MacOS X',
        'Environment :: X11 Applications :: Qt',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: European Public License, Version 1.2 (EUPL-1.2)',
        "Natural Language :: English",
        'Operating System :: OS Independent',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Operating System :: POSIX :: Linux',
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        'Topic :: Database'
    ],
    keywords=['JMBde', 'BDE', 'Database', 'qt', 'qt5', 'pysyde2'],
    author=u'Juergen Muelbert',
    author_email='juergen.muelbert@gmail.com',
    url='https://github.com/jmuelbert/jmbde-python',
    license='EUPL-1.2',
    packages=['jmbde'],
    package_data={
        'jmbde': [
            '*.ui',
            '*.qrc',
            'languages/*.ts',
            'i18n/*.qm'
        ],
        '': ['../README.rst', '../LICENSE', '../LICENSE.DE'],
        'docs': ['*.rst'],
        'i18n': ['*']
    },
    exclude_package_data={'docs': ['*.mEoS.*.rst', "*_ref.rst"]},
    extras_require={},

    entry_points={
        'gui_scripts': ['jmbde=app.__main__:main'],
    },
    install_requires=[
        'PySide2',
        'Qt.py',
    ],
    cmdclass=cmdclass,
    test_suite='tests',
    tests_require=["pytest"],
    include_package_data=True,
    zip_safe=False,
)
