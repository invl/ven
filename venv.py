import os
import subprocess
import sys


VENV_DIR = '.venv'


def find_base_dir(path):
    if os.path.exists(os.path.join(path, VENV_DIR)):
        return path
    if path == '/':
        return None
    return find_base_dir(os.path.split(path)[0])


def main():
    cwd = os.getcwd()
    base_dir = find_base_dir(cwd) or cwd
    venv_dir = os.path.join(base_dir, VENV_DIR)
    bin_dir = os.path.join(venv_dir, 'bin')

    if not os.path.exists(venv_dir):
        subprocess.check_call(['virtualenv', venv_dir])

    os.environ['VIRTUAL_ENV'] = venv_dir
    os.environ['PATH'] = bin_dir + ':' + os.environ['PATH']
    os.environ.pop('PYTHON_HOME', None)

    cmds = sys.argv[1:] or [os.environ['SHELL']]
    subprocess.check_call(cmds)


if __name__ == '__main__':
    main()
