#!/usr/bin/python3
""" Module that contains the User class """

from models.base_model import BaseModel


class User(BaseModel):
    """ User class """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """ Constructor """
        super().__init__(*args, **kwargs)
