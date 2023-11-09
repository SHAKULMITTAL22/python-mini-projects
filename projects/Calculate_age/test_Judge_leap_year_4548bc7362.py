import time
import pytest

def judge_leap_year(year: int) -> bool:
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

def test_Judge_leap_year_4548bc7362():
    # Scenario 1: year is a leap year
    assert judge_leap_year(2020) == True, "2020 is a leap year"
    
    # Scenario 2: year is not a leap year
    assert judge_leap_year(2021) == False, "2021 is not a leap year"

    # Scenario 3: year is the current year
    current_year = time.localtime().tm_year
    if judge_leap_year(current_year):
        assert judge_leap_year(current_year) == True, f"{current_year} is a leap year"
    else:
        assert judge_leap_year(current_year) == False, f"{current_year} is not a leap year"

    # Scenario 4: year is minimum possible year(1)
    assert judge_leap_year(1) == False, "1 is not a leap year"

    # Scenario 5: year is maximum possible year (9999)
    assert judge_leap_year(9999) == False, "9999 is not a leap year"
    
    # Scenario 6: year is a leap year according to the Gregorian calendar
    assert judge_leap_year(2000) == True, "2000 is a leap year according to the Gregorian calendar"
    
    # Scenario 7: year is divisible by 100 but not 400.
    assert judge_leap_year(1900) == False, "1900 is not a leap year as it is divisible by 100 but not 400"
