import copy
import os
import sys
import unittest


class TestGitRoot(unittest.TestCase):
    def setUp(self):
        self.orig_sys_path = copy.deepcopy(sys.path)

    def tearDown(self):
        sys.path = self.orig_sys_path

    def test_import(self):
        self.assertEqual(len(sys.path), len(self.orig_sys_path))
        from syspath import git_root  # noqa: F401
        import syspath
        self.assertIn(syspath.get_git_root(), sys.path)
