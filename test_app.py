from app import square, is_even

# Tests for square(n)
def test_square_positive():
    assert square(4) == 16

def test_square_negative():
    assert square(-3) == 9

# Tests for is_even(n)
def test_is_even_true():
    assert is_even(4) is True

def test_is_even_false():
    assert is_even(5) is False
