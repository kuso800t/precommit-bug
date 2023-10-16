from subprocess import check_call
from tempfile import TemporaryDirectory


def test0():
    with TemporaryDirectory() as tmpdir:
        def git(*args):
            check_call(("git", *args), cwd=tmpdir)
        git("init")
        git("add", ".")
