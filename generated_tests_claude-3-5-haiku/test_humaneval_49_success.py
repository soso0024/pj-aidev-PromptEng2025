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
        raise ValueError("Invalid input: n must be non-negative and p must be positive")
    ret = 1
    for i in range(n):
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

def test_modp_edge_cases():
    assert modp(0, 5) == 1
    assert modp(1, 5) == 2
    assert modp(4, 5) == 1

@pytest.mark.parametrize("n,p,expected", [
    (0, 3, 1),
    (1, 3, 2),
    (2, 3, 1),
    (3, 3, 2),
    (4, 3, 1),
    (5, 3, 2)
])
def test_modp_parametrized(n, p, expected):
    assert modp(n, p) == expected

def test_modp_prime_modulus():
    assert modp(10, 11) > 0
    assert modp(20, 23) > 0

def test_modp_non_prime_modulus():
    assert modp(10, 12) > 0
    assert modp(20, 15) > 0

def test_modp_large_exponent():
    result = modp(1000, 1000000007)
    assert result > 0
    assert result < 1000000007

@pytest.mark.parametrize("n,p", [
    (-1, 5),
    (0, 0),
    (1, 0)
])
def test_modp_invalid_inputs(n, p):
    with pytest.raises(ValueError):
        modp(n, p)