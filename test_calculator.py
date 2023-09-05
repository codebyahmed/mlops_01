from calculator import sub

def test_sub():
    assert sub(4, 2) == 2
    assert sub(4, 1) == 3
    assert sub(4, 5) == -1