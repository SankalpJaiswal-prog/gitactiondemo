from calculator import add
from calculator import sub

def tes_add():
    assert add(10,5) == 15

def test_sub():
    assert sub(10,5) == 5