venv
====

Easy way to use virtualenv

Quickstart
----------

Install `venv`::

    $ pip install --user venv

Activate virtualenv inside `.venv` (Create if not exists)::

    $ venv

::

    New python executable in /tmp/venv/.venv/bin/python
    Installing setuptools, pip...done.

Run `pip list` inside virtualenv without activating it::

    $ venv pip list

::

    pip (1.5.6)
    setuptools (3.6)
    wsgiref (0.1.2)

`venv` can find `.venv` in ancestor directory::

    $ mkdir foo && cd foo
    $ venv pip list

::

    (same as previous example)
