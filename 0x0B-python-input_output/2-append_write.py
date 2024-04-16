#!/usr/bin/python3

"""
    writes a string to a text file (UTF8) and returns-
     the number of characters written:
        -> if the file doesn’t exist it will created
        -> if the file does exist it will overwrite
"""


def append_write(filename="", text=""):
    """
       prototype
       ---------
       filename: str
             the name of the file we went to write
       text: str
            the new content we want to write in the file "filename"

       return
       ------
          int
          lentgh of text we write in the file "filename"
    """
    length_write = 0
    with open(filename, 'a', encoding="UTF8") as f:
        length_write = f.write(text)

    f.close()
    return length_write
