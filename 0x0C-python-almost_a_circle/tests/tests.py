
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

if __name__ == "__main__":
    unittest.main()
