#!/usr/bin/python3
''' Module for class Student '''


class Student:
    ''' Defines a student '''
    def __init__(self, first_name, last_name, age):
        ''' Initiates a student
            Args:
                first_name(str): first name
                last_name(str): last name
                age(int): age
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        ''' retrieves a dictionary representaion
            Args:
                attrs: list of strings, only attribute
                names contained in this list must be retrieved
        '''
        if (type(attrs) == list and all(type(i) == str for i in attrs)):
            return {m: getattr(self, m) for m in attrs if hasattr(self, m)}
        return self.__dict__

    def reload_from_json(self, json):
        ''' replaces all atrributes of Student
            Args:
                json(dict): dictionary
        '''
        for key_i, value_i in json.items():
            setattr(self, key_i, value_i)
