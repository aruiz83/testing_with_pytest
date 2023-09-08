import pytest
from app.rectangle import area, perimeter

# exercise_102

# Proceso inicial emulando subTest:


def test_area():
    test_cases = [
        (1, 5, 5),
        (2, 10, 20),
        (100, 50, 5000)
    ]
    for width, height, expected in test_cases:
        result = area(width, height)
        assert result == expected


def test_perimeter():
    test_cases = [
        (1, 5, 12),
        (2, 10, 24),
        (100, 50, 300)
    ]
    for width, height, expected in test_cases:
        result = perimeter(width, height)
        assert result == expected

# Utlizando parametrize


@pytest.mark.parametrize("width, height, expected_area", [
    (1, 5, 5),
    (2, 10, 20),
    (100, 50, 5000),
])
def test_area(width, height, expected_area):
    result = area(width, height)
    assert result == expected_area


@pytest.mark.parametrize("width, height, expected_perimeter", [
    (1, 5, 12),
    (2, 10, 24),
    (100, 50, 300),
])
def test_perimeter(width, height, expected_perimeter):
    result = perimeter(width, height)
    assert result == expected_perimeter
