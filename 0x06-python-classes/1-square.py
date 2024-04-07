#!/usr/bin/python3

""" A modules that contains a class Square that defines a square by:
            (based on 0-square.py)

     - Private instance attribute: size
     - Instantiation with size (no type/value verification) """


class Square:
    """ defines a square by:
                    Private instance attribute:
                    size Instantiation with size """

    def __init__(self, size=None):
        """Instantiation with size (no type/value verification)"""
        self.__size = size
