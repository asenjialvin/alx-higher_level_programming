#!/usr/bin/python3
''' Defines the "Base" of all other classes '''
import json
import csv
import turtle


class Base:
    ''' "Base" of all other classes '''
    __nb_objects = 0

    def __init__(self, id=None):
        ''' Constructor.
            Args:
                id(int): id
        '''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        ''' returns the JSON string representation of list_dictionaries
            Args:
                list_dictionaries(dict): list of dicts
            Return: None if empty or json string
        '''
        if list_dictionaries is not None or list_dictionaries != []:
            return json.dumps(list_dictionaries)
        else:
            return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        ''' writes JSON string representation of list_objs to file
            Args:
                cls(obj): class
                list_objects(list): list of instances who inherits Base
        '''
        filename = "{}.json".format(cls.__name__)
        with open(filename, 'w') as f:
            if list_objs is None:
                f.write([])
            else:
                # to_json_string taks dict as a paramater
                list_of_dicts = []
                for i in list_objs:
                    list_of_dicts.append(i.to_dictionary())
                f.write(Base.to_json_string(list_of_dicts))

    @staticmethod
    def from_json_string(json_string):
        ''' returns the list of the JSON string representation
            Args:
                json(string): string representing a list of dictionaries
            Return: None if empty or list
        '''
        if json_string is not None or json_string != "":
            return json.loads(json_string)
        else:
            return []

    @classmethod
    def create(cls, **dictionary):
        '''return an instance with all attributes already set
            Args:
                dictionary(dict): double pointer to a dictionary
        '''
        if dictionary and dictionary != {}:
            if cls.__name__ == "Square":
                new_obj = cls(3)
            elif cls.__name__ == "Rectangle":
                new_obj = cls(5, 3)
            new_obj.update(**dictionary)
            return new_obj

    @classmethod
    def load_from_file(cls):
        ''' return a list of instances
            Args:
                cls(obj): object
        '''
        filename = "{}.json".format(cls.__name__)
        try:
            with open(filename) as f:
                list_of_dict = Base.from_json_string(f.read())
                return list(map(lambda d: cls.create(**d), list_of_dict))
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        ''' writes csv string representation of list_objs to file
            Args:
                cls(obj): class
                list_objects(list): list of instances who inherits Base
        '''
        filename = "{}.csv".format(cls.__name__)
        with open(filename, 'w', newline='') as csv_f:
            if list_objs is None:
                csv_f.write("[]")
            else:
                if cls.__name__ == "Square":
                    fieldnames = ["id", "size", "x", "y"]
                elif cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                for i in list_objs:
                    (csv.DictWriter(csv_f,
                     fieldnames=fieldnames)).writerow(i.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        ''' return a list of instances
            Args:
                cls(obj): object
        '''
        filename = "{}.csv".format(cls.__name__)
        try:
            with open(filename, newline='') as f:
                if cls.__name__ == "Square":
                    parameter = ["id", "size", "x", "y"]
                elif cls.__name__ == "Rectangle":
                    parameter = ["id", "width", "height", "x", "y"]
                list_of_dict = csv.DictReader(f, fieldnames=parameter)
                list_of_dict = [dict([k, int(v)] for k, v in i.items())
                                for i in list_of_dict]
                return [cls.create(**i) for i in list_of_dict]
        except IOError:
            return []

    def draw(list_rectangles, list_squares):
        ''' opens a window and draws all the Rectangles and Squares
            Args:
                list_rectangle(list): list of rectangles
                list_square(list): list of squares
        '''
        blue_turtle = turtle.Turtle()
        blue_turtle.screen.bgcolor("#27296d")
        blue_turtle.pensize(3)
        blue_turtle.shape("turtle")

        blue_turtle.color("#a393eb")
        for rectangle in list_rectangles:
            blue_turtle.showturtle()
            blue_turtle.up()
            blue_turtle.goto(rectangle.x, rectangle.y)
            blue_turtle.down()
            for i in range(2):
                blue_turtle.forward(rectangle.width)
                blue_turtle.left(90)
                blue_turtle.forward(rectangle.height)
                blue_turtle.left(90)
            blue_turtle.hideturtle()

        blue_turtle.color("#a2c11c")
        for square in list_squares:
            blue_turtle.showturtle()
            blue_turtle.up()
            blue_turtle.goto(square.x, square.y)
            blue_turtle.down()
            for i in range(2):
                blue_turtle.forward(square.width)
                blue_turtle.left(90)
                blue_turtle.forward(square.height)
                blue_turtle.left(90)
            blue_turtle.hideturtle()

        turtle.exitonclick()
