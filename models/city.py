#!/usr/bin/python3

""" Module that contains the City class """
from models.base_model import BaseModel


class City(BaseModel):
    """ City class """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """ Constructor """
        super().__init__(*args, **kwargs)
