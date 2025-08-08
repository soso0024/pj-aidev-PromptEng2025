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

def test_change_base_positive_int():
    assert change_base(8, 3) == '22'
    assert change_base(8, 2) == '1000'
    assert change_base(7, 2) == '111'

def test_change_base_negative_int():
    with pytest.raises(ValueError):
        change_base(-8, 3)

def test_change_base_zero():
    assert change_base(0, 2) == '0'

def test_change_base_base_less_than_two():
    with pytest.raises(ValueError):
        change_base(8, 1)

def test_change_base_base_greater_than_nine():
    with pytest.raises(ValueError):
        change_base(8, 10)

def test_change_base_float_input():
    with pytest.raises(TypeError):
        change_base(8.5, 3)

def test_change_base_string_input():
    with pytest.raises(TypeError):
        change_base('8', 3)

@pytest.mark.parametrize("x, base, expected", [
    (100, 2, '1100100'),
    (1234, 16, '4D2'),
    (0, 5, '0'),
    (1000, 10, '1000')
])
def test_change_base_parameterized(x, base, expected):
    assert change_base(x, base) == expected