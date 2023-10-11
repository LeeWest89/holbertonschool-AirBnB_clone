#!/usr/bin/python3
"""
Defines unittests for the City class in models/city.py.
"""
import os
import unittest
from time import sleep
from models.city import City


class TestCity(unittest.TestCase):
    """Unittests for testing City class."""

    @classmethod
    def setUpClass(cls):
        """Set up for the tests."""
        cls.city = City()
        cls.city.save()

    @classmethod
    def tearDownClass(cls):
        """Tear down for the tests."""
        del cls.city
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_instantiation(self):
        """Test if City class is correctly created without arguments."""
        self.assertIs(type(self.city), City)

    def test_save(self):
        """Test if 'save' method correctly updates 'updated_at' attribute."""
        old_updated_at = self.city.updated_at
        sleep(0.1)
        self.city.save()
        new_updated_at = self.city.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

    def test_to_dict(self):
        """Test that 'to_dict' method returns a dictionary."""
        self.assertIs(type(self.city.to_dict()), dict)


if __name__ == "__main__":
    unittest.main()
