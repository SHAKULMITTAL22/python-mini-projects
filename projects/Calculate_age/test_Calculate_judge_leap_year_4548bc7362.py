import unittest
from calendar import isleap

# Define the CalculateYear class with a staticmethod judge_leap_year
class CalculateYear:
    @staticmethod
    def judge_leap_year(year):
        return isleap(year)

class TestCalculateYear(unittest.TestCase):
    def test_leap_year_divisible_by_4(self):
        self.assertTrue(CalculateYear.judge_leap_year(2020))

    def test_year_not_divisible_by_4(self):
        self.assertFalse(CalculateYear.judge_leap_year(2021))

    def test_year_divisible_by_100_not_400(self):
        self.assertFalse(CalculateYear.judge_leap_year(1900))
        
    def test_year_divisible_by_100_and_400(self):
        self.assertTrue(CalculateYear.judge_leap_year(2000))

    def test_negative_year(self):
        with self.assertRaises(ValueError):  # assuming isleap() raises ValueError for negative years
            CalculateYear.judge_leap_year(-2020)

    def test_float_year(self):
        with self.assertRaises(TypeError):  # assuming isleap() raises TypeError for float years
            CalculateYear.judge_leap_year(2020.5)

    def test_non_integer_non_float_year(self):
        with self.assertRaises(TypeError):  # assuming isleap() raises TypeError for non-integer, non-float years
            CalculateYear.judge_leap_year("2020")

    def test_year_zero(self):
        self.assertFalse(CalculateYear.judge_leap_year(0))  # assuming isleap() returns False for year 0

    def test_no_parameters(self):
        with self.assertRaises(TypeError):  # assuming isleap() raises TypeError when no arguments are provided
            CalculateYear.judge_leap_year()

if __name__ == '__main__':
    unittest.main(verbosity=3)
