#!/usr/bin/python3
""" FileStorage Class """
from datetime import datetime
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage():
    """
    Class that serializes instances to a JSON file and
    deserializes JSON file to instances.

    Attributes:
        Class:
            __file_path: path to the JSON file "string"
            __objects: will store all objects by <class name>.id "dict"

        Methods:
            all: returns the dictionary __objects.
            new: sets in __objects the obj with the key <obj class name>.id
            save: serializes __objects to the JSON file
            reload: deserialixes the JSON file to __objects
    """
    __file_path = "storage.json"
    __objects = {}

    def all(self):
        """ function returns dictionary __objects. """
        return self.__objects

    def new(self, obj):
        """
        function sets in __objects the obj with
        the key <obj class name>id.

        Args:
            obj: object of a class.
        """
        key = f"{obj.__class__.__name__}.{obj.__dict__['id']}"
        self.__objects[key] = obj

    def save(self):
        """
        function serializes the __objects to JSON file.
        """
        dic = {}
        for key, obj in self.__objects.items():
            dic[key] = obj.to_dict()
        json_string = json.dumps(dic)
        with open(self.__file_path, "w") as f:
            f.write(json_string)

    def reload(self):
        """
        function deserializes the JSON file to __objects, but only
        if the JSON file (__file_path)
        """
        Classes = {
                "BaseModel": BaseModel,
                "User": User,
                "State": State,
                "City": City,
                "Place": Place,
                "Amenity": Amenity,
                "Review": Review
                }
        try:
            with open(self.__file_path) as f:
                json_string = f.read()
            Dict = json.loads(json_string)
            for v in Dict.values():
                for key, Class in Classes.items():
                    if v["__class__"] == key :
                        self.new(Class(**v))
        except Exception:
            pass
