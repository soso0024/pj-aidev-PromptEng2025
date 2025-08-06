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

def test_modp_basic():
    assert modp(1, 5) == 2
    assert modp(2, 5) == 4
    assert modp(3, 5) == 3

@pytest.mark.parametrize("n, p, expected", [
    (0, 5, 1),
    (1, 7, 2),
    (2, 11, 4),
    (3, 13, 8),
    (4, 17, 16),
    (5, 19, 13),
])
def test_modp_various_inputs(n, p, expected):
    assert modp(n, p) == expected

@pytest.mark.parametrize("n, p", [
    (10, 1000),
    (20, 999),
    (50, 997),
    (100, 991),
])
def test_modp_large_numbers(n, p):
    result = modp(n, p)
    assert result >= 0
    assert result < p

def test_modp_edge_cases():
    assert modp(0, 5) == 1
    assert modp(1, 2) == 0
    assert modp(0, 2) == 1

@pytest.mark.parametrize("n, p", [
    (5, 0),
])
def test_modp_invalid_inputs(n, p):
    with pytest.raises(ZeroDivisionError):
        modp(n, p)

def test_modp_prime_modulus():
    assert modp(4, 7) == 2
    assert modp(5, 11) == 10
    assert modp(6, 13) == 12

def test_modp_composite_modulus():
    assert modp(3, 4) == 0
    assert modp(4, 6) == 4
    assert modp(5, 8) == 0

def test_modp_types():
    with pytest.raises(TypeError):
        modp("1", 5)
    with pytest.raises(TypeError):
        modp(1, "5")
    with pytest.raises(TypeError):
        modp(1.5, 5)