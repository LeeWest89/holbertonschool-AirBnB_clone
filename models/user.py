#!/usr/bin/python3
"""Creates a User class that inherits from BaseModel."""
from .base_model import BaseModel


class User(BaseModel):
    """User class that inherits from BaseModel"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
