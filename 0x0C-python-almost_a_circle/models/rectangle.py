#!/usr/bin/python3
"""
A modles contain a rectangele calss
   which used to calculate area and premeter
"""
from models.base import Base


class Rectangle(Base):
    """
       A class used to calculet some mathimathical
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
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if int(width) <= 0:
            raise ValueError("width must be > 0")
        if int(height) <= 0:
            raise ValueError("height must be > 0")
        if int(x) < 0:
            raise ValueError("x must be >= 0")
        if int(y) < 0:
            raise ValueError("y must be >= 0")
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        Base.__init__(self, id)

    @property
    def width(self) -> int:
        """width getter
        """
        return self.__width

    @property
    def height(self) -> int:
        """height getter
        """
        return self.__height

    @property
    def x(self) -> int:
        """x getter
        """
        return self.__x

    @property
    def y(self) -> int:
        """y getter
        """
        return self.__y

    @width.setter
    def width(self, new_width: int):
        """width setter
        """
        if not isinstance(new_width, int):
            raise TypeError("width must be an integer")
        if int(new_width) <= 0:
            raise ValueError("width must be > 0")
        self.__width = new_width

    @height.setter
    def height(self, new_height: int):
        """height setter
        """
        if not isinstance(new_height, int):
            raise TypeError("height must be an integer")
        if int(new_height) <= 0:
            raise ValueError("height must be > 0")
        self.__height = new_height

    @x.setter
    def x(self, new_x: int):
        """x setter
        """
        if not isinstance(new_x, int):
            raise TypeError("x must be an integer")
        if int(new_x) < 0:
            raise ValueError("x must be >= 0")
        self.__x = new_x

    @y.setter
    def y(self, new_y: int):
        """y setter
        """
        if not isinstance(new_y, int):
            raise TypeError("y must be an integer")
        if int(new_y) < 0:
            raise ValueError("y must be >= 0")
        self.__y = new_y

    def area(self):
        """
        returns the area value of the Rectangle instance.
        """
        return self.__width * self.__height
