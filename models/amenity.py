#!/usr/bin/python3
"""Creates an Amenity class that inherits from BaseModel"""
from .base_model import BaseModel


class Amenity(BaseModel):

    """Amenity class that inherits from BaseModel

    Attributes:
        name (str): name of amenity
    """
    name = ""
