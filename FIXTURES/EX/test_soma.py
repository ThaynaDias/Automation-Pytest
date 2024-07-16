import pytest
def soma_dobro(numeros):
    return sum(x * 2 for x in numeros) 


@pytest.fixture
def list_num():
    return [5,-9, 8, -3, 10]

def test_soma_dobro(list_num):
    result = soma_dobro(list_num)
    assert result == 11, "A soma dobro dos números deve ser 11"

def test_soma_dobro_vazia(list_num):
    list_num.clear()
    result = soma_dobro(list_num) 
    assert result == 0, "A soma dobro dos números deve ser 0"


## Resolução do prof


@pytest.fixture
def lista_numeros():
    return [1,-2,-3]

def test_soma_dobro(lista_numeros):
    resultado = soma_dobro(lista_numeros)
    assert resultado == -8, "A soma dobro dos números deve ser 30"

def test_soma_dobro_lista_vazia(lista_numeros):
    lista_numeros.clear()  
    resultado = soma_dobro(lista_numeros)
    assert resultado == 0, "A soma dobro de uma lista vazia deve ser 0"

