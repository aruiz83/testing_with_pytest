import pytest
from app.generate_password import Utils

# exercise_77


@pytest.fixture
def utils_instace():
    return Utils()


def test_generate_password(utils_instace):
    result = utils_instace.generate_password(10)
    assert len(result) == 10
    assert any(c.isupper() for c in result)
    assert any(c.islower() for c in result)
    assert any(c.isdigit() for c in result)


# Define diferentes valores de 'n' para probar
@pytest.mark.parametrize("n", [8, 12, 18])
def test_generate_password_len(utils_instace, n):
    result = utils_instace.generate_password(n)
    assert len(result) == n
    assert any(c.isupper() for c in result)
    assert any(c.islower() for c in result)
    assert any(c.isdigit() for c in result)


# def test_generate_password_len_mock(utils_instace, mocker):
#     mocker.patch('app.generate_password.Utils.generate_password',
#                  return_value='1a2B3c4D')
#     number = utils_instace.generate_password(8)

#     assert number == '1a2B3c4D'
