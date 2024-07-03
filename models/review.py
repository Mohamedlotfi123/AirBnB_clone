#!/usr/bin/python3
""" Review class """
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Place class

    Attributes:
        class:
            place_id: id of the place
            user_id: id of the user
            text: comment
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """
        initialization method
        """
        if len(kwargs) == 0:
            super().__init__()
        else:
            super().__init__(**kwargs)
