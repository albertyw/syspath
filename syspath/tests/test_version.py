import unittest

from syspath import __version__


class TestVersion(unittest.TestCase):
    def test_version(self) -> None:
        self.assertTrue(__version__)
