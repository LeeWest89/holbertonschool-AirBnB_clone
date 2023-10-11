#!/usr/bin/python3
"""Creates a Review class that inherits from BaseModel"""
from .base_model import BaseModel


class Review(BaseModel):

    """Review class that inherits from BaseModel

    Attributes:
        place_id (str): place id
        user_id (str): user id
        text (str): text of the review
    """
    place_id = ""
    user_id = ""
    text = ""
