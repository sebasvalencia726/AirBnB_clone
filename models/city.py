#!/usr/bin/python3
"""City module
"""
from .base_model import BaseModel


class City(BaseModel):
    """class City that inherits from BaseModel

    Args:
        BaseModel (class): parent class

    """
    def __init__(self, *args, **kwargs):
        """Constructor

        Args: Public class attributes.
            state_id: string - empty string: it will be the State.id
            name: string - empty string

        """
        super(City, self).__init__(*args, **kwargs)
        self.state_id = ''
        self.name = ''
