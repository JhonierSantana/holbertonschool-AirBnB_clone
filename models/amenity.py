#!/usr/bin/python3
""" Amenity model of the program.
    """

from models.base_model import BaseModel


class Amenity(BaseModel):
    """ Inherits from BaseModel, used to manage Amenity info.
        """
    name = str()
