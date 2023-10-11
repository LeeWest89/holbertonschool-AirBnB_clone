#!/usr/bin/python3
"""
Defines unittests for the Amenity class in models/amenity.py.
"""
import os
import unittest
from time import sleep
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Unittests for testing Amenity class."""

    @classmethod
    def setUpClass(cls):
        """Set up for the tests."""
        cls.amenity = Amenity()
        cls.amenity.save()

    @classmethod
    def tearDownClass(cls):
        """Tear down for the tests."""
        del cls.amenity
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_instantiation(self):
        """Test if Amenity class is correctly created without arguments."""
        self.assertIs(type(self.amenity), Amenity)

    def test_save(self):
        """Test if 'save' method correctly updates 'updated_at' attribute."""
        old_updated_at = self.amenity.updated_at
        sleep(0.1)
        self.amenity.save()
        new_updated_at = self.amenity.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

    def test_to_dict(self):
        """Test if 'to_dict' method returns a dictionary."""
        self.assertIs(type(self.amenity.to_dict()), dict)


if __name__ == "__main__":
    unittest.main()
