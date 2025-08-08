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
from your_module import change_base
import pytest

@pytest.mark.parametrize("x, base, expected", [
    (8, 3, '22'),
    (8, 2, '1000'),
    (7, 2, '111'),
    (0, 2, '0'),
    (-8, 2, '-1000'),
    (100, 10, '100'),
    (1234, 16, '4d2'),
])
def test_change_base(x, base, expected):
    assert change_base(x, base) == expected

def test_invalid_base():
    with pytest.raises(ValueError):
        change_base(8, 11)

def test_negative_number():
    assert change_base(-8, 2) == '-1000'

def test_zero_input():
    assert change_base(0, 2) == '0'