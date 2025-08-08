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
    for j in range(2, int(n**0.5) + 1):
        if n % j == 0:
            return False
    return True

def is_multiply_prime(a):
    if a < 2:
        return False
    for i in range(2, int(a**0.5) + 1):
        if is_prime(i) and a % i == 0:
            for j in range(2, int(a/i) + 1):
                if is_prime(j) and a % (i*j) == 0:
                    for k in range(2, int(a/(i*j)) + 1):
                        if is_prime(k) and a == i*j*k:
                            return True
    return False

@pytest.mark.parametrize("a, expected", [
    (6, True),
    (10, True),
    (15, True),
    (21, True),
    (100, False),
    (101, False),
    (0, False),
    (-5, False),
    (1, False),
    (2, True),
    (3, True),
    (4, False),
    (5, True),
    (7, True),
    (11, True),
    (13, True),
    (17, True),
    (19, True),
    (23, True),
    (29, True),
])
def test_is_multiply_prime(a, expected):
    assert is_multiply_prime(a) == expected

def test_is_multiply_prime_edge_cases():
    assert is_multiply_prime(2) is True
    assert is_multiply_prime(1) is False
    assert is_multiply_prime(0) is False
    assert is_multiply_prime(-5) is False

def test_is_multiply_prime_invalid_input():
    with pytest.raises(TypeError):
        is_multiply_prime("invalid")
    with pytest.raises(TypeError):
        is_multiply_prime([1, 2, 3])
    with pytest.raises(TypeError):
        is_multiply_prime(None)