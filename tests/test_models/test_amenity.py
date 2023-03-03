#!/usr/bin/python3
""" unittest for State class """
import unittest
from models.amenity import Amenity
import os
import models


class TestAmenity(unittest.TestCase):
    """
    Testing Amenity
    """
    def test_instance(self):
        """ test instance """
        test1 = Amenity()
        self.assertIsInstance(test1, Amenity)

    def test_permissions(self):
        """
        test permissions
        """
        self.assertTrue(os.access("models/amenity.py", os.X_OK))
        self.assertTrue(os.access("models/amenity.py", os.R_OK))
        self.assertTrue(os.access("models/amenity.py", os.W_OK))
        self.assertTrue(os.access("models/amenity.py", os.F_OK))

    def test_ids_maker(self):
        """ 
        test to generate the id
        create two instances of the BaseModel class
        option1 and option2.
        """
        option1 = Amenity()
        option2 = Amenity()
        self.assertNotEqual(option1, option2)

    def test_docstring_mandatory(self):
        """
        testing if class has correct docstring
        """
        self.assertIsNotNone(models.amenity.__doc__)
        self.assertIsNotNone(Amenity.__doc__)
