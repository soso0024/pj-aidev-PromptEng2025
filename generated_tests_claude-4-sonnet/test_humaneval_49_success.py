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

def test_modp_basic_cases():
    assert modp(3, 5) == 3
    assert modp(1101, 101) == 2
    assert modp(0, 101) == 1
    assert modp(3, 11) == 8
    assert modp(100, 101) == 1

def test_modp_zero_n():
    assert modp(0, 5) == 1
    assert modp(0, 1000) == 1
    assert modp(0, 2) == 1

def test_modp_small_p():
    assert modp(1, 2) == 0
    assert modp(2, 2) == 0
    assert modp(3, 2) == 0
    assert modp(5, 3) == 2

def test_modp_large_values():
    assert modp(1000, 1009) == 942
    assert modp(500, 997) == 993
    assert modp(10, 1000) == 24

def test_modp_edge_cases():
    assert modp(1, 1000) == 2
    assert modp(2, 1000) == 4
    assert modp(10, 13) == 10

@pytest.mark.parametrize("n,p,expected", [
    (0, 5, 1),
    (1, 5, 2),
    (2, 5, 4),
    (3, 5, 3),
    (4, 5, 1),
    (5, 7, 4),
    (10, 101, 14),
    (20, 23, 6)
])
def test_modp_parametrized(n, p, expected):
    assert modp(n, p) == expected

def test_modp_power_of_two_pattern():
    assert modp(1, 1000) == 2
    assert modp(2, 1000) == 4
    assert modp(3, 1000) == 8
    assert modp(4, 1000) == 16
    assert modp(5, 1000) == 32

def test_modp_cycle_detection():
    assert modp(4, 5) == 1
    assert modp(8, 5) == 1
    assert modp(12, 5) == 1