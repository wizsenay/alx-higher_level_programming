#!/usr/bin/python3

"""This modules test the beas modules"""
import unittest
import sys
sys.path.append("/alx-higher_level_programming/0x0C-python-almost_a_circle")

from models.base import Base


class TestBase(unittest.TestCase):
    """ used to test the calss whic called base"""

    def test_id(self):
        user_1 = Base(5)
        user_2 = Base(2)

        id_user_1 = user_1.id
        id_user_2 = user_2.id

        self.assertEqual(id_user_1, 5)
        self.assertEqual(id_user_2, 2)

    def test_none_id(self):
        user_3 = Base()
        user_4 = Base()

        id_user_3 = user_3.id
        id_user_4 = user_4.id
        self.assertEqual(id_user_3, 1)
        self.assertEqual(id_user_4, 2)

if __name__ == '__main__':
    unittest.main()
