#!/usr/bin/python3
""" Review model of the program.
    """

from models.base_model import BaseModel


class Review(BaseModel):
    """ Inherits from BaseModel, used to manage Review info.
        """
    place_id = str()
    user_id = str()
    text = str()

    def __init__(self, *args, **kargs):
        """ Initialize the Review class.
            """
        super().__init__(*args, **kargs)
