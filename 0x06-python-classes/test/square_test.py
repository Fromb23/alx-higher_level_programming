#!/usr/bin/python3

import unittest
from square import Square

class TestSquare(unittest.TestCase):
    def setUp(self):
        self.s = Square(size=5)
    def test_size_setter(self):
        with self.assertRaises(TypeError):
            self.s.size = "not an integer"
    def test_size_getter(self):
        self.s.size = 5
        self.assertEqual(self.s.size, 5)

    def test_if_tuple(self):
        self.assertIsinstance(self.s.position, tuple)
    def test_position_len(self):
        self.assertEqual(len(self.s.position), 2)
    def test_position1_int(self):
        self.assertIsinstance(self.s.position[0], int)
    def test_position2_int(self):
        self.assertIsinstance(self.s.position[1], int)
    def test_position_less_zero(self):
        with self.assertRaises(TypeError):
            self.s.position = (1, -1)

    def test_area(self):
        expected_area = 25
        self.assertEqual(self.s.area(), expected_area)


if __name__ == '__main__':
    unittest.main()
