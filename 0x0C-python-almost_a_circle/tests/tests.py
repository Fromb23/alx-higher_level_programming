
#!/usr/bin/python3

import unittest
import json
import os
from models.base import Base

class TestBase(unittest.TestCase):
    def test_init_with_id(self):
        b1 = Base(10)
        self.assertEqual(b1.id, 10)

    def test_init_without_id(self):
        b2 = Base()
        self.assertTrue(hasattr(b2, 'id'))

    def test_to_json_string_empty(self):
        self.assertEqual(Base.to_json_string([]), '[]')

class TestSaveToFile(unittest.TestCase):
    """Test cases for the save_to_file method."""

    def test_save_empty_list(self):
        """Test saving an empty list of objects."""
        Base.save_to_file([])
        self.assertFalse(os.path.exists("Base.json"))

    def test_save_single_object(self):
        """Test saving a single object to a file."""
        obj = Base(1)
        Base.save_to_file([obj])
        self.assertTrue(os.path.exists("Base.json"))

    def test_save_multiple_objects(self):
        """Test saving multiple objects to a file."""
        objs = [Base(1), Base(2), Base(3)]
        Base.save_to_file(objs)
        self.assertTrue(os.path.exists("Base.json"))

    def test_save_none(self):
        """Test saving when list_objs is None."""
        Base.save_to_file(None)
        self.assertFalse(os.path.exists("Base.json"))

if __name__ == "__main__":
    unittest.main()
