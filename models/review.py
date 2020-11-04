#!/usr/bin/python3
"""Review module
"""
from .base_model import BaseModel


class Review(BaseModel):
    """class Review that inherits from BaseModel

    Args:
        BaseModel (class): parent class

    """
    def __init__(self, *args, **kwargs):
        """Constructor

        Args: Public class attributes.
            place_id: string - empty string: it will be the Place.id
            user_id: string - empty string: it will be the User.id
            text: string - empty string

        """
        super(Review, self).__init__(*args, **kwargs)
        self.place_id = ''
        self.user_id = ''
        self.text = ''
