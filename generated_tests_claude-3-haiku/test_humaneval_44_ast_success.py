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

def change_base(x: int, base: int):
    if base < 2 or base > 16:
        raise ValueError("Base must be between 2 and 16 inclusive")
    if x < 0:
        raise ValueError("Input must be a non-negative integer")
    
    ret = ""
    while x > 0:
        digit = x % base
        if digit < 10:
            ret = str(digit) + ret
        else:
            ret = chr(ord('a') + digit - 10) + ret
        x //= base
    return ret or '0'

def test_change_base_positive_integers():
    assert change_base(10, 2) == '1010'
    assert change_base(42, 16) == '2a'
    assert change_base(100, 10) == '100'

def test_change_base_negative_integers():
    with pytest.raises(ValueError):
        change_base(-10, 2)

def test_change_base_zero_base():
    with pytest.raises(ValueError):
        change_base(10, 0)

@pytest.mark.parametrize("x, base, expected", [
    (0, 2, '0'),
    (1, 2, '1'),
    (15, 16, 'f'),
    (255, 16, 'ff'),
    (1000, 10, '1000')
])
def test_change_base_parameterized(x, base, expected):
    assert change_base(x, base) == expected