from app.class_container import Container

# exercise_53


def test_container_has_code_attribute():
    container = Container()
    #  Que contenga el atributo 'code'
    assert hasattr(container, 'code')


def test_container_code_is_correct():
    container = Container()
    #  El valor del atributo 'code'
    assert container.code == 'ABCD1234'


def test_container_code_is_string():
    container = Container()
    #  El tipo de dato del atributo 'code'
    assert isinstance(container.code, str)
