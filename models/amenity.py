#!/usr/bin/python3

""" Module that contains the Amenity class """
from models.base_model import BaseModel


class Amenity(BaseModel):
    """ Amenity class """
    name = ""

    def __init__(self, *args, **kwargs):
        """ Constructor """
        super().__init__(*args, **kwargs)
