#!/usr/bin/python3

"""
   A base class used to give an id and maneageid attribute
        in all your future classes and to avoid duplicating the same code
"""


class Base:
    __nb_objects = 0
    def __init__(self, id=None):
        #__nb_objects = 0
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
