#!/usr/bin/python3

"""A modules that returns the list of available
       attributes and methods of an object: """


def lookup(obj):
    """returns the list of available attributes and methods of an object"""
    return (dir(obj))
