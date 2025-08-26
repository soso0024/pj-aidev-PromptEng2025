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
from is_multiply_prime import is_multiply_prime

import pytest

@pytest.mark.parametrize("input,expected", [
    (1, False),
    (2, False),
    (3, False),
    (4, True),
    (6, True),
    (8, True),
    (9, False),
    (10, False),
    (12, True),
    (15, True),
    (16, True),
    (18, True),
    (21, True),
    (25, True),
    (27, False),
    (30, True),
    (100, True),
    (101, False),
    (102, True),
    (103, False),
    (104, True),
    (105, True),
    (0, False),
    (-1, False),
    (1.0, False),
])
def test_is_multiply_prime(input, expected):
    assert is_multiply_prime(input) == expected