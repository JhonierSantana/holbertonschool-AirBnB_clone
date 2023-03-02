#!/usr/bin/python3
""" City model of the program.
    """

from models.base_model import BaseModel


class City(BaseModel):
    """ Inherits from BaseModel, used to manage City info.
        """

    state_id = str()
    name = str()
