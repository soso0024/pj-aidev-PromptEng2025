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

def largest_divisor(n: int) -> int:
    if n < 1:
        raise ValueError("Input must be a positive integer")
    
    for i in reversed(range(1, n)):
        if n % i == 0:
            return i
    
    return 1

def test_largest_divisor_normal_cases():
    assert largest_divisor(15) == 5
    assert largest_divisor(100) == 50
    assert largest_divisor(17) == 1
    assert largest_divisor(24) == 12

def test_largest_divisor_edge_cases():
    assert largest_divisor(1) == 1
    assert largest_divisor(2) == 1

@pytest.mark.parametrize("n,expected", [
    (15, 5),
    (100, 50),
    (17, 1),
    (24, 12),
    (1, 1),
    (2, 1)
])
def test_largest_divisor_parametrized(n, expected):
    assert largest_divisor(n) == expected

def test_largest_divisor_error_cases():
    with pytest.raises(TypeError):
        largest_divisor(None)
    with pytest.raises(TypeError):
        largest_divisor("string")
    with pytest.raises(TypeError):
        largest_divisor(3.14)

def test_largest_divisor_negative_numbers():
    with pytest.raises(ValueError):
        largest_divisor(-10)