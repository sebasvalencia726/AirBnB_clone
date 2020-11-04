#!/usr/bin/python3
"""State module
"""
from .base_model import BaseModel


class State(BaseModel):
    """class User that inherits from BaseModel

    Args:
        BaseModel (class): parent class

    """
    def __init__(self, *args, **kwargs):
        """Constructor

        Args: Public class attributes.
            name: string - empty string
        """
        super(State, self).__init__(*args, **kwargs)
        self.name = ''
