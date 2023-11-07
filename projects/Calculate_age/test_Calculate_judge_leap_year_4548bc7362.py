import unittest
import calculate
from calendar import isleap
import time

class TestJudgeLeapYear(unittest.TestCase):

    def test_judge_leap_year_zero_negative(self):
        self.assertEqual(calculate.judge_leap_year(0), False)
        self.assertEqual(calculate.judge_leap_year(-10), False)

    def test_judge_leap_year_multiple_of_4_not_100(self):
        self.assertEqual(calculate.judge_leap_year(2004), True)
        self.assertEqual(calculate.judge_leap_year(2104), True)

    def test_judge_leap_year_multiple_of_100_not_400(self):
        self.assertEqual(calculate.judge_leap_year(2100), False)
        self.assertEqual(calculate.judge_leap_year(2200), False)

    def test_judge_leap_year_multiple_of_400(self):
        self.assertEqual(calculate.judge_leap_year(2000), True)
        self.assertEqual(calculate.judge_leap_year(2400), True)

    def test_judge_leap_year_not_multiple_of_4(self):
        self.assertEqual(calculate.judge_leap_year(2019), False)
        self.assertEqual(calculate.judge_leap_year(2021), False)
    
    def test_judge_leap_year_large_year(self):
        self.assertEqual(calculate.judge_leap_year(10000), False)
        self.assertEqual(calculate.judge_leap_year(12000), True)

    def test_judge_leap_year_current_year(self):
        current_year = time.localtime(time.time()).tm_year
        self.assertEqual(calculate.judge_leap_year(current_year), isleap(current_year))


if __name__ == '__main__':
    unittest.main()
