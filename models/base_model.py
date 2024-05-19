#!/usr/bin/python3
""" BaseModel Class """
from datetime import datetime
from uuid import uuid4
import storage


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
        if len(kwargs) > 0:
            Format = "%Y-%m-%dT%H:%M:%S.%f"
            self.id = kwargs.get('id')
            self.name = kwargs.get('name')
            self.my_number = kwargs.get('my_number')
            c = kwargs.get('created_at')
            self.created_at = datetime.strptime(c, Format)
            c = kwargs.get('updated_at')
            self.updated_at = datetime.strptime(c, Format)
        else:
            self.name = None
            self.my_number = 0
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        if self not in kwargs:
            storage.new(self)

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
        storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of
        __dict__ of the instance
        """
        dic = self.__dict__
        dic["created_at"] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        dic["updated_at"] = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        dic["__class__"] = "BaseModel"
        return dic
