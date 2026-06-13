#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
import sys
import os

# Inject the parent directory into the system path so Python can find the module
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Defines a suite of test cases for the max_integer function."""

    def test_max_at_end(self):
        """Test with the maximum value at the end of the list."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_at_beginning(self):
        """Test with the maximum value at the beginning of the list."""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_max_in_middle(self):
        """Test with the maximum value inside the middle of the list."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_one_negative(self):
        """Test a list containing a single negative value along positives."""
        self.assertEqual(max_integer([1, -3, 4, 2]), 4)

    def test_all_negative(self):
        """Test a list consisting entirely of negative numbers."""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_single_element(self):
        """Test a list with only a single integer element."""
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        """Test passing an explicitly empty list container."""
        self.assertEqual(max_integer([]), None)

    def test_no_arguments(self):
        """Test invoking the function with completely empty arguments."""
        self.assertEqual(max_integer(), None)


if __name__ == '__main__':
    unittest.main()
