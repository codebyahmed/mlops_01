from calculator import  multiply

def test_multiply():
    assert multiply(2,6) == 12
    assert multiply(2.5,-5) == -12.5
    assert multiply(-3,-6) == 18