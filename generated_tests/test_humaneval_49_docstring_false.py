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
    assert modp(3, 5) == 3
    assert modp(1101, 101) == 2
    assert modp(0, 101) == 1
    assert modp(3, 11) == 8
    assert modp(100, 101) == 1

@pytest.mark.parametrize("n, p, expected", [
    (0, 7, 1),
    (1, 7, 2),
    (2, 7, 4),
    (3, 7, 1),
    (10, 13, 10),
    (20, 17, 16),
    (50, 97, 4),
])
def test_modp_parametrized(n, p, expected):
    assert modp(n, p) == expected

def test_modp_large_numbers():
    assert modp(1000, 997) == 16
    assert modp(500, 499) == 4
    assert modp(2000, 1999) == 1264

@pytest.mark.parametrize("n, p", [
    (-1, 5),
    (3, 0),
    (3, -7),
])
def test_modp_invalid_inputs(n, p):
    if p <= 0:
        with pytest.raises(ValueError):
            modp(n, p)
    elif n < 0:
        with pytest.raises(ValueError):
            modp(n, p)

def test_modp_edge_cases():
    assert modp(0, 2) == 1
    assert modp(1, 2) == 0
    assert modp(0, 1000000007) == 1
    assert modp(1, 1000000007) == 2

def test_modp_consecutive_powers():
    p = 23
    prev = 1
    for i in range(5):
        result = modp(i, p)
        assert result == prev
        prev = (prev * 2) % p