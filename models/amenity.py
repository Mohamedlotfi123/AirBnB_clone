#!/usr/bin/python3
""" Amenity class """
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity class

    Attributes:
        class:
            name: name of the amenity
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """
        initialization method
        """
        if len(kwargs) == 0:
            super().__init__()
        else:
            super.__init__(**kwargs)
