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

def test_modp_basic_cases():
    assert modp(0, 7) == 1
    assert modp(1, 7) == 2
    assert modp(2, 7) == 4
    assert modp(3, 7) == 1

def test_modp_large_n():
    assert modp(10, 13) == 4
    assert modp(100, 17) == 16

def test_modp_prime_modulus():
    assert modp(5, 11) == 10
    assert modp(7, 19) == 6

def test_modp_composite_modulus():
    assert modp(4, 15) == 1
    assert modp(6, 21) == 1

@pytest.mark.parametrize("n,p,expected", [
    (0, 5, 1),
    (1, 5, 2),
    (2, 5, 4),
    (3, 5, 3),
    (4, 5, 1),
    (10, 13, 4),
    (100, 17, 16)
])
def test_modp_parametrized(n, p, expected):
    assert modp(n, p) == expected

def test_modp_error_cases():
    with pytest.raises(TypeError):
        modp('invalid', 5)
    with pytest.raises(TypeError):
        modp(5, 'invalid')
    with pytest.raises(ZeroDivisionError):
        modp(5, 0)