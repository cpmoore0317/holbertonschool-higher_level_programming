#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_positive_integers(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_negative_integers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-1, -3, -4, -2]), -1)

    def test_mixed_integers(self):
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)
        self.assertEqual(max_integer([-1, -3, 0, 2]), 2)

    def test_single_element_list(self):
        self.assertEqual(max_integer([7]), 7)

    def test_duplicate_values(self):
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)

    def test_large_list(self):
        self.assertEqual(max_integer(list(range(1, 10001))), 10000)

if __name__ == '__main__':
    unittest.main()
