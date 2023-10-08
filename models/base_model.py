#!/usr/bin/python3
"""Creates the BaseModel for HBnB"""
import uuid
from models import storage
from datetime import datetime
import time


class BaseModel:
    """Defines all common attributes/methods for other classes:"""

    def __init__(self, *args, **kwargs):
        """Sets up id, created_at, and updated_at"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if not kwargs:
            storage.new(self)

    def __str__(self):
        """prints class name, self.id, and self.__dict__"""
        return ("[{}] ({}) {}". format(self.__class__.__name__,
                                       self.id, self.__dict__))

    def save(self):
        """updates the public instance attribute updated_at /
          with the current datetime"""
        time.sleep(0.1)
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """ returns a dictionary containing all keys/values of __dict__"""
        model_d = self.__dict__.copy()
        model_d["__class__"] = self.__class__.__name__
        model_d["created_at"] = self.created_at.isoformat()
        model_d["updated_at"] = self.updated_at.isoformat()
        return (model_d)
