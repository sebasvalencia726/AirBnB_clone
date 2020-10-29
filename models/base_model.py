#!/usr/bin/python3
"""BaseModel module
"""
import uuid


class BaseModel:
    """Base

    Attrs:
        nb_objects (int): private attribute that
        indicates the number of objects.

    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Init method.

        Args:
            id (str):  public instance attribute that identifies the object.

        """
        if id is None:
            BaseModel.__nb_objects += 1
            self.id = BaseModel.__nb_objects
        else:
            self.id = id
