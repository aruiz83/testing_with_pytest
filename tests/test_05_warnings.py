import pytest
from app.calculate_salary import calculate_salary

# exercise_50

# valid_inputs = [
#     ([10.0, 15.0, 20.0], [40.0, 30.0, 20.0], 1250.0),
#     ([5.0, 7.5], [40.0, 30.0], 425.0),
# ]

# invalid_inputs = [
#     ([10.0, 15.0, 20.0], [40.0, 30.0], ValueError,
#      "Wages and hours lists must have the same length"),
#     (["10.0", 15.0, 20.0], [40.0, 30.0, 20.0],
#      TypeError, "Wages list must contain numbers"),
#     ([10.0, 15.0, 20.0], [40.0, "30.0", 20.0],
#      TypeError, "Hours list must contain numbers"),
#     ([10.0, 15.0, 20.0], [-40.0, 30.0, 20.0],
#      ValueError, "Hours must be non-negative"),
#     ([-10.0, 15.0, 20.0], [40.0, 30.0, 20.0],
#      ValueError, "Wages must be non-negative"),
# ]


# @pytest.mark.parametrize("wages, hours, expected", valid_inputs)
# def test_calculate_salary_with_valid_input(wages, hours, expected):
#     assert calculate_salary(wages, hours) == expected


# @pytest.mark.parametrize("wages, hours, exception, message", invalid_inputs)
# def test_calculate_salary_with_invalid_input(wages, hours, exception, message):
#     with pytest.raises(exception, match=message):
#         calculate_salary(wages, hours)


def test_calculate_salary_with_zero_total_salary():
    wages = [0.0, 0.0, 0.0]
    hours = [0.0, 0.0, 0.0]
    with pytest.warns(UserWarning, match="Total salary is zero or negative"):
        calculate_salary(wages, hours)
