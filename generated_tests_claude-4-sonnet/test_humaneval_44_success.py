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
    ret = ""
    while x > 0:
        ret = str(x % base) + ret
        x //= base
    return ret

def test_change_base_zero():
    assert change_base(0, 2) == ""
    assert change_base(0, 10) == ""
    assert change_base(0, 16) == ""

def test_change_base_binary():
    assert change_base(1, 2) == "1"
    assert change_base(2, 2) == "10"
    assert change_base(3, 2) == "11"
    assert change_base(4, 2) == "100"
    assert change_base(8, 2) == "1000"
    assert change_base(15, 2) == "1111"

def test_change_base_decimal():
    assert change_base(1, 10) == "1"
    assert change_base(10, 10) == "10"
    assert change_base(123, 10) == "123"
    assert change_base(999, 10) == "999"

def test_change_base_octal():
    assert change_base(1, 8) == "1"
    assert change_base(8, 8) == "10"
    assert change_base(64, 8) == "100"
    assert change_base(15, 8) == "17"

def test_change_base_hexadecimal():
    assert change_base(1, 16) == "1"
    assert change_base(16, 16) == "10"
    assert change_base(255, 16) == "1515"
    assert change_base(256, 16) == "100"

@pytest.mark.parametrize("x,base,expected", [
    (1, 3, "1"),
    (3, 3, "10"),
    (9, 3, "100"),
    (10, 3, "101"),
    (1, 5, "1"),
    (5, 5, "10"),
    (25, 5, "100"),
    (26, 5, "101"),
    (1, 7, "1"),
    (7, 7, "10"),
    (49, 7, "100"),
    (50, 7, "101")
])
def test_change_base_various_bases(x, base, expected):
    assert change_base(x, base) == expected

def test_change_base_large_numbers():
    assert change_base(1000, 2) == "1111101000"
    assert change_base(1000, 8) == "1750"
    assert change_base(1000, 16) == "3148"

def test_change_base_edge_cases():
    assert change_base(1, 36) == "1"
    assert change_base(35, 36) == "35"
    assert change_base(36, 36) == "10"

def test_change_base_single_digit():
    for base in range(2, 11):
        assert change_base(1, base) == "1"

def test_change_base_power_of_base():
    assert change_base(4, 2) == "100"
    assert change_base(9, 3) == "100"
    assert change_base(16, 4) == "100"
    assert change_base(25, 5) == "100"