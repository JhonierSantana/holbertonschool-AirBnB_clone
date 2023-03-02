#!/usr/bin/python3
""" unittest for State class """
import unittest
from models.user import User
import os
import models


class TestCity(unittest.TestCase):
    """ Testing User """
    def test_instance(self):
        """ test instance """
        test1 = User()
        self.assertIsInstance(test1, User)

    def test_permissions(self):
        """ test permissions """
        self.assertTrue(os.access("models/user.py", os.X_OK))
        self.assertTrue(os.access("models/user.py", os.R_OK))
        self.assertTrue(os.access("models/user.py", os.W_OK))
        self.assertTrue(os.access("models/user.py", os.F_OK))

    def test_ids_maker(self):
        """ test to generate unique id """
        user1_id = User()
        user2_id = User()
        self.assertNotEqual(user1_id, user2_id)

    def test_docstring_mandatory(self):
        """ testing if class has correct docstring """
        self.assertIsNotNone(models.user.__doc__)
        self.assertIsNotNone(User.__doc__)
