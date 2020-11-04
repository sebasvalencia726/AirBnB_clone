#!/usr/bin/python3
"""Amenity module
"""
from .base_model import BaseModel


class Amenity(BaseModel):
    """class Amenity that inherits from BaseModel

    Args:
        BaseModel (class): parent class

    """
    def __init__(self, *args, **kwargs):
        """Constructor

        Args: Public class attributes.
            name: string - empty string

        """
        super(Amenity, self).__init__(*args, **kwargs)
        self.name = ''
