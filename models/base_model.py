#!/usr/bin/python3
"""This file holds all of the methods that create the BaseModel for our HBnB
 Project."""
import uuid
import models
from datetime import datetime


class BaseModel:
    """Defines all common attributes/methods for other classes:"""

    def __init__(self, *args, **kwargs):
        """Sets up id, created_at, and updated_at"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key,
                            datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                elif key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """prints class name, self.id, and self.__dict__"""
        return ("[{}] ({}) {}". format(self.__class__.__name__,
                                       self.id, self.__dict__))

    def save(self):
        """updates the public instance attribute updated_at /
        with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ returns a dictionary containing all keys/values of __dict__"""
        model_d = self.__dict__.copy()
        model_d["__class__"] = self.__class__.__name__
        model_d["created_at"] = self.created_at.isoformat()
        model_d["updated_at"] = self.updated_at.isoformat()
        return (model_d)
