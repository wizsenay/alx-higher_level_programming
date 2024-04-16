#!/usr/bin/python3

""" a modules used to convert any data type to sting foramt(sting type) """

import json


def to_json_string(my_obj):
    """
       prototype
       ---------
       my_obj: Any
         any data type input that want to covert str type

       return
       ------
         str
         the converted text
    """
    return json.dumps(my_obj)
