#!/usr/bin/python3
""" BaseModel Class """

class BaseModel():
    """
    BaseModel class that defines all common attributes/methods
    for other classes.

    Attributes:
        id: unique id "string".
        created_at: current datetime when an instance is created.
        updated_at: current datetime when an instance is updated.
    
    Methods:
        save: Update the public instance attribute updated_at.
        to_dict: Dictionary containing all keys/values of __dict__
                of the instance.
        __str__: Print [<class name>] (<self.id>) <self.__dict__>
    """
