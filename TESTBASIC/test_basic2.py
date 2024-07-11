def somar(a,b):
    return a +b

def comprimento (list):
    return len(list)

def test_somar_comprimento():
    assert somar(4,5) == 9
    assert comprimento([0,1,2,3,4,5,6,7,8,9]) == 10