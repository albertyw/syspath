import copy
import sys
import unittest

from .. import syspath


class TestCurrentPath(unittest.TestCase):
    def setUp(self) -> None:
        self.orig_sys_path = copy.deepcopy(sys.path)

    def tearDown(self) -> None:
        sys.path = self.orig_sys_path

    def test_import(self) -> None:
        self.assertEqual(len(sys.path), len(self.orig_sys_path))
        from .. import current_path  # noqa: F401
        self.assertIn(syspath.get_current_path(), sys.path)

    def test_path(self) -> None:
        from .. import current_path
        self.assertEqual(current_path.path, syspath.get_current_path())
