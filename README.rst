venv
====

Easy way to use virtualenv.


Features
--------
- Store virtualenv in .venv directory, kind of like a git repo.
- Run command inside virtualenv without activating it.


Install
-------
::

    $ pip install --user venv


Quickstart
----------

Initialize an empty virtualenv using `venv init`::

    $ venv init
    New python executable in .venv/bin/python
    Installing setuptools, pip...done.

    $ ls -A
    .venv

Run command inside virtualenv using `venv run`::

    $ venv run which python
    ~/project/.venv/bin/python

Activate virtualenv in a sub-shell::

    $ venv run
    $ which python
    ~/project/.venv/bin/python
    $ (Deactivate with Ctrl-D)
