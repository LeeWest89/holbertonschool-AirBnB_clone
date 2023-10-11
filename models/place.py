#!/usr/bin/python3
"""Creates a State class that inherits from BaseModel"""
from .base_model import BaseModel


class Place(BaseModel):
    """Place class that inherits from BaseModel

    Attributes:
        city_id (str): city id
        used_id (str): user id
        name (str): name of the location
        description (str): description of location
        number_rooms (int): number of rooms
        number_bathrooms (int): number of bathrooms
        max_guest (int): maximum number of guest
        price_by_night (int): price by night
        latitude (float): latitude of location
        longitude (float): longitude of location
        amenity_ids (list): list of amenity ids
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
