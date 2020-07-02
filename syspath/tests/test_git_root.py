import copy
import sys
import unittest

from .. import syspath


class TestGitRoot(unittest.TestCase):
    def setUp(self) -> None:
        self.orig_sys_path = copy.deepcopy(sys.path)

    def tearDown(self) -> None:
        sys.path = self.orig_sys_path

    def test_import(self) -> None:
        self.assertEqual(len(sys.path), len(self.orig_sys_path))
        from .. import git_root  # noqa: F401
        self.assertIn(syspath.get_git_root(), sys.path)

    def test_path(self) -> None:
        from .. import git_root
        self.assertEqual(git_root.path, syspath.get_git_root())
