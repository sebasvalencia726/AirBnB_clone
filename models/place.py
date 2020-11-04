#!/usr/bin/python3
"""Place module
"""
from .base_model import BaseModel


class Place(BaseModel):
    """class Amenity that inherits from BaseModel

    Args:
        BaseModel (class): parent class

    """
    def __init__(self, *args, **kwargs):
        """Constructor

        Args: Public class attributes.
            city_id: string - empty string: it will be the City.id
            user_id: string - empty string: it will be the User.id
            name: string - empty string
            description: string - empty string
            number_rooms: integer - 0
            number_bathrooms: integer - 0
            max_guest: integer - 0
            price_by_night: integer - 0
            latitude: float - 0.0
            longitude: float - 0.0
            amenity_ids: list of string - empty list: it will be the list of Amenity.id later

        """
        super(Place, self).__init__(*args, **kwargs)
        self.city_id = ''
        self.user_id = ''
        self.name = ''
        self.description = ''
        self.number_rooms = 0
        self.number_bathrooms = 0
        self.max_guest = 0
        self.price_by_night = 0
        self.latitude = 0.0
        self.longitude = 0.0
        self.amenity_ids = []
