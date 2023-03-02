#!/usr/bin/python3
""" User Class for HBnB
    """

from models.base_model import BaseModel


class User(BaseModel):
    """ User class - Inherits from BaseModel and used to manage HBnB's users
        """

    email = str()
    password = str()
    first_name = str()
    last_name = str()
