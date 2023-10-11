#!/usr/bin/python3
"""
Defines unittests for the State class in models/state.py.
"""
import os
import unittest
from time import sleep
from models.state import State


class TestState(unittest.TestCase):
    """Unittests for testing the State class."""

    @classmethod
    def setUpClass(cls):
        """Set up for the tests."""
        cls.state = State()
        cls.state.save()

    @classmethod
    def tearDownClass(cls):
        """Tear down for the tests."""
        del cls.state
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_instantiation(self):
        """Test if State class is correctly created without arguments."""
        self.assertIs(type(self.state), State)

    def test_save(self):
        """Test if 'save' method correctly updates 'updated_at' attribute."""
        old_updated_at = self.state.updated_at
        sleep(0.1)
        self.state.save()
        new_updated_at = self.state.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

    def test_to_dict(self):
        """Test if 'to_dict' method returns a dictionary."""
        self.assertIs(type(self.state.to_dict()), dict)


if __name__ == "__main__":
    unittest.main()
