#!/usr/bin/python3
""" State class """
from models.base_model import BaseModel


class State(BaseModel):
    """
    State class

    Attributes:
        class:
            name: name of the state
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
