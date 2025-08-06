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
    (4, 7, 2),
    (10, 13, 10),
    (20, 17, 16),
    (50, 97, 4),
])
def test_modp_parametrized(n, p, expected):
    assert modp(n, p) == expected

@pytest.mark.parametrize("n, p", [
    (3, 0),
])
def test_modp_invalid_inputs(n, p):
    with pytest.raises(ZeroDivisionError):
        modp(n, p)

def test_modp_large_numbers():
    assert modp(1000, 997) == 16
    assert modp(10000, 997) == 40

def test_modp_power_of_two():
    assert modp(8, 17) == 1
    assert modp(16, 31) == 2

def test_modp_prime_modulus():
    assert modp(10, 11) == 1
    assert modp(12, 13) == 1
    assert modp(15, 17) == 9

def test_modp_consecutive_numbers():
    results = [modp(i, 13) for i in range(5)]
    assert results == [1, 2, 4, 8, 3]

def test_modp_edge_cases():
    assert modp(1, 2) == 0
    assert modp(0, 2) == 1
    assert modp(100, 2) == 0