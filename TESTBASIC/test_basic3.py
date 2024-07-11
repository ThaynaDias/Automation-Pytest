from funcoes import *

def test_email_valido():
    assert email_valido("exempplo@dominio.com") is True
    assert email_valido("exemplo.com") is False

def test_dividir():
    assert dividir(5, 2) == 2.5
    assert dividir(5,5) == 1