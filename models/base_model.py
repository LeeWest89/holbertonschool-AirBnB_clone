#!/usr/bin/python3
"""Creates the BaseModel for HBnB"""
import uuid
from datetime import datetime


class BaseModel:
    """Defines all common attributes/methods for other classes:"""

    def __init__(self):
        """Sets up id, create_at, and update_at"""
        self.id = str(uuid.uuid4())
        self.create_at = datetime.now()
        self.update_at = datetime.now()

    def __str__(self):
        """prints class name, self.id, and self.__dict__"""
        return ("[{}] ({}) {}". format(self.__class__.__name__,
                                       self.id, self.__dict__))

    def save(self):
        """updates the public instance attribute updated_at /
          with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """ returns a dictionary containing all keys/values of __dict__"""
        model_d = self.__dict__.copy()
        model_d["__class__"] = self.__class__.__name__
        model_d["created_at"] = self.create_at.isoformat()
        model_d["upadate_at"] = self.create_at.isoformat()
        return (model_d)
