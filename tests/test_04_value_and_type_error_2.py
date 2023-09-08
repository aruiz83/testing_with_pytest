import pytest
from app.calculate_shipping_cost import calculate_shipping_cost

# exercise_48


@pytest.mark.parametrize(
    "weight, destination, expected",
    [
        (5, "USA", 0),
        (10, "Canada", 15.0),
        (10, "Mexico", 20.0),
        (10, "Australia", 50.0),
    ],
)
def test_calculate_shipping_cost(weight, destination, expected):
    assert calculate_shipping_cost(weight, destination) == expected


@pytest.mark.parametrize(
    "weight, destination, error_type, error_message",
    [
        ("5kg", "USA", TypeError, "Weight must be a number"),
        (-10, "USA", ValueError, "Weight must be greater than zero"),
        (10, True, TypeError, "Destination must be a string"),
        (10, "", ValueError, "Destination cannot be empty"),
    ],
)
def test_calculate_shipping_cost_exceptions(weight, destination, error_type, error_message):
    with pytest.raises(error_type, match=error_message):
        calculate_shipping_cost(weight, destination)
