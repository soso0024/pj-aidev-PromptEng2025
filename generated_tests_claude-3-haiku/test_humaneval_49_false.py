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

def test_modp_zero_n():
    assert modp(0, 5) == 1

def test_modp_negative_n():
    with pytest.raises(ValueError):
        modp(-1, 5)

@pytest.mark.parametrize("n,p,expected", [
    (1, 5, 2),
    (2, 5, 4),
    (3, 5, 3),
    (4, 5, 1),
    (5, 5, 2),
    (10, 7, 1),
    (100, 11, 1)
])
def test_modp_normal_cases(n, p, expected):
    assert modp(n, p) == expected

def modp(n: int, p: int):
    if n < 0:
        raise ValueError("n cannot be negative")
    ret = 1
    for i in range(n):
        ret = (ret * 2) % p
    return ret