# Test cases for HumanEval/24
# Generated using Claude API



def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """

    for i in reversed(range(n)):
        if n % i == 0:
            return i


# Generated test cases:
import pytest

def test_largest_divisor_basic():
    assert largest_divisor(10) == 5
    assert largest_divisor(12) == 6
    assert largest_divisor(15) == 5

@pytest.mark.parametrize("number,expected", [
    (20, 10),
    (7, 1),
    (16, 8),
    (100, 50),
    (97, 1),
    (25, 5)
])
def test_largest_divisor_parametrized(number, expected):
    assert largest_divisor(number) == expected

def test_largest_divisor_prime_numbers():
    assert largest_divisor(2) == 1
    assert largest_divisor(3) == 1
    assert largest_divisor(5) == 1
    assert largest_divisor(7) == 1
    assert largest_divisor(11) == 1

def test_largest_divisor_perfect_squares():
    assert largest_divisor(4) == 2
    assert largest_divisor(9) == 3
    assert largest_divisor(16) == 8
    assert largest_divisor(25) == 5

@pytest.mark.parametrize("invalid_input", [
    0,
    -1,
    -10,
    -100
])
def test_largest_divisor_invalid_input(invalid_input):
    if invalid_input == 0:
        with pytest.raises(ValueError):
            largest_divisor(invalid_input)
    else:
        with pytest.raises(ValueError):
            largest_divisor(invalid_input)

def test_largest_divisor_type_error():
    with pytest.raises(TypeError):
        largest_divisor("not a number")
    with pytest.raises(TypeError):
        largest_divisor(3.14)
    with pytest.raises(TypeError):
        largest_divisor(None)

def test_largest_divisor_large_numbers():
    assert largest_divisor(1000) == 500
    assert largest_divisor(999) == 333
    assert largest_divisor(1024) == 512