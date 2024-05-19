#!/usr/bin/python3
""" FileStorage Class """
from datetime import datetime
import json


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
        dic = obj.__dict__.copy()
        created_at = dic.get("created_at")
        updated_at = dic.get("updated_at")
        dic["created_at"] = created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        dic["updated_at"] = updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        self.__objects[key] = dic

    def save(self):
        """
        function serializes the __objects to JSON file.
        """
        with open(self.__file_path, mode="w+", encoding="utf-8") as f:
            f.write(json.dumps(self.__objects))

    def reload(self):
        """
        function deserializes the JSON file to __objects, but only
        if the JSON file (__file_path)
        """
        try:
            with open(self.__file_path, mode="r", encoding="utf-8") as f:
                json.loads(f.read())
        except Exception:
            pass
