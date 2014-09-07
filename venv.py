import os
import subprocess
import sys


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


def main():
    cwd = os.getcwd()
    base_dir = find_base_dir(cwd) or cwd
    venv_dir = os.path.join(base_dir, VENV_DIR)
    bin_dir = os.path.join(venv_dir, BIN_DIR)

    if not os.path.exists(venv_dir):
        subprocess.check_call(['virtualenv', venv_dir])

    os.environ['VIRTUAL_ENV'] = venv_dir
    os.environ['PATH'] = os.pathsep.join([bin_dir, os.environ['PATH']])
    os.environ.pop('PYTHON_HOME', None)

    cmds = sys.argv[1:] or [os.environ[SHELL_ENV]]
    subprocess.check_call(cmds)


if __name__ == '__main__':
    main()
