#!/usr/bin/python3

""" A modules that contains a class Square that defines a square by:
            (based on 0-square.py)

     - Private instance attribute: size
     - Instantiation with size (no type/value verification) """


class Square:
    """ defines a square by:
                    Private instance attribute:
                    size Instantiation with size """

    def __init__(self, size=0):
        """Instantiation with size (int)"""
        if (not isinstance(size, int)):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
