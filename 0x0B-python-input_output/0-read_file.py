#!/usr/bin/python3

"""this modules read a file and print to the consule"""


def read_file(filename=""):
    """
        parameters
        ----------
        filename: str
            The name of the file we want to open
    """
    with open(filename, 'r', encoding="UTF8") as f:
        print(f.read(), end="")

    f.close()
