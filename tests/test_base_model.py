#!/usr/bin/python3
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def test_save(self):
        """Test the save method"""
        model = BaseModel()
        old_updated_at = model.updated_at
        model.save()
        new_updated_at = model.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

if __name__ == '__main__':
    unittest.main()