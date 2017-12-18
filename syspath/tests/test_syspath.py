import os
import unittest

import syspath

class TestSysPath(unittest.TestCase):
    def test_caller_path(self):
        path = syspath.caller_path(1)
        expected = os.path.realpath(__file__)
        self.assertEqual(path, expected)

