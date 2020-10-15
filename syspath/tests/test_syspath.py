import copy
import os
import sys
import unittest
from unittest.mock import patch

from .. import syspath


class TestSysPath(unittest.TestCase):
    def setUp(self) -> None:
        self.orig_sys_path = copy.deepcopy(sys.path)

    def tearDown(self) -> None:
        sys.path = self.orig_sys_path

    def test_append_path(self) -> None:
        syspath._append_path('asdf')
        self.assertEqual(sys.path[-1], 'asdf')

    def test_append_path_deduplicates(self) -> None:
        syspath._append_path(sys.path[0])
        self.assertEqual(len(sys.path), len(self.orig_sys_path))

    def test_caller_path(self) -> None:
        path = syspath._caller_path(1)
        expected = os.path.dirname(os.path.realpath(__file__))
        self.assertEqual(path, expected)

    def test_caller_path_error(self) -> None:
        with self.assertRaises(RuntimeError):
            syspath._caller_path(100)

    def test_append_current_path(self) -> None:
        appended_path = syspath.append_current_path()
        self.assertEqual(len(sys.path), len(self.orig_sys_path)+1)
        self.assertIn(appended_path, sys.path)
        self.assertEqual(os.path.split(appended_path)[1], 'tests')

    def test_append_cli_path(self) -> None:
        with patch('syspath.syspath._caller_path') as mock_caller_path:
            mock_caller_path.side_effect = RuntimeError()
            appended_path = syspath.append_current_path()
        self.assertIn(appended_path, sys.path)
        self.assertEqual(appended_path, os.getcwd())

    def test_append_git_root(self) -> None:
        appended_path = syspath.append_git_root()
        self.assertIn(appended_path, sys.path)

        # Dive into the root
        current_path = syspath.get_current_path()
        expected = os.path.split(current_path)[0]
        expected = os.path.split(expected)[0]
        expected = os.path.split(expected)[1]

        self.assertEqual(os.path.split(appended_path)[1], expected)

    def test_append_git_root_cli(self) -> None:
        with patch('syspath.syspath._caller_path') as mock_caller_path:
            mock_caller_path.side_effect = RuntimeError()
            appended_path = syspath.append_git_root()
        self.assertIn(appended_path, sys.path)

        # Dive into the root
        current_path = syspath.get_current_path()
        expected = os.path.split(current_path)[0]
        expected = os.path.split(expected)[0]
        expected = os.path.split(expected)[1]

        self.assertEqual(os.path.split(appended_path)[1], expected)

    def test_append_git_root_error(self) -> None:
        with patch('syspath.syspath._caller_path') as mock_caller_path:
            root = os.path.abspath(os.sep)
            mock_caller_path.return_value = root
            with self.assertRaises(RuntimeError):
                syspath.append_git_root()

    def test_append_parent_path(self) -> None:
        appended_path = syspath.append_parent_path()
        self.assertEqual(len(sys.path), len(self.orig_sys_path)+1)
        self.assertIn(appended_path, sys.path)
        self.assertEqual(os.path.split(appended_path)[1], 'syspath')

    def test_append_cli_parent_path(self) -> None:
        with patch('syspath.syspath._caller_path') as mock_caller_path:
            mock_caller_path.side_effect = RuntimeError()
            appended_path = syspath.append_parent_path()
        self.assertIn(appended_path, sys.path)
        path = os.getcwd()
        parent = os.path.abspath(os.path.join(path, os.pardir))
        self.assertEqual(appended_path, parent)
