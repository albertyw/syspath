import copy
import os
import sys
import unittest

try:
    from unittest.mock import patch
except ImportError:
    from mock import patch

import syspath


class TestSysPath(unittest.TestCase):
    def setUp(self):
        self.orig_sys_path = copy.deepcopy(sys.path)

    def tearDown(self):
        sys.path = self.orig_sys_path

    def test_append_path(self):
        syspath._append_path('asdf')
        self.assertEqual(sys.path[-1], 'asdf')

    def test_caller_path(self):
        path = syspath._caller_path(1)
        expected = os.path.dirname(os.path.realpath(__file__))
        self.assertEqual(path, expected)

    def test_caller_path_error(self):
        with self.assertRaises(RuntimeError):
            syspath._caller_path(100)

    def test_append_current_path(self):
        appended_path = syspath.append_current_path()
        self.assertEqual(len(sys.path), len(self.orig_sys_path)+1)
        self.assertEqual(appended_path, sys.path[-1])
        self.assertEqual(os.path.split(appended_path)[1], 'tests')

    def test_append_cli_path(self):
        with patch('syspath.syspath._caller_path') as mock_caller_path:
            mock_caller_path.side_effect = RuntimeError()
            appended_path = syspath.append_current_path()
        self.assertEqual(appended_path, sys.path[-1])
        self.assertEqual(appended_path, os.getcwd())

    def test_append_git_root(self):
        appended_path = syspath.append_git_root()
        self.assertEqual(len(sys.path), len(self.orig_sys_path)+1)
        self.assertEqual(appended_path, sys.path[-1])
        self.assertEqual(os.path.split(appended_path)[1], 'syspath')

    def test_append_git_root_cli(self):
        with patch('syspath.syspath._caller_path') as mock_caller_path:
            mock_caller_path.side_effect = RuntimeError()
            appended_path = syspath.append_git_root()
        self.assertEqual(appended_path, sys.path[-1])
        self.assertEqual(os.path.split(appended_path)[1], 'syspath')

    def test_append_git_root_error(self):
        with patch('syspath.syspath._caller_path') as mock_caller_path:
            root = os.path.abspath(os.sep)
            mock_caller_path.return_value = root
            with self.assertRaises(RuntimeError):
                syspath.append_git_root()

    def test_append_parent_path(self):
        appended_path = syspath.append_parent_path()
        self.assertEqual(len(sys.path), len(self.orig_sys_path)+1)
        self.assertEqual(appended_path, sys.path[-1])
        self.assertEqual(os.path.split(appended_path)[1], 'syspath')

    def test_append_cli_parent_path(self):
        with patch('syspath.syspath._caller_path') as mock_caller_path:
            mock_caller_path.side_effect = RuntimeError()
            appended_path = syspath.append_parent_path()
        self.assertEqual(appended_path, sys.path[-1])
        path = os.getcwd()
        parent = os.path.abspath(os.path.join(path, os.pardir))
        self.assertEqual(appended_path, parent)
