#!/usr/bin/python3
"""Creates a State class that inherits from BaseModel"""
from .base_model import BaseModel


class State(BaseModel):
    """State class that inherits from BaseModel

    Attribute:
        name (str): name of the state
    """

    name = ""
