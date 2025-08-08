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
    ret = 1
    for i in range(n):
        ret = (2 * ret) % p
    return ret

@pytest.mark.parametrize("n, p, expected", [
    (0, 2, 1),
    (1, 2, 2),
    (2, 2, 0),
    (3, 2, 0),
    (4, 2, 0),
    (5, 2, 0),
    (6, 2, 0),
    (7, 2, 1),
    (8, 2, 0),
    (9, 2, 1),
    (10, 2, 0),
    (11, 2, 1),
    (12, 2, 0),
    (13, 2, 1),
    (14, 2, 0),
    (15, 2, 1),
    (16, 2, 0),
    (17, 2, 1),
    (18, 2, 0),
    (19, 2, 1),
    (20, 2, 0),
    (21, 2, 1),
    (22, 2, 0),
    (23, 2, 1),
    (24, 2, 0),
    (25, 2, 1),
    (26, 2, 0),
    (27, 2, 1),
    (28, 2, 0),
    (29, 2, 1),
    (30, 2, 0),
    (31, 2, 1),
    (32, 2, 0),
    (0, 3, 1),
    (1, 3, 2),
    (2, 3, 1),
    (3, 3, 0),
    (4, 3, 2),
    (5, 3, 1),
    (6, 3, 0),
    (7, 3, 2),
    (8, 3, 1),
    (9, 3, 0),
    (10, 3, 2),
    (11, 3, 1),
    (12, 3, 0),
    (13, 3, 2),
    (14, 3, 1),
    (15, 3, 0),
    (16, 3, 2),
    (17, 3, 1),
    (18, 3, 0),
    (19, 3, 2),
    (20, 3, 1),
    (21, 3, 0),
    (22, 3, 2),
    (23, 3, 1),
    (24, 3, 0),
    (25, 3, 2),
    (26, 3, 1),
    (27, 3, 0),
    (28, 3, 2),
    (29, 3, 1),
    (30, 3, 0),
    (31, 3, 2),
    (32, 3, 1),
    (-1, 2, ValueError),
    (0, -1, ValueError),
    (33, 2, ValueError),
    (32, 0, ZeroDivisionError),
])
def test_modp(n, p, expected):
    if expected in (ValueError, ZeroDivisionError):
        with pytest.raises(expected):
            modp(n, p)
    else:
        assert modp(n, p) == expected