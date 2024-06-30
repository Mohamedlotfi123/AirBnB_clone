#!/usr/bin/python3
""" BaseModel Class """
from datetime import datetime
from uuid import uuid4
import models


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
        to_dict: Return dictionary containing all keys/values of __dict__
                of the instance.
        __str__: Print [<class name>] (<self.id>) <self.__dict__>
    """
    def __init__(self, *args, **kwargs):
        """
        initialization method
        """
        Format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == '__class__':
                    continue
                if k == "created_at" or k == "updated_at":
                    v = datetime.strptime(v, Format)
                setattr(self, k, v)
        else:
            models.storage.new(self)

    def __str__(self):
        """
        print [<class name>] (<self.id>) <self.__dict__> when you try
        to print instance of a class
        """
        return f"[BaseModel] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Update the public instance attribute updated_at with
        the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of
        __dict__ of the instance
        """
        dic = self.__dict__.copy()
        dic["created_at"] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        dic["updated_at"] = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        dic["__class__"] = self.__class__.__name__
        return dic
