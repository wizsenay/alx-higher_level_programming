#!/usr/bin/python3

"""
   this modules conian a class square
   which is an inherits from Rectangle
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
       A class used to somer mathimathics related wit square

       ...
       Attributes
       ----------
       size : int
         the length of the square
       x : int
       y : int
       id : int
         the id of the square
    """

    def __init__(self, size, x=0, y=0, id=None):
        """ initalize the attributers"""

        self.__size = size
        Rectangle.__init__(self, self.__size, self.__size, x, y, id)

    def __str__(self):
        """
        overriding the __str__ method so that
            it returns [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return (
                "[Square] ({}) {}/{} - {}"
                .format(
                   self.id,
                   self.x,
                   self.y,
                   self.width
                   )
                )

    @property
    def size(self):
        """ getter"""
        return self.__size

    @size.setter
    def size(self, new_size):
        """ setter"""
        self.__size = new_size
        self.width = self.__size
        self.height = self.__size
