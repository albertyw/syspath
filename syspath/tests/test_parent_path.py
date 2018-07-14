import copy
import sys
import unittest

import syspath


class TestParentPath(unittest.TestCase):
    def setUp(self):
        self.orig_sys_path = copy.deepcopy(sys.path)

    def tearDown(self):
        sys.path = self.orig_sys_path

    def test_import(self):
        self.assertEqual(len(sys.path), len(self.orig_sys_path))
        from syspath import parent_path  # noqa: F401
        import syspath
        self.assertIn(syspath.get_parent_path(), sys.path)

    def test_path(self):
        from syspath import parent_path
        self.assertEqual(parent_path.path, syspath.get_parent_path())
