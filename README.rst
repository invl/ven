venv
====

.. image:: https://pypip.in/d/venv/badge.png
        :target: https://pypi.python.org/pypi/venv/

.. image:: https://pypip.in/v/venv/badge.png
        :target: https://pypi.python.org/pypi/venv/

.. image:: https://pypip.in/license/venv/badge.png
        :target: https://pypi.python.org/pypi/venv/

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


Caveats
-------

Use '--' to separate `venv run` options and command that contains '-'::

    $ venv run -- python --version
    Python 2.7.5

`oh-my-zsh` overwrites $PATH, add the following to your .zshrc::

    if [ -n "$VIRTUAL_ENV" ]; then
        export PATH="$VIRTUAL_ENV/bin:$PATH"
    fi
