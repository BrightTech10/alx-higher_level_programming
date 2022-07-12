#!/usr/bin/python3
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    def test_args(self):
        # Test for argument(string)
        with self.assertRaises(TypeError):
            print(Square("5"))
        # Test for argument(float)
        with self.assertRaises(TypeError):
            print(Square(8.9))
        # Test for argument(empty)
        with self.assertRaises(TypeError):
            print(Square())
        # Test for argument(NoneType)
        with self.assertRaises(TypeError):
            print(Square(None))

    # Test for size
    def test_size(self):
        self.assertEqual(Square(5).size, 5)
        # (string)
        with self.assertRaises(TypeError):
            Square("5").size
        # (float)
        with self.assertRaises(TypeError):
            Square(4.4).size
        # (empty)
        with self.assertRaises(TypeError):
            Square().size
        # (zero)
        with self.assertRaises(ValueError):
            Square(0).size
        # (NoneType)
        with self.assertRaises(TypeError):
            Square(None).size

    # Tests for update method
    def test_update(self):
        r1 = Square(1, 2, 3, 4)
        # args(string)
        with self.assertRaises(TypeError):
            r1.update("89", "2", "3", "4")
        # args(float)
        with self.assertRaises(TypeError):
            r1.update(89, 2.7, 3.3, 4.2)
        # args(zero)
        with self.assertRaises(ValueError):
            r1.update(89, 0, 0, 0, 0)
        # kwargs(string)
        with self.assertRaises(TypeError):
            r1.update(x="2")
        # kwargs(zero)
        with self.assertRaises(ValueError):
            r1.update(size=0)


if __name__ == '__main__':
    unittest.main()
