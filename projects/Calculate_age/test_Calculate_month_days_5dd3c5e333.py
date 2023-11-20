# test_calculate.py

import pytest
from calculate import month_days
from calendar import isleap

class TestCalculateMonthDays:
    @pytest.mark.parametrize("month", [1, 3, 5, 7, 8, 10, 12])
    def test_months_with_31_days(self, month):
        assert month_days(month, isleap(2020)) == 31

    @pytest.mark.parametrize("month", [4, 6, 9, 11])
    def test_months_with_30_days(self, month):
        assert month_days(month, isleap(2020)) == 30

    def test_february_in_leap_year(self):
        assert month_days(2, True) == 29

    def test_february_in_non_leap_year(self):
        assert month_days(2, False) == 28

    @pytest.mark.parametrize("month", [0, 13])
    def test_invalid_month_values(self, month):
        # Assuming that month_days should raise a ValueError for invalid months
        # If the actual behavior is different, this test should be adjusted accordingly.
        with pytest.raises(ValueError):
            month_days(month, isleap(2020))

    def test_boundary_values_for_month_input(self):
        assert month_days(1, isleap(2020)) == 31
        assert month_days(12, isleap(2020)) == 31

    @pytest.mark.parametrize("year, expected", [(2024, True), (2100, False), (2000, True)])
    def test_leap_year_boundary(self, year, expected):
        assert month_days(2, isleap(year)) == (29 if expected else 28)

    @pytest.mark.parametrize("month", [1, 3, 4, 5, 6, 7, 8, 9, 10, 11])
    @pytest.mark.parametrize("leap_year", [True, False])
    def test_consistency_for_non_february_months_regardless_of_leap_year(self, month, leap_year):
        expected_days = 31 if month in [1, 3, 5, 7, 8, 10, 12] else 30
        assert month_days(month, leap_year) == expected_days
