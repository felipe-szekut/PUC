from SRC.Main import *
from unittest.mock import patch


def teste_root():
    result = root()
    yield result
    assert result == {"message": "Hello World"}


def funcaoteste():
    with patch('random.randint', return_value=12345):
        result = funcaoteste()
        yield result

    assert result == {"teste": True, "nun_aleatorio": 12345}


def test_create_estudante():
    estudante_teste = Estudante(name="Fulano", curso="curso 1", ativo=False)
    result = create_estudante(estudante_teste)
    yield result
    assert estudante_teste == result


def test_update_estudante_negativo():
    result = update_estudante(-5)
    yield result
    assert not result


def test_update_estudante_positivo():
    result = update_estudante(10)
    yield result
    assert result


def test_delete_estudante_negativo():
    result = delete_estudante(-5)
    yield result
    assert not result


def test_delete_estudante_positivo():
    result = delete_estudante(10)
    yield result
    assert result
