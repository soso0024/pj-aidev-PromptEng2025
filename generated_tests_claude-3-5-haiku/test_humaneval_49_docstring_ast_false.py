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
    assert modp(3, 5) == 3
    assert modp(1101, 101) == 2
    assert modp(0, 101) == 1
    assert modp(3, 11) == 8
    assert modp(100, 101) == 1

@pytest.mark.parametrize("n,p,expected", [
    (0, 2, 1),
    (1, 2, 0),
    (2, 3, 1),
    (10, 7, 4),
    (100, 13, 9)
])
def test_modp_parametrized(n, p, expected):
    assert modp(n, p) == expected

def test_modp_large_numbers():
    assert modp(10000, 17) == 16
    assert modp(1000000, 23) == 8

def test_modp_edge_cases():
    with pytest.raises(TypeError):
        modp(None, 5)
    with pytest.raises(TypeError):
        modp(3, None)
    with pytest.raises(ValueError):
        modp(3, 0)

def test_modp_negative_inputs():
    with pytest.raises(ValueError):
        modp(-1, 5)
    with pytest.raises(ValueError):
        modp(3, -5)