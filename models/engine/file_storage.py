#!/usr/bin/python3
"""This file is our file storage class and methods. Please take a look
around. We had a pleasure building it."""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
    A class that serializes instances to a JSON file and deserializes JSON file
    to instances.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id
        """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path)
        """
        with open(self.__file_path, 'w') as f:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists ; otherwise, do nothing. If the file doesn’t
        exist, no exception should be raised)
        """

        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                for k, v in json.load(f).items():
                    if v['__class__'] == 'BaseModel':
                        self.__objects[k] = BaseModel(**v)
                    elif v['__class__'] == 'User':
                        self.__objects[k] = User(**v)
                    elif v['__class__'] == 'State':
                        self.__objects[k] = State(**v)
                    elif v['__class__'] == 'City':
                        self.__objects[k] = City(**v)
                    elif v['__class__'] == 'Amenity':
                        self.__objects[k] = Amenity(**v)
                    elif v['__class__'] == 'Place':
                        self.__objects[k] = Place(**v)
                    elif v['__class__'] == 'Review':
                        self.__objects[k] = Review(**v)