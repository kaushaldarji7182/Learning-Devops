#Implement unit tests for a sample function using the unittest framework.

import unittest
from sample import add_numbers  # Import the function from the actual script

class TestMathFunctions(unittest.TestCase):
    
    def test_add_positive_numbers(self):
        """Test adding two positive numbers."""
        self.assertEqual(add_numbers(2, 3), 5)
    
    def test_add_negative_numbers(self):
        """Test adding two negative numbers."""
        self.assertEqual(add_numbers(-2, -3), -5)

    def test_add_mixed_numbers(self):
        """Test adding a positive and a negative number."""
        self.assertEqual(add_numbers(5, -3), 2)

    def test_add_zeros(self):
        """Test adding zero to a number."""
        self.assertEqual(add_numbers(0, 5), 5)
        self.assertEqual(add_numbers(5, 0), 5)
        self.assertEqual(add_numbers(0, 0), 0)

if __name__ == "__main__":
    unittest.main()
