import pytest
from app.count_text_lines import count_lines

# exercise_41


def test_count_lines_existing_file(tmp_path):
    # Crear un archivo de prueba con contenido
    file_path = tmp_path / "test_file.txt"
    with open(file_path, 'w') as f:
        f.write("Line 1\nLine 2\nLine 3")

    # Llamar a la función y verificar el resultado
    assert count_lines(file_path) == 3


def test_count_lines_non_existing_file():
    with pytest.raises(FileNotFoundError):
        count_lines("non_existing_file.txt")


# @pytest.mark.parametrize("filename, expected_lines", [
#     ('app/calculator.py', 12),
#     ('non_existing_script.py', None),
# ])
# def test_count_lines(filename, expected_lines):
#     if expected_lines is None:
#         with pytest.raises(FileNotFoundError):
#             count_lines(filename)
#     else:
#         total_lines = count_lines(filename)
#         assert total_lines == expected_lines
