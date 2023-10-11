#!/usr/bin/python3
"""Creates a City class that inherits from BaseModel"""
from .base_model import BaseModel


class City(BaseModel):

    """City class that inherits from BaseModel

    Attributes:
        state_id (str): id of the state
        name (str): name of city
        """

    state_id = ""
    name = ""
