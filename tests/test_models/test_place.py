#!/usr/bin/python3
"""
Defines unittests for the Place class in models/place.py.
"""
import os
import unittest
from time import sleep
from models.place import Place


class TestPlace(unittest.TestCase):
    """Unittests for testing Place class."""

    @classmethod
    def setUpClass(cls):
        """Set up for the tests."""
        cls.place = Place()
        cls.place.save()

    @classmethod
    def tearDownClass(cls):
        """Tear down for the tests."""
        del cls.place
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_instantiation(self):
        """Test if Place class is correctly created without arguments."""
        self.assertIs(type(self.place), Place)

    def test_save(self):
        """Test if 'save' method correctly updates 'updated_at' attribute."""
        old_updated_at = self.place.updated_at
        sleep(0.1)
        self.place.save()
        new_updated_at = self.place.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

    def test_to_dict(self):
        """Test that 'to_dict' method returns a dictionary."""
        self.assertIs(type(self.place.to_dict()), dict)


if __name__ == "__main__":
    unittest.main()
