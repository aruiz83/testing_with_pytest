import pytest
from app.emp import Employee

# exercise_83


def test_email():
    emp = Employee('John', 'Smith', 40, 80000)
    assert emp.email == 'john.smith@mail.com'


@pytest.mark.parametrize("employee, expected_email", [
    (Employee('John', 'Smith', 40, 80000), 'john.smith@mail.com'),
    (Employee('Jane', 'Doe', 35, 75000), 'jane.doe@mail.com'),
    (Employee('Alice', 'Johnson', 45, 90000), 'alice.johnson@mail.com'),
])
def test_many_emails(employee, expected_email):
    assert employee.email == expected_email


@pytest.fixture
def employee_instace():
    return Employee('John', 'Smith', 40, 80000)


def test_one_employee_email(employee_instace):
    emp = employee_instace
    expected_email = 'john.smith@mail.com'
    assert emp.email == expected_email
