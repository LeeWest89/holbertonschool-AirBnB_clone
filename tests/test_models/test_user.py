#!/usr/bin/python3
"""
Defines unittests for the User class in models/user.py.
"""
import os
import unittest
from time import sleep
from models.user import User


class TestUser(unittest.TestCase):
    """Unittests for testing the User class."""

    @classmethod
    def setUpClass(cls):
        """Set up for the tests."""
        cls.user = User()
        cls.user.save()

    @classmethod
    def tearDownClass(cls):
        """Tear down for the tests."""
        del cls.user
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_instantiation(self):
        """Test if User class is correctly created without arguments."""
        self.assertIs(type(self.user), User)

    def test_save(self):
        """Test if 'save' method correctly updates 'updated_at' attribute."""
        old_updated_at = self.user.updated_at
        sleep(0.1)
        self.user.save()
        new_updated_at = self.user.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

    def test_to_dict(self):
        """Test if 'to_dict' method returns a dictionary."""
        self.assertIs(type(self.user.to_dict()), dict)


if __name__ == "__main__":
    unittest.main()
