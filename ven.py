import os
import subprocess
import sys

import click


VENV_DIR = '.venv'

if os.name == 'nt':
    BIN_DIR = 'Scripts'
    SHELL_ENV = 'COMSPEC'
else:
    BIN_DIR = 'bin'
    SHELL_ENV = 'SHELL'


def find_base_dir(path):
    if os.path.exists(os.path.join(path, VENV_DIR)):
        return path
    parent, _ = os.path.split(path)
    return None if parent == path else find_base_dir(parent)


class VEnv(object):

    def __init__(self, path):
        self.base_dir = find_base_dir(path)
        if not self.base_dir:
            fatal('Not a virtualenv (or any of the parent directories): .venv')
        self.venv_dir = os.path.join(self.base_dir, VENV_DIR)
        self.bin_dir = os.path.join(self.venv_dir, BIN_DIR)

    def run(self, cmds=None):
        os.environ['VIRTUAL_ENV'] = self.venv_dir
        os.environ['PATH'] = os.pathsep.join(
            [self.bin_dir, os.environ['PATH']])
        os.environ.pop('PYTHON_HOME', None)
        return subprocess.call(cmds or [os.environ[SHELL_ENV]])


@click.group(help='Easy way to use virtualenv')
@click.version_option()
def main():
    pass


@main.command(help='Show help information')
@click.argument('command', required=False)
@click.pass_context
def help(ctx, command):
    cmds = {
        'help': help,
        'init': init,
        'run': run,
    }
    click.echo(cmds.get(command, main).get_help(ctx))


@main.command(help='Create a new virtualenv')
@click.option(
    '-p', '--python',
    metavar='PYTHON_EXE',
    help='The Python interpreter to use, passed to virtualenv')
def init(python):
    extra = ['--python', python] if python else []
    subprocess.check_call(['virtualenv', VENV_DIR] + extra)


@main.command(help='Run command in virtualenv (default: shell)')
@click.argument('command', nargs=-1, required=False)
def run(command):
    venv = VEnv(os.getcwd())
    sys.exit(venv.run(command))


def fatal(msg, code=1):
    click.echo('fatal: %s' % msg, err=True)
    sys.exit(code)

if __name__ == '__main__':
    main()
