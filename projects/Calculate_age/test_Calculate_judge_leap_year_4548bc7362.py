# test_calculate.py
import pytest
from calculate import judge_leap_year
import time
from calendar import isleap

# Common Year Test
def test_common_year():
    assert not judge_leap_year(2019), "2019 is not a leap year."

# Simple Leap Year Test
def test_simple_leap_year():
    assert judge_leap_year(2020), "2020 is a leap year."

# Century Common Year Test
def test_century_common_year():
    assert not judge_leap_year(1900), "1900 is not a leap year."

# Exceptional Century Leap Year Test
def test_exceptional_century_leap_year():
    assert judge_leap_year(2000), "2000 is a leap year."

# Zero Year Test
def test_zero_year():
    # Historically, there is no year 0, but isleap considers it a leap year.
    assert judge_leap_year(0), "Year 0 is considered a leap year in isleap."

# Negative Year Test
def test_negative_year():
    # The leap year function should handle negative years as well
    assert not judge_leap_year(-100), "Negative years are not leap years in isleap."

# Boundary Year Test
@pytest.mark.parametrize("year, expected", [(1999, False), (2000, True), (2001, False), (1900, False)])
def test_boundary_year(year, expected):
    assert judge_leap_year(year) == expected, f"{year} leap year status is incorrect."

# Current Year Test
def test_current_year():
    current_year = time.localtime().tm_year
    assert judge_leap_year(current_year) == isleap(current_year), f"{current_year} leap year status is incorrect."

# Far Future Year Test
def test_far_future_year():
    assert not judge_leap_year(10000), "Year 10000 is not a leap year."

# Far Past Year Test
def test_far_past_year():
    assert judge_leap_year(400), "Year 400 is a leap year."

# Random Year Test
@pytest.mark.parametrize("year", [1804, 2100, 2200, 2300, 2400])
def test_random_year(year):
    assert judge_leap_year(year) == isleap(year), f"{year} leap year status is incorrect."
