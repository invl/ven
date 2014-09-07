import subprocess


def test_run():
    subprocess.check_call('ven init'.split())
    subprocess.check_call('ven run -- python --version'.split())
