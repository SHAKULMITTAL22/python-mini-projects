"""
TEST CASE:
"""

import unittest
import calculate

class TestCalculateMethods(unittest.TestCase):

    def test_31_days_month(self):
        result = calculate.month_days(1, True)
        self.assertEqual(result, 31)

    def test_30_days_month(self):
        result = calculate.month_days(4, True)
        self.assertEqual(result, 30)

    def test_february_non_leap_year(self):
        result = calculate.month_days(2, False)
        self.assertEqual(result, 28)

    def test_february_leap_year(self):
        result = calculate.month_days(2, True)
        self.assertEqual(result, 29)

    def test_invalid_month_input(self):
        with self.assertRaises(ValueError):
            calculate.month_days(13, False)
        
    def test_non_integer_month_input(self):
        with self.assertRaises(TypeError):
            calculate.month_days("Jan", True)

    def test_non_boolean_year_input(self):
        with self.assertRaises(TypeError):
            calculate.month_days(2, "2020")

    def test_no_input_parameters(self):
        with self.assertRaises(TypeError):
            calculate.month_days()

    def test_additional_invalid_inputs(self):
        with self.assertRaises(ValueError):
            calculate.month_days(0, True)
        
        with self.assertRaises(ValueError):
            calculate.month_days(-1, True)

        with self.assertRaises(TypeError):
            calculate.month_days(True, True)

if __name__ == '__main__':
    unittest.main(verbosity=2)
