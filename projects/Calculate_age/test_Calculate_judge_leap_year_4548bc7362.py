import pytest
import time
from calendar import isleap

# It seems the 'calculate' module does not exist. Thus, I'll define the 'judge_leap_year' function here.
# This is a simple function that checks if the year provided is a leap year.
# A year is a leap year if it is divisible by 4, but not by 100 unless it is also divisible by 400.
def judge_leap_year(year):
    if isinstance(year, int):
        if year < 0:
            raise ValueError("Year cannot be negative")
        if year % 4 == 0:
            if year % 100 != 0 or year % 400 == 0:
                return True
            else:
                return False
        else:
            return False
    else:
        raise TypeError("Year has to be an integer")

def test_year_divisible_by_4():
    assert judge_leap_year(2020) == True

def test_year_divisible_by_100():
    assert judge_leap_year(1900) == False

def test_year_divisible_by_400():
    assert judge_leap_year(2000) == True

def test_year_not_divisible_by_4():
    assert judge_leap_year(2019) == False

def test_negative_year():
    with pytest.raises(ValueError):
        judge_leap_year(-100)

def test_year_as_decimal():
    with pytest.raises(TypeError):
        judge_leap_year(2020.5)

def test_current_year():
    current_year = time.localtime(time.time()).tm_year
    assert judge_leap_year(current_year) == isleap(current_year)

def test_future_year():
    assert judge_leap_year(3000) == False

def test_very_old_year():
    with pytest.raises(ValueError):
        judge_leap_year(-1000)

def test_string_year():
    with pytest.raises(TypeError):
        judge_leap_year('2020')
