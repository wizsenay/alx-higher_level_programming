#!/usr/bin/python3

"""test the class rectangle"""

import unittest
import sys
sys.path.append("/alx-higher_level_programming/0x0C-python-almost_a_circle")

from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """unsed to test all atributers in the rectangle class"""

    def test_init(self):
        rectangle_1 = Rectangle(4, 3,  2, 1)
        rectangle_2 = Rectangle(10, 9,  1,)
        rectangle_3 = Rectangle(5, 5,)


        self.assertEqual(rectangle_1.width, 4)
        self.assertEqual(rectangle_1.height, 3)
        self.assertEqual(rectangle_1.x, 2)
        self.assertEqual(rectangle_1.y, 1)

        self.assertEqual(rectangle_2.width, 10)
        self.assertEqual(rectangle_2.height, 9)
        self.assertEqual(rectangle_2.x, 1)
        self.assertEqual(rectangle_2.y, 0)

        self.assertEqual(rectangle_3.width, 5)
        self.assertEqual(rectangle_3.height, 5)
        self.assertEqual(rectangle_3.x, 0)
        self.assertEqual(rectangle_3.y, 0)

    def test_TypeError_attributers_init(self):

        # tese the correct error are raise
        # check when rong type(other than int) it rise TypeError

        with self.assertRaises(TypeError, msg="width must be an integer"):
            Rectangle("not_int", 3)  # for width atrributer
        with self.assertRaises(TypeError, msg="height must be an integer"):
            Rectangle(3, 4.567)  # for hieght attributer
        with self.assertRaises(TypeError, msg="x must be an integer"):
            Rectangle(3, 4, "not_int")  # for x attributer
        with self.assertRaises(TypeError, msg="y must be an integer"):
            Rectangle(3, 4, 8, "nit")  # for y attribyter

    def test_ValueError_attributers_init(self):
        # tese the correct errors are raises
        # check when wrong value pass it raise aValueError

        with self.assertRaises(ValueError, msg="width must be > 0"):
            Rectangle(-2, 3)  # for width atrributer
        with self.assertRaises(ValueError, msg="height must be > 0"):
            Rectangle(2, 0)  # for hieght attributer
        with self.assertRaises(ValueError, msg="x must be >= 0"):
            Rectangle(2, 3, -3)  # for x attributer
        with self.assertRaises(ValueError, msg="y must be >= 0"):
            Rectangle(2, 3, 1, -2)  # for y attribyter


if __name__ == '__main__':
    unittest.main()
