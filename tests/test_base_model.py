#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    """test for the BaseModel"""

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
        self.assertEqual(model_d["updated_at"], self.model.updated_at.isoformat())
        self.assertEqual(model_d["created_at"], self.model.created_at.isoformat())

if __name__ == '__main__':
    unittest.main()
