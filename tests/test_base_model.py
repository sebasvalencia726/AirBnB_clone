#!/usr/bin/python3
"""Unittest for BaseModel class([..])
"""
import unittest
import inspect
from models.base_model import BaseModel, __doc__


class TestBaseModel(unittest.TestCase):

    def test_doctstrings(self):
        """Checking docstring for BaseModel class
        """
        self.assertTrue(len(__doc__.strip()) > 0)
        self.assertTrue(len(BaseModel.__doc__.strip()) > 0)
        functions = inspect.getmembers(BaseModel, predicate=inspect.ismethod)
        for name, func in functions:
            self.assertTrue(len(func.__doc__.strip()) > 0)
        functions = inspect.getmembers(BaseModel, predicate=inspect.isfunction)
        for name, func in functions:
            self.assertTrue(len(func.__doc__.strip()) > 0)

    def test_class_type(self):
        """Checking BaseModel class type
        """
        my_model = BaseModel()
        self.assertEqual(str(type(my_model)),
                         "<class 'models.base_model.BaseModel'>")

    def test_type_created_at(self):
        """created at method test type
        """
        my_model = BaseModel()
        self.assertEqual(str(type(my_model.created_at)),
                         "<class 'datetime.datetime'>")


if __name__ == '__main__':
    unittest.main()
