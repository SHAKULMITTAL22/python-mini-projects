# ********RoostGPT********
"""
Test generated by RoostGPT for test python-test using AI Type Open AI and AI Model gpt-4-turbo

ROOST_METHOD_HASH=month_days_1396fdc0ba
ROOST_METHOD_SIG_HASH=month_days_5dd3c5e333

### Scenario 1: Test for months with 31 days
Details:
  TestName: test_months_with_31_days
  Description: Verify that the function returns 31 days for months that typically have 31 days (January, March, May, July, August, October, December).
Execution:
  Arrange: Prepare a list of months that have 31 days.
  Act: Loop through the list, calling `month_days(month, leap_year)` for each month.
  Assert: Check that the function returns 31 for each month.
Validation:
  This test ensures that the function correctly identifies months that have 31 days, which is crucial for accurate date-related calculations in applications.

### Scenario 2: Test for months with 30 days
Details:
  TestName: test_months_with_30_days
  Description: Verify that the function returns 30 days for months that typically have 30 days (April, June, September, November).
Execution:
  Arrange: Prepare a list of months that have 30 days.
  Act: Loop through the list, calling `month_days(month, leap_year)` for each month.
  Assert: Check that the function returns 30 for each month.
Validation:
  This test checks the function's ability to correctly identify months with 30 days, ensuring accurate month-length information for scheduling and planning purposes.

### Scenario 3: Test for February in a leap year
Details:
  TestName: test_february_in_leap_year
  Description: Verify that the function returns 29 days for February when the year is a leap year.
Execution:
  Arrange: Set `leap_year` to True.
  Act: Call `month_days(2, leap_year)`.
  Assert: Check that the function returns 29.
Validation:
  This test is important to confirm that the function correctly handles the special case of February in a leap year, which is essential for any date calculations involving leap years.

### Scenario 4: Test for February in a non-leap year
Details:
  TestName: test_february_in_non_leap_year
  Description: Verify that the function returns 28 days for February when the year is not a leap year.
Execution:
  Arrange: Set `leap_year` to False.
  Act: Call `month_days(2, leap_year)`.
  Assert: Check that the function returns 28.
Validation:
  This test ensures that the function accurately calculates the number of days in February for non-leap years, which is critical for correct date management and functionality across various applications.

### Scenario 5: Test for invalid month number
Details:
  TestName: test_invalid_month_number
  Description: Verify that the function handles an invalid month number gracefully.
Execution:
  Arrange: Provide an invalid month number (e.g., 13 or 0).
  Act: Call `month_days(invalid_month, leap_year)` where `invalid_month` is the invalid month number.
  Assert: Check that the function returns None or raises an appropriate exception.
Validation:
  This test checks the function's robustness in handling erroneous input, ensuring that the function behaves predictably even with incorrect data.

### Scenario 6: Test for edge cases with month boundaries
Details:
  TestName: test_edge_cases_with_month_boundaries
  Description: Verify that the function correctly handles the boundary values of month numbers (1 and 12).
Execution:
  Arrange: Test with the lowest and highest valid month numbers.
  Act: Call `month_days(1, leap_year)` and `month_days(12, leap_year)`.
  Assert: Check that the function returns 31 for both calls.
Validation:
  This test ensures that the function correctly interprets the boundary values for month numbers, which is essential for preventing off-by-one errors and ensuring comprehensive functionality.
"""

# ********RoostGPT********
     def month_days(month, leap_year):
         if month in {1, 3, 5, 7, 8, 10, 12}:
             return 31
         elif month in {4, 6, 9, 11}:
             return 30
         elif month == 2:
             return 29 if leap_year else 28
         else:
             raise ValueError("Invalid month number")
     