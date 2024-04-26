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

        Rectangle.__init__(self, size, size, x, y, id)

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
        return self.width

    @size.setter
    def size(self, new_size):
        """ setter"""
        self.width = new_size
        self.height = new_size

    def update(self, *args, **kwargs):
        """
           assigns an argument to each attribute
        """
        if args:
            if len(args) >= 1:
                self.id = int(args[0])
            if len(args) >= 2:
                self.width = int(args[1])
                self.height = int(args[1])
            if len(args) >= 3:
                self.x = int(args[2])
            if len(args) >= 4:
                self.y = int(args[3])
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.width = kwargs["size"]
                self.height = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """ returns the dictionary representation of a Square """
        return {
            'id': self.id,
            'size': self.height,
            'x': self.x,
            'y': self.y
            }
