import pytest

from app.reverse_dict import reverse_dict

# exercise_112


@pytest.mark.parametrize("input_dict, expected_output", [
    (
        {"one": 1, "two": 2, "three": 3},
        {1: "one", 2: "two", 3: "three"}
    ),
    (
        {"a": 0, "b": -1, "c": 10},
        {0: "a", -1: "b", 10: "c"}
    ),
    ({}, {}),
    (
        {"one": "1", "two": 2, "three": 3},
        None
    ),
    (
        ["not a dictionary"],
        None
    ),
    (
        {"one": 1, "two": "2", "three": 3},
        None
    ),
    (
        {"one": 1, "two": 2, "three": "3"},
        None
    ),
    (
        {"one": 1, "two": 2, 3: "three"},
        None
    )
])
def test_reverse_dict(input_dict, expected_output):
    if not isinstance(input_dict, dict):
        with pytest.raises(TypeError):
            reverse_dict(input_dict)
    elif not all(isinstance(value, int) for value in input_dict.values()):
        with pytest.raises(ValueError):
            reverse_dict(input_dict)
    else:
        assert reverse_dict(input_dict) == expected_output
