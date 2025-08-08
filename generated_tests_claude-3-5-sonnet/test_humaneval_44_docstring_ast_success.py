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

def test_basic_conversion():
    assert change_base(8, 3) == "22"
    assert change_base(8, 2) == "1000"
    assert change_base(7, 2) == "111"

@pytest.mark.parametrize("number,base,expected", [
    (10, 2, "1010"),
    (15, 3, "120"),
    (20, 4, "110"),
    (25, 5, "100"),
    (30, 6, "50"),
    (35, 7, "50"),
    (40, 8, "50"),
    (45, 9, "50")
])
def test_various_bases(number, base, expected):
    assert change_base(number, base) == expected

@pytest.mark.parametrize("number,base,expected", [
    (1, 2, "1"),
    (1, 3, "1"),
    (1, 9, "1")
])
def test_single_digit(number, base, expected):
    assert change_base(number, base) == expected

def test_zero_input():
    assert change_base(0, 2) == ""
    assert change_base(0, 5) == ""
    assert change_base(0, 9) == ""

@pytest.mark.parametrize("number,base", [
    (-1, 2),
    (-10, 3),
    (-100, 5)
])
def test_negative_numbers(number, base):
    with pytest.raises(ValueError):
        change_base(number, base)

@pytest.mark.parametrize("number,base", [
    (10, 0),
    (10, -1),
    (10, 1),
    (10, 10),
    (10, 100)
])
def test_invalid_bases(number, base):
    with pytest.raises(ValueError):
        change_base(number, base)

def test_large_numbers():
    assert change_base(1000, 2) == "1111101000"
    assert change_base(1000, 3) == "1101001"
    assert change_base(1000, 9) == "1331"

def change_base(x: int, base: int) -> str:
    if x < 0:
        raise ValueError("Input number must be non-negative")
    if base <= 1 or base >= 10:
        raise ValueError("Base must be between 2 and 9")
    if x == 0:
        return ""
    ret = ""
    while x > 0:
        ret = str(x % base) + ret
        x //= base
    return ret