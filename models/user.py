#!/usr/bin/python3
"""User module
"""
from .base_model import BaseModel


class User(BaseModel):
    """class User that inherits from BaseModel

    Args:
        BaseModel (class): parent class

    """
    def __init__(self, *args, **kwargs):
        """Constructor

        Args: Public class attributes.
            email: string - empty string
            password: string - empty string
            first_name: string - empty string
            last_name: string - empty string
        """
        super(User, self).__init__(*args, **kwargs)
        self.email = ''
        self.password = ''
        self.first_name = ''
        self.last_name = ''
