#!/usr/bin/python3
"""Unit tests for the FileStorage class in models/engine/file_storage.py."""
import os
import unittest
from models.engine.file_storage import FileStorage
from models import storage


class TestFileStorage(unittest.TestCase):
    """Tests for the FileStorage class."""

    @classmethod
    def setUpClass(cls):
        """Rename existing file.json if it exists."""
        if os.path.exists("file.json"):
            os.rename("file.json", "tmp")

    @classmethod
    def tearDownClass(cls):
        """Delete test file.json and rename original file if it was renamed."""
        if os.path.exists("file.json"):
            os.remove("file.json")
        if os.path.exists("tmp"):
            os.rename("tmp", "file.json")

    def setUp(self):
        """Reset FileStorage objects dictionary before each test."""
        FileStorage._FileStorage__objects = {}

    def test_instantiation(self):
        """Test FileStorage instantiation."""
        self.assertIsInstance(FileStorage(), FileStorage)

    def test_all_method(self):
        """Test 'all' method of FileStorage."""
        self.assertIsInstance(storage.all(), dict)


if __name__ == "__main__":
    unittest.main()
