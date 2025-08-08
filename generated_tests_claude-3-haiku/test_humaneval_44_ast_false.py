# Test cases for HumanEval/44
# Generated using Claude API



def change_base(x: int, base: int):
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """

    ret = ""
    while x > 0:
        ret = str(x % base) + ret
        x //= base
    return ret


# Generated test cases:
import pytest

def test_change_base_positive_integers():
    assert change_base(10, 2) == '1010'
    assert change_base(42, 16) == '2A'
    assert change_base(100, 10) == '100'

def test_change_base_negative_integers():
    with pytest.raises(ValueError):
        change_base(-10, 2)
    with pytest.raises(ValueError):
        change_base(10, -2)

def test_change_base_zero_base():
    with pytest.raises(ValueError):
        change_base(10, 0)

def test_change_base_large_numbers():
    assert change_base(2**64 - 1, 2) == '1'*64
    assert change_base(2**100, 16) == '1'*25

def test_change_base_empty_input():
    assert change_base(0, 2) == '0'

@pytest.mark.parametrize("x,base,expected", [
    (10, 2, '1010'),
    (42, 16, '2A'),
    (100, 10, '100'),
    (-10, 2, pytest.raises(ValueError)),
    (10, -2, pytest.raises(ValueError)),
    (10, 0, pytest.raises(ValueError)),
    (2**64 - 1, 2, '1'*64),
    (2**100, 16, '1'*25),
    (0, 2, '0')
])
def test_change_base_parametrized(x, base, expected):
    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            change_base(x, base)
    else:
        assert change_base(x, base) == expected