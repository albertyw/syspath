import copy
import os
import sys
import unittest

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
