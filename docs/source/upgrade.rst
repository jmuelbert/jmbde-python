.. _upgrade:

Upgrade
=======

.. Note::
    Upgrade steps for older versions can be found at the
    `Wiki <https://github.com/jmuelbert/jmbde-python/wiki/Upgrading>`_

.. Note::
    Make sure to check the changelog for every patch version
    of the upgrading target and make changes accordingly.
    Check the logs for Spirit deprecation warnings.

.. Warning::
    Trying to skip a minor version while upgrading will break things. For example, it's
    not possible to upgrade from 0.4.x to 0.6.x without upgrading to 0.5.x first,
    however it's possible to skip patch versions, i.e: upgrade from 0.4.x to 0.4.xx

From v0.0.x to v0.0.x
---------------------

Starting from jmbde v0.0.1, cloning the repo is no longer encouraged. Pip it instead.

Installation::

    pip install -I jmbde
    # Replace the x by the latest patch version

Migration::
