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

        self.assertEqual(rectangle_1.width, 4)
        self.assertEqual(rectangle_1.height, 3)
        self.assertEqual(rectangle_1.x, 2)
        self.assertEqual(rectangle_1.y, 1)

    def test_TypeError_attributers_init(self):

        # tese the correct error are raise
        # check when rong type(other than int) it rise TypeError

        with self.assertRaises(TypeError):
            Rectangle("not_int", 3)  # for width atrributer
            Rectangle(3, 4.567)  # for hieght attributer
            Rectangle(3, 4, "not_int")  # for x attributer
            Rectangle(3, 4, 8, True)  # for y attribyter

    def test_ValueError_attributers_init(self):
        # tese the correct errors are raises
        # check when wrong value pass it raise aValueError

        with self.assertRaises(ValueError):
            Rectangle(-2, 3, 1, 2)  # for width atrributer
            Rectangle(2, -3, 1, 2)  # for hieght attributer
            Rectangle(-2, 3, 0, 2)  # for x attributer
            Rectangle(2, 3, 1, -2)  # for y attribyter


if __name__ == '__main__':
    unittest.main()
