ven
===

.. image:: https://pypip.in/d/ven/badge.png
        :target: https://pypi.python.org/pypi/ven/

.. image:: https://pypip.in/v/ven/badge.png
        :target: https://pypi.python.org/pypi/ven/

.. image:: https://pypip.in/license/ven/badge.png
        :target: https://pypi.python.org/pypi/ven/

Easy way to use virtualenv.


Features
--------
- Store virtualenv in .venv directory, along with your .git and requirements.txt
- Run command inside virtualenv without activating it.


Install
-------
::

    $ pip install --user ven


Quickstart
----------

Initialize an empty virtualenv using `ven init`::

    $ ven init
    New python executable in .venv/bin/python
    Installing setuptools, pip...done.

    $ ls -A
    .ven

Run command inside virtualenv using `ven run`::

    $ ven run which python
    ~/project/.venv/bin/python

Activate virtualenv in a sub-shell::

    $ ven run
    $ which python
    ~/project/.venv/bin/python
    $ (Deactivate with Ctrl-D)


Usage
-----
::

    Usage: ven [OPTIONS] COMMAND [ARGS]...

      Easy way to use virtualenv

    Options:
      --help  Show this message and exit.

    Commands:
      init  Create a new virtualenv
      run   Run command in virtualenv (default: shell)


Caveats
-------

Use '--' to separate `ven run` options and command that contains '-'::

    $ ven run -- python --version
    Python 2.7.5

`oh-my-zsh` overwrites $PATH, add the following to your .zshrc::

    if [ -n "$VIRTUAL_ENV" ]; then
        export PATH="$VIRTUAL_ENV/bin:$PATH"
    fi

Recommanded aliases::

    alias vrun='ven run --'
    alias vpy='ven run -- python'
    alias vpip='ven run -- pip'
