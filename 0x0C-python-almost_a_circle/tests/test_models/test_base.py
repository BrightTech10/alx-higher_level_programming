#!/usr/bin/python3
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    # Tests for NoneType
    def test_value_None(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)

    # Tests for int
    def test_value_int(self):
        b1 = Base(12)
        self.assertEqual(b1.id, 12)
        b2 = Base(-44)
        self.assertEqual(b2.id, -44)


if __name__ == '__main__':
    unittest.main
