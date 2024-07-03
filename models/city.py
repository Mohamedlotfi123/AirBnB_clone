#!/usr/bin/python3
""" City class """
from models.base_model import BaseModel


class City(BaseModel):
    """
    City class

    Attributes:
        class:
            state_id: id of the state
            name: name of the city
    """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """
        initialization method
        """
        if len(kwargs) == 0:
            super().__init__()
        else:
            super.__init__(**kwargs)
