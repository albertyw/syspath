import copy
import sys
import unittest

from .. import syspath


class TestParentPath(unittest.TestCase):
    def setUp(self) -> None:
        self.orig_sys_path = copy.deepcopy(sys.path)

    def tearDown(self) -> None:
        sys.path = self.orig_sys_path

    def test_import(self) -> None:
        self.assertEqual(len(sys.path), len(self.orig_sys_path))
        from .. import parent_path  # noqa: F401
        self.assertIn(syspath.get_parent_path(), sys.path)

    def test_path(self) -> None:
        from .. import parent_path
        self.assertEqual(parent_path.path, syspath.get_parent_path())
