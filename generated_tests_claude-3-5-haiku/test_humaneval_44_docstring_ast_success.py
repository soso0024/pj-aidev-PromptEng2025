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
    if x == 0:
        return ''
    
    digits = '0123456789abcdef'
    ret = ""
    while x > 0:
        ret = digits[x % base] + ret
        x //= base
    return ret

def test_change_base_decimal_to_binary():
    assert change_base(8, 2) == '1000'
    assert change_base(7, 2) == '111'
    assert change_base(15, 2) == '1111'

def test_change_base_decimal_to_ternary():
    assert change_base(8, 3) == '22'
    assert change_base(9, 3) == '100'

def test_change_base_zero():
    assert change_base(0, 2) == ''
    assert change_base(0, 3) == ''

@pytest.mark.parametrize("x,base,expected", [
    (1, 2, '1'),
    (10, 3, '101'),
    (16, 4, '100'),
    (255, 16, 'ff')
])
def test_change_base_parametrized(x, base, expected):
    assert change_base(x, base) == expected

def test_change_base_single_digit():
    assert change_base(5, 5) == '10'
    assert change_base(9, 9) == '10'

def test_change_base_large_numbers():
    assert change_base(1024, 2) == '10000000000'
    assert change_base(1000, 8) == '1750'