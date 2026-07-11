#!/usr/bin/python3
"""Script"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance."""

        if isinstance(attrs, list):
            all_are_strings = True
            for item in attrs:
                if not isinstance(item, str):
                    all_are_strings = False
                    break
            if all_are_strings:
                filtered_dict = {}
                for attr in attrs:
                    if hasattr(self, attr):
                        filtered_dict[attr] = getattr(self, attr)
                return filtered_dict

        return self.__dict__
