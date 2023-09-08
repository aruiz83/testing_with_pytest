import pytest
from app.calculator import Calculator

# exercise_40
# Se utiliza pytest.mark.parametrize para definir varios casos de prueba en una sola función.


@pytest.mark.parametrize("dividend, divisor, expected", [
    (10, 5, 2),
    (0, 5, 0),
    (-10, 5, -2),
])
def test_divide_positive_numbers_and_zero(dividend, divisor, expected):
    calculator = Calculator()
    result = calculator.divide(dividend, divisor)
    assert result == expected


def test_divide_by_zero_should_raise_error():
    calculator = Calculator()
    with pytest.raises(ValueError):
        calculator.divide(10, 0)
