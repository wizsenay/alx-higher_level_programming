#!/usr/bin/python3
"""A modles contain a rectangele calss
   which used to calculate area and premeter
"""

from base import Base


class Rectangle(Base):
    """A class used to calculet some mathimathical
                  opreation related with rectangle
       ...
       Attributes
       ----------
       width : int
          the width of the rectangle
       height : int
          the hight(lenght) of the rectanglre
       x : int
       y : int

       Methods
       -------
       width(), height(), y(), x()
         getter functions return the value of private attributers
       width(new_width), height(new_height), y(new_y), x(new_x)
         setter finctions return set a value to the private attrinuters
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        parameters
        ----------
        width : int
           the width of the rectangle
        height : int
           the hight(lenght) of the rectanglre
        id : int
           the id of the instance
        x : int
        y : int
        """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        Base.__init__(self, id)

    @property
    def width(self):
        """width getter
        """
        return self.__width

    @property
    def height(self):
        """height getter
        """
        return self.__height

    @property
    def x(self):
        """x getter
        """
        return self.__x

    @property
    def y(self):
        """y getter
        """
        return self.__y

    @width.setter
    def width(self, new_width):
        """width setter
        """
        self.__width = new_width

    @height.setter
    def height(self, new_height):
        """height setter
        """
        self.__height = new_height

    @x.setter
    def x(self, new_x):
        """x setter
        """
        self.__x = new_x

    @y.setter
    def y(self, new_y):
        """y setter
        """
        self.__y = new_y
