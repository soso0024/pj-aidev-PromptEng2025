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

def test_modp_zero():
    assert modp(0, 5) == 1

def test_modp_one():
    assert modp(1, 5) == 2

def test_modp_negative_n():
    with pytest.raises(ValueError):
        modp(-1, 5)

def test_modp_negative_p():
    with pytest.raises(ValueError):
        modp(2, -5)

def test_modp_zero_p():
    with pytest.raises(ZeroDivisionError):
        modp(2, 0)

@pytest.mark.parametrize("n, p, expected", [
    (2, 5, 4),
    (3, 7, 1),
    (4, 11, 5),
    (5, 13, 6),
    (10, 1000, 24),
    (20, 997, 729),
])
def test_modp_various_inputs(n, p, expected):
    assert modp(n, p) == expected

@pytest.mark.parametrize("n, p", [
    (1.5, 5),
    ("2", 5),
    (2, "5"),
])
def test_modp_invalid_types(n, p):
    with pytest.raises(TypeError):
        modp(n, p)

def test_modp_large_numbers():
    assert modp(100, 997) == 907
    assert modp(1000, 997) == 582

def test_modp_boundary_cases():
    assert modp(1, 2) == 0
    assert modp(2, 3) == 1
    assert modp(3, 4) == 0