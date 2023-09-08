import pytest
from app.calculate_grade import calculate_grade

# exercise_42


def test_valid_input():
    assert calculate_grade([1, 2, 3]) == 2
    assert calculate_grade([8, 8, 8]) == 8
    assert calculate_grade([10, 20, 30]) == 20
    assert calculate_grade([11, 22, 33]) == 22
    assert calculate_grade([100, 0, 50]) == 50
    assert calculate_grade([99, 99, 99]) == 99
    assert pytest.approx(calculate_grade([100, 90, 80, 70]), 0.01) == 85.0


def test_invalid_input():
    with pytest.raises(TypeError, match="Input must be a list"):
        calculate_grade("not_a_list")

    with pytest.raises(ValueError, match="List cannot be empty"):
        calculate_grade([])

    with pytest.raises(TypeError, match="Elements of list must be numbers"):
        calculate_grade([1, "two", 3])

    with pytest.raises(ValueError, match="Elements of list must be between 0 and 100"):
        calculate_grade([101, 50, 75])

    with pytest.raises(ValueError, match="Elements of list must be between 0 and 100"):
        calculate_grade([-5, 90, 110])
