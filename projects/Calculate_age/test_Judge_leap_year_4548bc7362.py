import pytest
from calendar import isleap

def judge_leap_year(year):
    # Check year is integer to reject fractional years, and is positive to reject negative years.
    if not isinstance(year, int) or year <= 0:
        raise ValueError("Year must be a positive integer.")

    return isleap(year)

def test_Judge_leap_year_4548bc7362():
    # Test with Leap Year Input
    assert judge_leap_year(2020) == True, f"Expected True, but got {judge_leap_year(2020)}"

    # Test with Non-Leap Year Input
    assert judge_leap_year(2021) == False, f"Expected False, but got {judge_leap_year(2021)}"

    # Test with Edge Case at Turn of the Century
    assert judge_leap_year(1900) == False, f"Expected False, but got {judge_leap_year(1900)}"

    # Test with Leap Year at Turn of the Century
    assert judge_leap_year(2000) == True, f"Expected True, but got {judge_leap_year(2000)}"

    # Test with Negative Year Input
    with pytest.raises(ValueError):
        judge_leap_year(-100)

    # Test with Fractional Year Input
    with pytest.raises(ValueError):
        judge_leap_year(2000.5)

    # Test with a Future Year
    future_year = 2050
    assert judge_leap_year(future_year) == False, f"Expected False, but got {judge_leap_year(future_year)}"

test_Judge_leap_year_4548bc7362()
