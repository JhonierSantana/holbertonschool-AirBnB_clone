#!/usr/bin/python3
"""
unittest for base model
"""
import unittest
from models.base_model import BaseModel
import os
import models


class BaseModelTest(unittest.TestCase):
    """
    base model is a test that ensures
    that each instance of the BaseModel class has a unique identifier
    """

    def test_ids_maker(self):
        """
        test to generate the id
        create two instances of the BaseModel class
        firstins and seconding
        """

        firstins = BaseModel()
        seconding = BaseModel()
        self.assertNotEqual(firstins, seconding)
        """
        The assertNotEquals() method verifies that 
        firstins and seconding are not equal.
        If firstins and seconding are the same,
        then it means they have the same identifier
        """

    def test_docstring_mandatory(self):
        """
        this method is to make sure that
        docstring have been added to the different 
        important parts of the BaseModel class.
        -------------------------------------------------------------------------
        makes several calls to the assertIsNotNone() method of the self object
        Each call to this method verifies that a docstring is not None.
        """
        self.assertIsNotNone(models.base_model.__doc__)
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_permissions(self):
        """
        test permissions
        It's a test method that checks
        if the base_model.py file has certain permissions
        ---------------------------------------------------
        the file has execute permissions (os.X_OK)
        the file has read permissions (os.R_OK)
        the file has write permissions (os.W_OK
        the file has if the file exists (os.F_OK
        ---------------------------------------------------
        return: test_permissions returns None
        return: If all of these checks pass (os.access() returns True.
        """
        self.assertTrue(os.access("models/base_model.py", os.X_OK))
        self.assertTrue(os.access("models/base_model.py", os.R_OK))
        self.assertTrue(os.access("models/base_model.py", os.W_OK))
        self.assertTrue(os.access("models/base_model.py", os.F_OK))

    def test_instance(self):
        """
        is a test method that checks if an
        instance of the BaseModel class is created correctly.
        -------------------------------------------------------
        an instance of BaseModel called BaseIns is created.
        The assertIsInstance() method is then used to check
        if BaseIns is an instance of the BaseModel class.
        return:the test passes and test_instance returns None.
        """
        BaseIns = BaseModel()
        self.assertIsInstance(BaseIns, BaseModel)

if __name__ == '__main__':
    """
    checks whether the file is running as a stand-alone
    program or has been imported as a module in another file.
    ------------------------------------------------------------
    we use unittest.main(), which executes all the test methods
    defined in the current test class.
    """
    unittest.main()
