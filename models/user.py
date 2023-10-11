#!/usr/bin/python3
"""Creates a User class that inherits from BaseModel."""
from .base_model import BaseModel


class User(BaseModel):
    """User class that inherits from BaseModel

        Attributes:
        email (str): user's email address
        password (str): email password
        first_name (str): user's first name
        last_name (str):: user's last name"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
