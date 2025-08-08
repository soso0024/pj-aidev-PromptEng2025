# Test cases for HumanEval/49
# Generated using Claude API



def modp(n: int, p: int):
    """Return 2^n modulo p (be aware of numerics).
    >>> modp(3, 5)
    3
    >>> modp(1101, 101)
    2
    >>> modp(0, 101)
    1
    >>> modp(3, 11)
    8
    >>> modp(100, 101)
    1
    """

    ret = 1
    for i in range(n):
        ret = (2 * ret) % p
    return ret


# Generated test cases:
import pytest

def modp(n: int, p: int):
    if n < 0 or p <= 0:
        raise ValueError("n must be non-negative and p must be positive")
    
    ret = 1
    for _ in range(n):
        ret = (2 * ret) % p
    return ret

def test_modp_basic_cases():
    assert modp(0, 7) == 1
    assert modp(1, 7) == 2
    assert modp(2, 7) == 4
    assert modp(3, 7) == 1

def test_modp_large_numbers():
    assert modp(10, 1000000007) > 0
    assert modp(100, 1000000007) > 0

def test_modp_prime_modulus():
    assert modp(5, 11) == 10
    assert modp(7, 13) == 3

@pytest.mark.parametrize("n,p,expected", [
    (0, 5, 1),
    (1, 5, 2),
    (2, 5, 4),
    (3, 5, 3),
    (4, 5, 1),
    (10, 7, 2),
    (100, 13, 3)
])
def test_modp_parametrized(n, p, expected):
    assert modp(n, p) == expected

def test_modp_negative_inputs():
    with pytest.raises(ValueError):
        modp(-1, 7)
    with pytest.raises(ValueError):
        modp(5, -3)

def test_modp_zero_modulus():
    with pytest.raises(ValueError):
        modp(5, 0)