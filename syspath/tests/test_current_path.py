import copy
import sys
import unittest

import syspath


class TestCurrentPath(unittest.TestCase):
    def setUp(self):
        self.orig_sys_path = copy.deepcopy(sys.path)

    def tearDown(self):
        sys.path = self.orig_sys_path

    def test_import(self):
        self.assertEqual(len(sys.path), len(self.orig_sys_path))
        from syspath import current_path  # noqa: F401
        import syspath
        self.assertIn(syspath.get_current_path(), sys.path)

    def test_path(self):
        from syspath import current_path
        self.assertEqual(current_path.path, syspath.get_current_path())
