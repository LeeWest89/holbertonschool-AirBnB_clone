#!/usr/bin/python3
"""
Defines unittests for the Review class in models/review.py.
"""
import os
import unittest
from time import sleep
from models.review import Review


class TestReview(unittest.TestCase):
    """Unittests for testing Review class."""

    @classmethod
    def setUpClass(cls):
        """Set up for the tests."""
        cls.review = Review()
        cls.review.save()

    @classmethod
    def tearDownClass(cls):
        """Tear down for the tests."""
        del cls.review
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_instantiation(self):
        """Test if Review class is correctly created without arguments."""
        self.assertIs(type(self.review), Review)

    def test_save(self):
        """Test if 'save' method correctly updates 'updated_at' attribute."""
        old_updated_at = self.review.updated_at
        sleep(0.1)
        self.review.save()
        new_updated_at = self.review.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

    def test_to_dict(self):
        """Test that 'to_dict' method returns a dictionary."""
        self.assertIs(type(self.review.to_dict()), dict)


if __name__ == "__main__":
    unittest.main()
