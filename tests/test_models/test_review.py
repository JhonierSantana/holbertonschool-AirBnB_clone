#!/usr/bin/python3
""" unittest for review """
import unittest
from models.review import Review
import os
import models


class TestCity(unittest.TestCase):
    """
    Testing Review
    """
    def test_instance(self):
        """
        test instance
        """
        test1 = Review()
        self.assertIsInstance(test1, Review)

    def test_permissions(self):
        """
        test permissions
        """
        self.assertTrue(os.access("models/review.py", os.X_OK))
        self.assertTrue(os.access("models/review.py", os.R_OK))
        self.assertTrue(os.access("models/review.py", os.W_OK))
        self.assertTrue(os.access("models/review.py", os.F_OK))

    def test_ids_maker(self):
        """
        test to generate unique id
        """
        review1_id = Review()
        review2_id = Review()
        self.assertNotEqual(review1_id, review2_id)

    def test_docstring_mandatory(self):
        """
        testing if class has correct docstring
        """
        self.assertIsNotNone(models.review.__doc__)
        self.assertIsNotNone(Review.__doc__)
