#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max_int(self):
        self.assertEqual(max_integer([1, 2, 4, 3]), 4)
        self.assertEqual(max_integer([3, 3, 3, 3]), 3)
        self.assertEqual(max_integer([1.2, 4.6, 6, 7.9]), 7.9)
        self.assertEqual(max_integer([-1, -10, -100, -290]), -1)
        self.assertIsNone(max_integer())
        self.assertIsNone(max_integer([]))
        self.assertEqual(max_integer(["string"]), 'string')

if __name__ == "__main__":
    unittest.main()
