#!/usr/bin/python3
"""
Defines unittests for the BaseModel class in models/base_model.py.
"""
import unittest
import os
from time import sleep
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Tests for the BaseModel"""

    @classmethod
    def setUp(cls):
        if os.path.exists("file.json"):
            os.rename("file.json", "tmp")

    @classmethod
    def tearDown(cls):
        if os.path.exists("file.json"):
            os.remove("file.json")
        if os.path.exists("tmp"):
            os.rename("tmp", "file.json")

    def test_one_save(self):
        model = BaseModel()
        sleep(0.1)
        first_updated_at = model.updated_at
        model.save()
        self.assertLess(first_updated_at, model.updated_at)

    def test_to_dict_type(self):
        model = BaseModel()
        self.assertIsInstance(model.to_dict(), dict)

    def test_no_args(self):
        """Test for no argument"""
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_save(self):
        """Test the save method"""
        self.model = BaseModel()
        old_updated_at = self.model.updated_at
        self.model.save()
        new_updated_at = self.model.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

    def test_init(self):
        """Test for the init method"""
        self.model = BaseModel()
        self.assertIsInstance(self.model.id, str)
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_str(self):
        """Test for the string method"""
        self.model = BaseModel()
        str_model = str(self.model)
        self.assertIn(self.model.id, str_model)
        self.assertIn(str(self.model.__dict__), str_model)
        self.assertIn(self.model.__class__.__name__, str_model)

    def test_to_dict(self):
        """Test for making a dictionary"""
        self.model = BaseModel()
        model_d = self.model.to_dict()
        self.assertIsInstance(model_d, dict)
        self.assertEqual(model_d["__class__"], "BaseModel")
        self.assertEqual(model_d["updated_at"],
                         self.model.updated_at.isoformat())
        self.assertEqual(model_d["created_at"],
                         self.model.created_at.isoformat())

    def test_unique_id(self):
        """Tests that each BaseModel instance has a unique id"""
        model1 = BaseModel()
        model2 = BaseModel()
        self.assertNotEqual(model1.id, model2.id)

    def test_id_str(self):
        """Tests that the id attribute is a string, and therefore public"""
        model = BaseModel()
        self.assertIsInstance(model.id, str)


if __name__ == '__main__':
    unittest.main()
