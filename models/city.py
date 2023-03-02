#!/usr/bin/python3
""" City model of the program.
    """

from models.base_model import BaseModel


class City(BaseModel):
    """ Inherits from BaseModel, used to manage City info.
        """

    state_id = str()
    name = str()

    def __init__(self, *args, **kwars):
        """ Initialize the City class.
            """
        super().__init__(*args, **kwars)
