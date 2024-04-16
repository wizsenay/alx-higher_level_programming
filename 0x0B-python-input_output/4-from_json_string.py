#!/usr/bin/python3

""" a modules used to convert JSON string format to its orignal data type"""

import json


def from_json_string(my_str):
    """
       prototype
       ---------
       my_str: str
         a str format represent by JSON

       return
       ------
         any
         an object (Python data structure) represented by a JSON string
    """
    return json.loads(my_str)
