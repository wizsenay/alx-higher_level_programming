#!/usr/bin/python3

""" this modules used to writes an Object to a text file,
          using a JSON representation
"""

import json


def save_to_json_file(my_obj, filename):
    """
       prototype
       ---------
        my_obj: any
           any tupe of dat tan retun in to sting and write in the give file
        filename: str
           the name of the file that we went to add a given string
    """
    with open(filename, 'w', encoding="UTF8") as f:
        json.dump(my_obj, f)
    f.close()
