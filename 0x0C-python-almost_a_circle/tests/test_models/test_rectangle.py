#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    # Tests for id
    def test_id(self):
        self.assertEqual(Rectangle(10, 2).id, 1)
        self.assertEqual(Rectangle(2, 10).id, 2)
        self.assertEqual(Rectangle(10, 2, 0, 0, 12).id, 12)
        self.assertEqual(Rectangle(10, 2, 0, 0, None).id, 3)

    # Tests for width and height (string)
    def test_value_string(self):
        with self.assertRaises(TypeError):
            Rectangle(10, "2")
        with self.assertRaises(TypeError):
            Rectangle("10", 2)
        with self.assertRaises(TypeError):
            Rectangle("10", "2")

    # Tests for width and height (Nonetype)
    def test_value_None(self):
        with self.assertRaises(TypeError):
            Rectangle(None, "2")
        with self.assertRaises(TypeError):
            Rectangle(6, None)
        with self.assertRaises(TypeError):
            Rectangle(None, None)

    # Tests for width and height (empty)
    def test_value_None(self):
        with self.assertRaises(TypeError):
            Rectangle(6)
        with self.assertRaises(TypeError):
            Rectangle()

    # Tests for width and height (float)
    def test_value_float(self):
        with self.assertRaises(TypeError):
            Rectangle(10, 3.7)
        with self.assertRaises(TypeError):
            Rectangle(10.9, 2)
        with self.assertRaises(TypeError):
            Rectangle(9.0, 8.6)

    # Tests for width and height (zero)
    def test_value_zero(self):
        with self.assertRaises(ValueError):
            Rectangle(10, 0)
        with self.assertRaises(ValueError):
            Rectangle(0, 2)
        with self.assertRaises(ValueError):
            Rectangle(0, 0)

    # Tests for width and height (negative int)
    def test_value_negative(self):
        with self.assertRaises(ValueError):
            Rectangle(10, -1)
        with self.assertRaises(ValueError):
            Rectangle(-8, 2)
        with self.assertRaises(ValueError):
            Rectangle(-7, -4)

    # Tests for x
    def test_x(self):
        # For int
        self.assertEqual(Rectangle(10, 2, 3, 1).x, 3)
        # For dict type
        with self.assertRaises(TypeError):
            r2 = Rectangle(10, 2, {}, 8)
        # For None type
        with self.assertRaises(TypeError):
            r2 = Rectangle(10, 2, None, 8)
        # For float
        with self.assertRaises(TypeError):
            r2 = Rectangle(10, 2, 6.6, 8)
        # For string
        with self.assertRaises(TypeError):
            r2 = Rectangle(10, 2, "6", 8)
        # For negative int
        with self.assertRaises(ValueError):
            r2 = Rectangle(10, 2, -2, 9)

    # Tests for y
    def test_y(self):
        # For int
        self.assertEqual(Rectangle(10, 2, 3, 1).y, 1)
        # For string
        with self.assertRaises(TypeError):
            r2 = Rectangle(10, 2, 0, "8")
        # For float
        with self.assertRaises(TypeError):
            r2 = Rectangle(10, 2, 0, 8.8)
        # For dict type
        with self.assertRaises(TypeError):
            r2 = Rectangle(10, 2, 0, {})
        # For None type
        with self.assertRaises(TypeError):
            r2 = Rectangle(10, 2, 1, None)
        # For negative int
        with self.assertRaises(ValueError):
            r2 = Rectangle(10, 2, 2, -9)

    # Tests for area
    def test_area(self):
        # All int
        self.assertEqual(Rectangle(8, 7, 0, 0, 12).area(), 56)
        # Height (string)
        with self.assertRaises(TypeError):
            Rectangle(10, "7").area()
        # Height (float)
        with self.assertRaises(TypeError):
            Rectangle(10, 7.7).area()
        # Height (zero)
        with self.assertRaises(ValueError):
            Rectangle(10, 0).area()
        # Height (Nonetype)
        with self.assertRaises(TypeError):
            Rectangle(10, None).area()
        # Height (zero)
        with self.assertRaises(ValueError):
            Rectangle(10, 0).area()
        # Width (string)
        with self.assertRaises(TypeError):
            Rectangle("10", 7).area()
        # Width (float)
        with self.assertRaises(TypeError):
            Rectangle(10.9, 7).area()
        # Width (zero)
        with self.assertRaises(ValueError):
            Rectangle(0, 7).area()
        # Width (NoneType)
        with self.assertRaises(TypeError):
            Rectangle(None, 7).area()
        # One argument
        with self.assertRaises(TypeError):
            Rectangle(10).area()
        # No argument
        with self.assertRaises(TypeError):
            Rectangle().area()
        # Width and height(NoneType)
        with self.assertRaises(TypeError):
            Rectangle(None, None).area()

    # Tests for display
    def test_display(self):
        # Height (string)
        with self.assertRaises(TypeError):
            Rectangle(10, "7").display()
        # Height (float)
        with self.assertRaises(TypeError):
            Rectangle(10, 7.7).display()
        # Height (zero)
        with self.assertRaises(ValueError):
            Rectangle(10, 0).display()
        # Height (Nonetype)
        with self.assertRaises(TypeError):
            Rectangle(10, None).display()
        # Height (zero)
        with self.assertRaises(ValueError):
            Rectangle(10, 0).display()
        # Width (string)
        with self.assertRaises(TypeError):
            Rectangle("10", 7).display()
        # Width (float)
        with self.assertRaises(TypeError):
            Rectangle(10.9, 7).display()
        # Width (zero)
        with self.assertRaises(ValueError):
            Rectangle(0, 7).display()
        # Width (NoneType)
        with self.assertRaises(TypeError):
            Rectangle(None, 7).display()
        # One argument
        with self.assertRaises(TypeError):
            Rectangle(10).display()
        # No argument
        with self.assertRaises(TypeError):
            Rectangle().display()
        # Width and height(NoneType)
        with self.assertRaises(TypeError):
            Rectangle(None, None).display()

    # Tests for __str__ method
    def test_str(self):
        # String
        with self.assertRaises(TypeError):
            print(Rectangle(4, 6, "2", 1, 12))
        # Float
        with self.assertRaises(TypeError):
            print(Rectangle(4, 6, 3.9, 1, 12))
        # Zero
        with self.assertRaises(ValueError):
            print(Rectangle(4, 0, 3, 1, 12))

    # Tests for update method
    def test_update(self):
        r1 = Rectangle(10, 10, 10, 10)
        # String
        with self.assertRaises(TypeError):
            r1.update("89", "2", "3", "4", "5")
        with self.assertRaises(TypeError):
            r1.update(id='89', width=2)
        # Float
        with self.assertRaises(TypeError):
            r1.update(89, 2.7, 3.3, 4.2, 4.4)
        with self.assertRaises(TypeError):
            r1.update(height=3.3)
        # Zero
        with self.assertRaises(ValueError):
            r1.update(89, 0, 0, 0, 0)
        with self.assertRaises(ValueError):
            r1.update(x=0)


if __name__ == '__main__':
    unittest.main()
