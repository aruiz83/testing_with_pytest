import pytest
from app.count_text_lines import count_lines

# exercise_41
# Se utiliza pytest.mark.parametrize para definir varios casos de prueba en una sola función.


@pytest.mark.parametrize("filename, expected_lines", [
    ('app/calculator.py', 12),
    ('non_existing_script.py', None),
])
def test_count_lines(filename, expected_lines):
    if expected_lines is None:
        with pytest.raises(FileNotFoundError):
            count_lines(filename)
    else:
        total_lines = count_lines(filename)
        assert total_lines == expected_lines
