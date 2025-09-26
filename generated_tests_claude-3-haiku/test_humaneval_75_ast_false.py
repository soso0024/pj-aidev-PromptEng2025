# Test cases for HumanEval/75
# Generated using Claude API


def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """

    def is_prime(n):
        for j in range(2,n):
            if n%j == 0:
                return False
        return True

    for i in range(2,101):
        if not is_prime(i): continue
        for j in range(2,101):
            if not is_prime(j): continue
            for k in range(2,101):
                if not is_prime(k): continue
                if i*j*k == a: return True
    return False


# Generated test cases:
import pytest

def test_is_multiply_prime(input, expected):
    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            is_multiply_prime(input)
    else:
        assert is_multiply_prime(input) == expected

@pytest.mark.parametrize("input,expected", [
    (1, False),
    (2, False),
    (6, True),
    (12, True),
    (24, True),
    (30, True),
    (100, True),
    (101, False),
    (1000, False),
    (2000, True),
    (0, False),
    (-1, False),
    (3.14, TypeError),
    ('test', TypeError)
])
def test_is_multiply_prime(input, expected):
    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            is_multiply_prime(input)
    else:
        assert is_multiply_prime(input) == expected