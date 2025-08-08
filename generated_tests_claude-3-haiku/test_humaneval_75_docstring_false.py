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

def is_prime(n):
    if n < 2:
        return False
    for j in range(2, int(n ** 0.5) + 1):
        if n % j == 0:
            return False
    return True

def is_multiply_prime(a):
    if a < 2:
        return False
    for i in range(2, int(a ** (1/3)) + 1):
        if is_prime(i):
            for j in range(2, int(a // i) + 1):
                if is_prime(j) and is_prime(a // (i * j)):
                    return True
    return False

@pytest.mark.parametrize("input,expected", [
    (30, True),
    (2, False),
    (100, False),
    (210, True),
    (1, False),
    (-10, False),
    (0, False),
    (101, False),
    (1000, True),
    (99, False)
])
def test_is_multiply_prime(input, expected):
    assert is_multiply_prime(input) == expected