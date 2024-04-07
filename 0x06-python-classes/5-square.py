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
        self.__size = size

    @property
    def size(self):
        """return the value of privet attribut"""
        return self.__size

    @size.setter
    def size(self, value):
        """add a new vale to the privet attribut '__size' """
        if (not isinstance(value, int)):
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ublic instance method: def area(self):
                 that returns the current square area"""
        return (int(self.__size) ** 2)

    def my_print(self):
        """prints in stdout the square with the character #"""
        i = 0
        if self.__size == 0:
            print("\n")
        else:
            while (i < self.__size):
                j = 0
                while(j < self.__size):
                    print("#", end="")
                    j += 1
                print()
                i += 1
