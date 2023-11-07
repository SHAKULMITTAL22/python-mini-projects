import pytest

class InvalidYearError(Exception):
    """Raise when the input year is invalid"""
    pass

def judge_leap_year(year):
    if not isinstance(year, int) or year<= 0:
        raise InvalidYearError("Invalid year")
    if year % 4 != 0:
        return False
    if year % 100 != 0:
        return True
    if year % 400 != 0:
        return False
    return True

def test_judge_leap_year_2000():
    year = 2000
    assert judge_leap_year(year) == True

def test_judge_leap_year_2001():
    year = 2001
    assert judge_leap_year(year) == False

def test_judge_leap_year_2100():
    year = 2100
    assert judge_leap_year(year) == False

def test_judge_leap_year_2400():
    year = 2400
    assert judge_leap_year(year) == True

def test_judge_leap_year_1988():
    year = 1988
    assert judge_leap_year(year) == True

@pytest.mark.parametrize("year", [-1000, 0])   # Edge case scenario 
def test_judge_leap_year_negative_or_zero(year):
    with pytest.raises(InvalidYearError):     # Expect an exception to be thrown
        judge_leap_year(year)

# To run this test un-comment the below lines
"""
def test_judge_leap_year_float():
    year = 2000.0
    with pytest.raises(InvalidYearError): # Expect an exception to be thrown
        judge_leap_year(year)
"""
