#!/usr/bin/python3
""" unittest for State class """
import unittest
from models.state import State
import os
import models
import datetime


class TestState(unittest.TestCase):
    """
    Testing State
    """
    def test_instance(self):
        """
        test instance
        """
        test1 = State()
        self.assertIsInstance(test1, State)

    def test_permissions(self):
        """
        test permissions
        """
        self.assertTrue(os.access("models/state.py", os.X_OK))
        self.assertTrue(os.access("models/state.py", os.R_OK))
        self.assertTrue(os.access("models/state.py", os.W_OK))
        self.assertTrue(os.access("models/state.py", os.F_OK))

    def test_ids_maker(self):
        """
        test to generate the id
        """
        state1_id = State()
        state2_id = State()
        self.assertNotEqual(state1_id, state2_id)

    def test_docstring_mandatory(self):
        """
        testing if class has correct docstring
        """
        self.assertIsNotNone(models.state.__doc__)
        self.assertIsNotNone(State.__doc__)
