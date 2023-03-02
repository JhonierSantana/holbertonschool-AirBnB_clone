#!/usr/bin/python3
""" unittest for State class """
import unittest
from models.city import City
import os
import models


class TestCity(unittest.TestCase):
    """ Testing City """
    def test_instance(self):
        """ test instance """
        test1 = City()
        self.assertIsInstance(test1, City)

    def test_permissions(self):
        """ test permissions """
        self.assertTrue(os.access("models/city.py", os.X_OK))
        self.assertTrue(os.access("models/city.py", os.R_OK))
        self.assertTrue(os.access("models/city.py", os.W_OK))
        self.assertTrue(os.access("models/city.py", os.F_OK))

    def test_ids_maker(self):
        """ test to generate unique id """
        city1_id = City()
        city2_id = City()
        self.assertNotEqual(city1_id, city2_id)

    def test_docstring_mandatory(self):
        """ testing if class has correct docstring """
        self.assertIsNotNone(models.city.__doc__)
        self.assertIsNotNone(City.__doc__)
