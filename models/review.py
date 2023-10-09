#!/usr/bin/python3
"""Creates a Review class that inherits from BaseModel"""
from .base_model import BaseModel


class Review(BaseModel):

    """Review class that inherits from BaseModel"""
    place_id = ""
    user_id = ""
    text = ""
