#!/usr/bin/python3
""" Place class for HBnB
    """

from models.base_model import BaseModel


class Place(BaseModel):
    """ Place class for HBnB. Inherits from BaseModel
        """

    city_id = str()
    user_id = str()
    name = str()
    description = str()
    number_rooms = int()
    number_bathrooms = int()
    max_guest = int()
    price_by_night = int()
    latitude = float()
    longitude = float()
    amenity_ids = list()

    def __init__(self, *args, **kwargs):
        """ Init method for place
            """
        super().__init__(*args, **kwargs)
