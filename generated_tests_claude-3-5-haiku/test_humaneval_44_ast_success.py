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
        return "0"
    
    digits = "0123456789abcdefghijklmnopqrstuvwxyz"
    ret = ""
    while x > 0:
        ret = digits[x % base] + ret
        x //= base
    return ret

def test_change_base_decimal_to_binary():
    assert change_base(10, 2) == "1010"

def test_change_base_decimal_to_hex():
    assert change_base(255, 16) == "ff"

def test_change_base_zero():
    assert change_base(0, 2) == "0"

@pytest.mark.parametrize("x,base,expected", [
    (15, 2, "1111"),
    (100, 16, "64"),
    (7, 8, "7"),
    (42, 3, "1120")
])
def test_change_base_multiple_cases(x, base, expected):
    assert change_base(x, base) == expected

def test_change_base_single_digit():
    assert change_base(5, 10) == "5"

def test_change_base_large_number():
    assert change_base(1234567, 36) == "qglj"