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
from typing import Union

def test_change_base_basic():
    assert change_base(10, 2) == "1010"
    assert change_base(8, 3) == "22"
    assert change_base(8, 2) == "1000"

@pytest.mark.parametrize("number,base,expected", [
    (10, 2, "1010"),
    (15, 3, "120"),
    (8, 3, "22"),
    (100, 3, "10201"),
    (255, 4, "3333"),
    (1, 2, "1"),
    (7, 3, "21"),
    (64, 3, "2121"),
])
def test_change_base_parametrized(number, base, expected):
    assert change_base(number, base) == expected

def test_change_base_zero():
    assert change_base(0, 2) == ""
    assert change_base(0, 3) == ""
    assert change_base(0, 9) == ""

@pytest.mark.parametrize("number,base", [
    (10, 2),
    (15, 3),
    (8, 3),
    (100, 3),
])
def test_change_base_valid_inputs(number, base):
    result = change_base(number, base)
    assert isinstance(result, str)
    assert all(c.isdigit() and int(c) < base for c in result)

def test_change_base_large_numbers():
    assert change_base(1000, 2) == "1111101000"
    assert change_base(1000, 3) == "1101001"

def test_change_base_edge_cases():
    assert change_base(1, 2) == "1"
    assert change_base(7, 2) == "111"
    assert change_base(8, 2) == "1000"