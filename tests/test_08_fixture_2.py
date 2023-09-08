import os
import pytest
import tempfile
from app.file_reader import FileReader

# exercise_67
# Define una fixture para crear y eliminar el archivo temporal


@pytest.fixture
def temp_file():
    # Crea el archivo temporal
    temp = tempfile.NamedTemporaryFile(mode='w', delete=False)
    temp.write("Hello, world!")
    temp.close()
    yield temp.name  # Proporciona el nombre del archivo al código de prueba
    # Elimina el archivo temporal después de que las pruebas hayan terminado
    os.unlink(temp.name)

# Se puede hacer uso de la fixture en las pruebas


def test_read_file(temp_file):
    reader = FileReader()
    # Lee el contenido del archivo temporal utilizando el método read_file
    result = reader.read_file(temp_file)
    # Comprueba que el contenido del archivo coincida con el valor esperado
    assert result == "Hello, world!"
