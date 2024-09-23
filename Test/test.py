from SRC.Main import *
from unittest.mock import patch

import pytest
import pytest_asyncio

@pytest.mark.asyncio
async def teste_root():
    result = await root()
    assert result == {"message": "Hello World"}

@pytest.mark.asyncio
async def funcaoteste():
    with patch('random.randint', return_value=12345):
        result = funcaoteste()

    assert result == {"teste": True, "nun_aleatorio": 12345}

@pytest.mark.asyncio
async def test_create_estudante():
    estudante_teste = Estudante(name="Fulano", curso="curso 1", ativo=False)
    assert estudante_teste == create_estudante()

@pytest.mark.asyncio
async def test_update_estudante_negativo():
    result = await update_estudante(-5)
    assert not result

@pytest.mark.asyncio
async def test_update_estudante_positivo():
    result = await update_estudante(10)
    assert result

@pytest.mark.asyncio
async def test_delete_estudante_negativo():
    result = await delete_estudante(-5)
    assert not result

@pytest.mark.asyncio
async def test_delete_estudante_positivo():
    result = await delete_estudante(10)
    assert result
