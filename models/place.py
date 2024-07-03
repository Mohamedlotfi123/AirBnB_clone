#!/usr/bin/python3
""" Place class """
from models.base_model import BaseModel


class Place(BaseModel):
    """
    Place class

    Attributes:
        class:
            city_id: string - the City id
            user_id: string - the User id
            name: the Place name
            description: the Place description
            number_rooms: rooms number
            number_bathrooms: bathroom number
            max_guest: guest number
            price_by_night: price of the night
            latitude: the latitude
            longitude: the longitude
            amenity_ids: the Amenity ids
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """
        initialization method
        """
        if len(kwargs) == 0:
            super().__init__()
        else:
            super.__init__(**kwargs)
