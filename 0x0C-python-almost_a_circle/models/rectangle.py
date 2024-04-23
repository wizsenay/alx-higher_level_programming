#!/usr/bin/python3

"""
   A modles contain a rectangele calss which used to calculate area and premeter
"""

from base import Base


class Rectangle(Base):
    """A rectangele class"""
    def __init__(self, width=0, height=0, x=0, y=0, id=None):
        """initalized attributers"""
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        Base.__init__(self, id)

    @property
    def width(self):
        return self.__width
    @property
    def height(self):
        return self.__height
    @property
    def x(self):
        return self.__x
    @property
    def y(self):
        return self.__y


    @width.setter
    def width(self, new_width):
        self.__width = new_width

    @height.setter
    def height(self, new_height):
        self.__height = new_height

    @x.setter
    def x(self, new_x):
        self.__x = new_x

    @y.setter
    def y(self, new_y):
        self.__y = new_y
