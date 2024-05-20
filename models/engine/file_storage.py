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
        return FileStorage.__objects

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
        objd = FileStorage.__objects
        objdict = {obj: objd[obj].to_dict() for obj in objd.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        """
        function deserializes the JSON file to __objects, but only
        if the JSON file (__file_path)
        """
        try:
            with open(Filestorage.__file_path) as f:
                dic = json.loads(f)
                for obj in dic.values():
                    cls_name = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(cls_name)(**obj))
        except Exception:
            pass
