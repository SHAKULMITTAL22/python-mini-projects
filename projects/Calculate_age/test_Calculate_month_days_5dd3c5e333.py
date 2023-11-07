# importing necessary libraries
# make sure pytest is installed in your Python environment, if not install via pip install pytest
import pytest
import calculate

def test_month_days_non_leap_year():
    '''
    Test Scenario 1: Validating month days for non-leap years
    '''
    for month in range(1, 13):
        if month in [1, 3, 5, 7, 8, 10, 12]:
            assert calculate.month_days(month, False) == 31
        elif month in [4, 6, 9, 11]:
            assert calculate.month_days(month, False) == 30
        elif month == 2:
            assert calculate.month_days(month, False) == 28


def test_month_days_leap_year():
    '''
    Test Scenario 2: Validating month days for leap years
    '''
    for month in range(1, 13):
        if month in [1, 3, 5, 7, 8, 10, 12]:
            assert calculate.month_days(month, True) == 31
        elif month in [4, 6, 9, 11]:
            assert calculate.month_days(month, True) == 30
        elif month == 2:
            assert calculate.month_days(month, True) == 29


def test_month_days_negative_month():
    '''
    Test Scenario 3: Validating for negative month value
    '''
    with pytest.raises(Exception):
        assert calculate.month_days(-5, True)

    with pytest.raises(Exception):
        assert calculate.month_days(-1, False)


def test_month_days_above_12():
    '''
    Test Scenario 4: Validating for month value more than 12
    '''
    with pytest.raises(Exception):
        assert calculate.month_days(13, True)

    with pytest.raises(Exception):
        assert calculate.month_days(20, False)


def test_month_days_non_integer_month():
    '''
    Test Scenario 5: Validating for non-integer month values
    '''
    with pytest.raises(Exception):
        assert calculate.month_days(5.5, True)
    
    with pytest.raises(Exception):
        assert calculate.month_days("1", False)
        

def test_month_days_non_boolean_years():
    '''
    Test Scenario 6: Check function with leap_year parameter as non-boolean
    '''
    with pytest.raises(Exception):
        assert calculate.month_days(5, "True")
    
    with pytest.raises(Exception):
        assert calculate.month_days(1, 0)
