#!/usr/bin/python3

"""This modlus provide a class used to give an id for the instancess"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
         returns the list of the JSON string representation json_string
         ...
         paramater
         ---------
         list_dictionaries : list
              the list we went to convetr to string
        """
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
          writes the JSON string representation of list_objs to a file
          The filename is <Class name>.json
          ...
          parameter
          ---------
          cls : calss
          list_objs : list
             it is a list of instances who inherits of Base
        """
        filename = cls.__name__ + ".json"
        if list_objs is None:
            list_objs = []

        with open(filename, mode="w", encoding="utf-8") as f:
            f.write(
                    cls.to_json_string([obj.to_dictionary()
                                        for obj in list_objs])
                    )

    @staticmethod
    def from_json_string(json_string):
        """
         returns the list of the JSON string representation json_string
         ...
         paramater
         ---------
         json_string : list
              the list we went to convetr to string
        """
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Class method that returns an instance with all attributes already set.

        Parameters:
        - cls (type): The class itself.
        - **dictionary (dict): A dictionary containing attribute values.

        Returns:
        - instance: An instance of the class with attributes set
        """
        if cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = cls(1, 1)

        if dummy is not None:
            dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + ".json"
        try:
            with open(filename, mode="r", encoding="utf-8") as f:
                file_content = f.read()
                instance_list = []
                for item in cls.from_json_string(file_content):
                    item = cls.create(**item)
                    instance_list.append(item)
            return instance_list
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Class method to serialize instances to a CSV file.

        Parameters:
        - list_objs (list): A list of instances to be serialized.

        The method writes the serialized data to a CSV file named
        <Class name>.csv using the csv.DictWriter class.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, mode="w", newline="") as f:
            if cls.__name__ == "Rectangle":
                fieldnames = ['id', 'width', 'height', 'x', 'y']
            elif cls.__name__ == "Square":
                fieldnames = ['id', 'size', 'x', 'y']
            else:
                raise ValueError(f"Unsupported class: {cls.__name__}")

            data = [obj.to_dictionary() for obj in list_objs]
            csv_writer = csv.DictWriter(f, fieldnames=fieldnames)

            csv_writer.writeheader()
            csv_writer.writerows(data)

    @classmethod
    def load_from_file_csv(cls):
        """
        Class method to deserialize instances from a CSV file.

        Returns:
        - list: A list of instances deserialized from the CSV file.

        The method reads a CSV file named <Class name>.csv and
        creates instances
        of the class using the create() method with the data from the file.
        If the file is not found, an empty list is returned.
        """

        rectangles = []
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, mode="r", newline="") as f:
                reader = csv.DictReader(f)

                for row in reader:
                    for key in row.keys():
                        row[key] = int(row[key])
                    rectangle = cls.create(**row)
                    rectangles.append(rectangle)
            return rectangles
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        screen = turtle.Screen()
        screen.title("Drawing Rectangles and Squares")
        screen.bgcolor("white")

        # Function to draw a rectangle
        def draw_rectangle(rectangle):
            turtle.penup()
            turtle.goto(rectangle.width / 2, rectangle.height / 2)
            turtle.pendown()
            for _ in range(4):
                turtle.forward(rectangle.width)
                turtle.right(90)

        # Function to draw a square
        def draw_square(square):
            turtle.penup()
            turtle.goto(square.width / 2, square.height / 2)
            turtle.pendown()
            for _ in range(4):
                turtle.forward(square.width)
                turtle.right(90)

        # Draw rectangles
        turtle.color("blue")
        for rectangle in list_rectangles:
            draw_rectangle(rectangle)

        # Draw squares
        turtle.color("red")
        for square in list_squares:
            draw_square(square)

        turtle.done()
