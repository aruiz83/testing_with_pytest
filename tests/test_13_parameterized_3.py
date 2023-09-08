import pytest
from app.average import average

# exercise_123


@pytest.mark.parametrize(
    "input_list, expected_output",
    [
        ([1, 2, 3], 2),
        ([10, 20, 30, 40], 25),
        ([5], 5),
        ([0, 0, 0], 0),
        ([], None),
        (["not a number"], None),
        (["1", 2, 3], None),
        ([None], None),
    ]
)
def test_average(input_list, expected_output):
    if expected_output is None:
        with pytest.raises((TypeError, ValueError)):
            average(input_list)
    else:
        assert average(input_list) == expected_output
