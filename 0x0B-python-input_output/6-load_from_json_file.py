#!/usr/bin/python3

""" this modules used to creates an Object from a “JSON file”
"""

import json


def load_from_json_file(filename):
    """
       prototype
       ---------
       filename: str
        the name of the JSONfile that we went creates an Object by using json
    """
    with open(filename) as f:
        return json.load(f)
