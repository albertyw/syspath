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
        syspath.append_path('asdf')
        self.assertEqual(sys.path[-1], 'asdf')

    def test_caller_path(self):
        path = syspath.caller_path(1)
        expected = os.path.dirname(os.path.realpath(__file__))
        self.assertEqual(path, expected)

    def test_append_current_path(self):
        syspath.append_current_path()
        self.assertEqual(len(sys.path), len(self.orig_sys_path)+1)
        appended_path = sys.path[-1]
        self.assertEqual(os.path.split(appended_path)[1], 'tests')

    def test_append_cli_path(self):
        with patch('syspath.syspath.caller_path') as mock_caller_path:
            mock_caller_path.side_effect = RuntimeError()
            syspath.append_current_path()
        appended_path = sys.path[-1]
        self.assertEqual(appended_path, os.getcwd())
