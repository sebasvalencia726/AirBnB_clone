#!/usr/bin/python3
""" Module that contains the base class """

import uuid
from datetime import datetime


class BaseModel():
    """
    BaseModel class:
    """

    def __init__(self, *args, **kwargs):
        """
        Constructor
        """
        if kwargs:
            for value[key] in kwargs.items():
                if key == "created_at":
                    self.created_at = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                elif key == "updated_at":
                    self.updated_at = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                else:
                    if key != "__class__":
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """
        This method is a str representation of the class
        """
        message = ("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))
        return message

    def save(self):
        """
        This method updates the public instance attribute updated_at
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        This method creates a new dictionary
        """
        new_dictionary = dict(self.__dict__)
        new_dictionary["created_at"] = self.created_at.isoformat()
        new_dictionary["updated_at"] = self.updated_at.isoformat()
        new_dictionary["__class__"] = self.__class__.__name__
        return (new_dictionary)
