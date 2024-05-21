#!/usr/bin/python3
""" FileStorage Class """
from datetime import datetime
import json
from models.base_model import BaseModel


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
        FileStorage.__objects[key] = obj

    def save(self):
        """
        function serializes the __objects to JSON file.
        """
        Format = "%Y-%m-%dT%H:%M:%S.%f"
        dic = {}
        for key, obj in self.__objects.items():
            self.__objects[key] = obj.to_dict()
        json_string = json.dumps(self.__objects)
        with open(self.__file_path, "w") as f:
            f.write(json_string)

    def reload(self):
        """
        function deserializes the JSON file to __objects, but only
        if the JSON file (__file_path)
        """
        try:
            with open(self.__file_path) as f:
                json_string = f.read()
            dic = json.loads(json_string)
            for k, v in dic.items():
                self.__objects[k] = BaseModel(**v)
        except Exception:
            pass
