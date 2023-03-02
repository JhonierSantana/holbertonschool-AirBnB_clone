#!/usr/bin/python3
""" State model of the program.
    """

from models.base_model import BaseModel


class State(BaseModel):
    """ Inherits from BaseModel, used to manage State info.
        """

    name = str()
