import pytest
from datetime import date
from birthDateToCurrentAge import ageCalculator

class Test_BirthDateToCurrentAgeAgeCalculator:

    @pytest.mark.positive
    def test_age_calculation_past_date(self, mocker):
        mocker.patch("birthDateToCurrentAge.date", autospec=True)
        birth_date = date(1990, 6, 15)
        mocker.patch.object(date, "today", return_value=date(2024, 6, 14))
        expected_result = (33, 11, 30)
        assert ageCalculator(birth_date.year, birth_date.month, birth_date.day) == expected_result

    @pytest.mark.positive
    def test_age_calculation_on_birthday(self, mocker):
        mocker.patch("birthDateToCurrentAge.date", autospec=True)
        birth_date = date(1990, 6, 14)
        mocker.patch.object(date, "today", return_value=date(2024, 6, 14))
        expected_result = (34, 0, 0)
        assert ageCalculator(birth_date.year, birth_date.month, birth_date.day) == expected_result

    @pytest.mark.negative
    def test_age_calculation_future_date(self, mocker):
        mocker.patch("birthDateToCurrentAge.date", autospec=True)
        birth_date = date(2030, 6, 14)
        mocker.patch.object(date, "today", return_value=date(2024, 6, 14))
        with pytest.raises(ValueError):
            ageCalculator(birth_date.year, birth_date.month, birth_date.day)

    @pytest.mark.positive
    def test_age_calculation_leap_year(self, mocker):
        mocker.patch("birthDateToCurrentAge.date", autospec=True)
        birth_date = date(2000, 2, 29)
        mocker.patch.object(date, "today", return_value=date(2024, 3, 1))
        expected_result = (24, 0, 1)
        assert ageCalculator(birth_date.year, birth_date.month, birth_date.day) == expected_result

    @pytest.mark.positive
    def test_age_calculation_december_31(self, mocker):
        mocker.patch("birthDateToCurrentAge.date", autospec=True)
        birth_date = date(1999, 12, 31)
        mocker.patch.object(date, "today", return_value=date(2024, 1, 1))
        expected_result = (24, 0, 1)
        assert ageCalculator(birth_date.year, birth_date.month, birth_date.day) == expected_result

    @pytest.mark.positive
    def test_age_calculation_january_1(self, mocker):
        mocker.patch("birthDateToCurrentAge.date", autospec=True)
        birth_date = date(2000, 1, 1)
        mocker.patch.object(date, "today", return_value=date(2024, 1, 1))
        expected_result = (24, 0, 0)
        assert ageCalculator(birth_date.year, birth_date.month, birth_date.day) == expected_result

    @pytest.mark.positive
    def test_age_calculation_last_day_of_month(self, mocker):
        mocker.patch("birthDateToCurrentAge.date", autospec=True)
        birth_date = date(1995, 4, 30)
        mocker.patch.object(date, "today", return_value=date(2024, 5, 1))
        expected_result = (29, 0, 1)
        assert ageCalculator(birth_date.year, birth_date.month, birth_date.day) == expected_result

    @pytest.mark.positive
    def test_age_calculation_first_day_of_month(self, mocker):
        mocker.patch("birthDateToCurrentAge.date", autospec=True)
        birth_date = date(1995, 5, 1)
        mocker.patch.object(date, "today", return_value=date(2024, 5, 1))
        expected_result = (29, 0, 0)
        assert ageCalculator(birth_date.year, birth_date.month, birth_date.day) == expected_result

    @pytest.mark.positive
    def test_age_calculation_infant(self, mocker):
        mocker.patch("birthDateToCurrentAge.date", autospec=True)
        birth_date = date(2023, 8, 10)
        mocker.patch.object(date, "today", return_value=date(2024, 6, 14))
        expected_result = (0, 10, 4)
        assert ageCalculator(birth_date.year, birth_date.month, birth_date.day) == expected_result

    @pytest.mark.positive
    def test_age_calculation_non_leap_year(self, mocker):
        mocker.patch("birthDateToCurrentAge.date", autospec=True)
        birth_date = date(2000, 2, 29)
        mocker.patch.object(date, "today", return_value=date(2023, 3, 1))
        expected_result = (23, 0, 1)
        assert ageCalculator(birth_date.year, birth_date.month, birth_date.day) == expected_result
