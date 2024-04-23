#!/usr/bin/python3

"""This modlus provide a class used to give an id for the instancess"""


class Base:
    """
    A base class used to give id for every instancess
    ...
    Attributes
    ----------
    __nb_objects : int
          assign the new value to the public instance attribute id
    id : int
       The id of the given instance
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        parameters
        ----------
        id : int
           The id of the given instance
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
