#!/usr/bin/python3
""" FileStorage Class """
import JSON


class FileStorage(BaseModel):
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
    __file_path = "root/alx/AirBnB_clone/models/engine/storage.json"
    _objects = {}

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
        self.__objects[obj] = f"{obj.__class__.__name__}.{obj.id}"

    def save(self):
        """
        function serializes the __objects to JSON file.
        """
        with open(self.__file_path, "a") as f:
            f.write(json.dumps(self.__objects) + "\n")

    def reload(self):
        """
        function deserializes the JSON file to __objects, but only
        if the JSON file (__file_path)
        """
        try:
            with open(self.__file_path) as f:
                json.loads(f.read())
        except Exception:
            pass
