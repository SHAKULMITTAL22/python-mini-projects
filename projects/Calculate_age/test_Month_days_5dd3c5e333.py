import pytest
from unittest.mock import patch
from calendar import isleap, monthrange
import time

def judge_leap_year(year):
    return isleap(year)

def month_days(month, leap_year):
    if month == 2:
        if leap_year:
            return 29
        else:
            return 28
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 31

@patch('builtins.input', side_effect=["John Doe", "1992"])
@patch('time.localtime', return_value=time.struct_time((2022, 7, 26, 0, 0, 0, 0, 0, 0)))
def test(test_input, mock_time):
    name, start_year = test_input.side_effect
    start_year = int(start_year)
    localtime = mock_time.return_value
    current_year = localtime.tm_year
    year = current_year - start_year

    # Test Age Calculation
    assert year == 30

    # Test Leap Year Logic
    assert judge_leap_year(2000)
    assert not judge_leap_year(1900)
    assert judge_leap_year(2004)
    assert not judge_leap_year(2005)

    # Test Month Days
    assert month_days(2, True) == 29
    assert month_days(2, False) == 28

    for m in [4, 6, 9, 11]:
        assert month_days(m, True) == 30
        assert month_days(m, False) == 30

    for m in [1, 3, 5, 7, 8, 10, 12]:
        assert month_days(m, True) == 31
        assert month_days(m, False) == 31

    # Test Days Calculation for Years
    day = 0
    for y in range(start_year, start_year + year):
        if (judge_leap_year(y)):
            day += 366
        else:
            day += 365
    assert day == 10957

    # Test Days Calculation for Current Year
    leap_year = judge_leap_year(localtime.tm_year)
    for m in range(1, localtime.tm_mon):
        day += month_days(m, leap_year)
    day += localtime.tm_mday
    assert day == 11022

    # Test Final Result
    month = year * 12 + localtime.tm_mon
    assert year == 30
    assert month == 367
    assert day == 11022
