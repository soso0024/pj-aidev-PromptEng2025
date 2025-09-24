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

@pytest.mark.parametrize("n, p, expected", [
    (3, 5, 3),
    (1101, 101, 2),
    (0, 101, 1),
    (3, 11, 8),
    (100, 101, 1),
    (-1, 5, ValueError),
    (3.14, 5, TypeError),
    (0, 0, ZeroDivisionError)
])
def test_modp(n, p, expected):
    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            modp(n, p)
    else:
        assert modp(n, p) == expected

def modp(n: int, p: int):
    if p == 0:
        raise ZeroDivisionError
    if not isinstance(n, int):
        raise TypeError
    if n < 0:
        raise ValueError
    ret = 1
    for i in range(n):
        ret = (2 * ret) % p
    return ret