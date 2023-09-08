import pytest
from app.calculator import Calculator

# exercise_66
# Se define una fixture para configurar una instancia de Calculator: calculator_instance


@pytest.fixture
def calculator_instance():
    calculator = Calculator()
    yield calculator
    # Puedes agregar limpieza si es necesario después de que se haya usado la instancia

# Ahora puedes usar la fixture en tus pruebas


def test_calculator_add(calculator_instance):
    result = calculator_instance.add(1, 2)
    assert result == 3


def test_calculator_subtract(calculator_instance):
    result = calculator_instance.subtract(1, 2)
    assert result == -1
