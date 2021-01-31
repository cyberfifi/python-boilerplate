import unittest

from src.sub import add


class SubTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(3, 1), 4)
