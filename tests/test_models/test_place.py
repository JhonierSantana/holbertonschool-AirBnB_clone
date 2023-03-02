#!/usr/bin/python3
""" unittest for State place """
import unittest
from models.place import Place
import os
import models


class TestPlace(unittest.TestCase):
    """ Testing Place """
    def test_instance(self):
        """ test instance """
        test1 = Place()
        self.assertIsInstance(test1, Place)

    def test_permissions(self):
        """ test permissions """
        self.assertTrue(os.access("models/place.py", os.X_OK))
        self.assertTrue(os.access("models/place.py", os.R_OK))
        self.assertTrue(os.access("models/place.py", os.W_OK))
        self.assertTrue(os.access("models/place.py", os.F_OK))

    def test_ids_maker(self):
        """ test to generate unique id """
        place1_id = Place()
        place2_id = Place()
        self.assertNotEqual(place1_id, place2_id)

    def test_docstring_mandatory(self):
        """ testing if class has correct docstring """
        self.assertIsNotNone(models.place.__doc__)
        self.assertIsNotNone(Place.__doc__)
