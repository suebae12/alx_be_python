# test_simple_calculator.py

import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method with various scenarios."""
        # Test basic addition
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)
        
        # Test with negative numbers
        self.assertEqual(self.calc.add(-5, -3), -8)
        self.assertEqual(self.calc.add(-10, 15), 5)
        
        # Test with large numbers
        self.assertEqual(self.calc.add(1000, 2000), 3000)
        
        # Test with decimal numbers
        self.assertEqual(self.calc.add(3.5, 2.5), 6.0)
        # Use assertAlmostEqual for floating point comparisons
        self.assertAlmostEqual(self.calc.add(0.1, 0.2), 0.3, places=7)

    def test_subtraction(self):
        """Test the subtraction method with various scenarios."""
        # Test basic subtraction
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(1, 1), 0)
        self.assertEqual(self.calc.subtract(0, 0), 0)
        
        # Test with negative numbers
        self.assertEqual(self.calc.subtract(-5, -3), -2)
        self.assertEqual(self.calc.subtract(-10, 5), -15)
        
        # Test when result is negative
        self.assertEqual(self.calc.subtract(3, 5), -2)
        
        # Test with large numbers
        self.assertEqual(self.calc.subtract(1000, 300), 700)
        
        # Test with decimal numbers
        self.assertEqual(self.calc.subtract(5.5, 2.5), 3.0)
        # Use assertAlmostEqual for floating point comparisons
        self.assertAlmostEqual(self.calc.subtract(0.3, 0.1), 0.2, places=7)

    def test_multiplication(self):
        """Test the multiplication method with various scenarios."""
        # Test basic multiplication
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(0, 5), 0)
        self.assertEqual(self.calc.multiply(1, 1), 1)
        
        # Test with negative numbers
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(-2, -3), 6)
        
        # Test with zero
        self.assertEqual(self.calc.multiply(0, 0), 0)
        self.assertEqual(self.calc.multiply(100, 0), 0)
        
        # Test with large numbers
        self.assertEqual(self.calc.multiply(100, 50), 5000)
        
        # Test with decimal numbers
        self.assertEqual(self.calc.multiply(2.5, 3.0), 7.5)
        # Use assertAlmostEqual for floating point comparisons
        self.assertAlmostEqual(self.calc.multiply(0.1, 0.2), 0.02, places=7)

    def test_division(self):
        """Test the division method with normal cases and division by zero."""
        # Test basic division
        self.assertEqual(self.calc.divide(6, 2), 3.0)
        self.assertEqual(self.calc.divide(5, 2), 2.5)
        self.assertEqual(self.calc.divide(0, 5), 0.0)
        
        # Test with negative numbers
        self.assertEqual(self.calc.divide(-6, 2), -3.0)
        self.assertEqual(self.calc.divide(6, -2), -3.0)
        self.assertEqual(self.calc.divide(-6, -2), 3.0)
        
        # Test with decimal numbers
        self.assertEqual(self.calc.divide(5.5, 2.0), 2.75)
        # Use assertAlmostEqual for floating point comparisons
        self.assertAlmostEqual(self.calc.divide(1.0, 3.0), 1/3, places=7)
        
        # Test division by zero returns None
        self.assertIsNone(self.calc.divide(5, 0))
        self.assertIsNone(self.calc.divide(0, 0))
        self.assertIsNone(self.calc.divide(-5, 0))
        
        # Test that division by zero doesn't raise an exception
        try:
            result = self.calc.divide(10, 0)
            self.assertIsNone(result)
        except Exception as e:
            self.fail(f"Division by zero should return None, not raise exception: {e}")

    def test_edge_cases(self):
        """Test edge cases for all operations."""
        # Test with very large numbers
        large_num = 999999999
        self.assertEqual(self.calc.add(large_num, 1), large_num + 1)
        self.assertEqual(self.calc.subtract(large_num, 1), large_num - 1)
        self.assertEqual(self.calc.multiply(large_num, 2), large_num * 2)
        self.assertEqual(self.calc.divide(large_num, 2), large_num / 2)
        
        # Test with very small decimal numbers
        small_num = 0.000001
        self.assertAlmostEqual(self.calc.add(small_num, small_num), small_num * 2, places=7)
        self.assertAlmostEqual(self.calc.multiply(small_num, 2), small_num * 2, places=7)

    def test_identity_properties(self):
        """Test mathematical identity properties."""
        # Addition identity: a + 0 = a
        self.assertEqual(self.calc.add(5, 0), 5)
        self.assertEqual(self.calc.add(-3, 0), -3)
        
        # Multiplication identity: a * 1 = a
        self.assertEqual(self.calc.multiply(5, 1), 5)
        self.assertEqual(self.calc.multiply(-3, 1), -3)
        
        # Division identity: a / 1 = a
        self.assertEqual(self.calc.divide(5, 1), 5.0)
        self.assertEqual(self.calc.divide(-3, 1), -3.0)

if __name__ == '__main__':
    unittest.main() 