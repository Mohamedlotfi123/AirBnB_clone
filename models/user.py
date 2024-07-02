#!/usr/bin/python3
""" User Class """
from models.base_model import BaseModel
import models


class User(BaseModel):
    """
    User Class.

    Attribute:
        class:
            email: user email
            password: user password
            first_name: user first name
            last_name: user last name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        if len(kwargs) == 0:
            super().__init__()
        else:
            super().__init__(**kwargs)
