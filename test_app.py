from app import square, is_even
def test_square_positive():
    assert square(4) == 16
def test_square_negative():
    assert square(-3) == 9
def test_is_even_true():
    assert is_even(8) is True
def test_is_even_false():
    assert is_even(7) is False