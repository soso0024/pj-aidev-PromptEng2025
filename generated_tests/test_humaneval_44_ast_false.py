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

def test_change_base_basic():
    assert change_base(10, 2) == "1010"
    assert change_base(8, 2) == "1000"
    assert change_base(7, 2) == "111"

@pytest.mark.parametrize("number,base,expected", [
    (10, 2, "1010"),
    (8, 2, "1000"),
    (7, 2, "111"),
    (100, 2, "1100100"),
    (1, 2, "1"),
    (7, 3, "21"),
    (8, 3, "22"),
])
def test_change_base_parametrized(number, base, expected):
    assert change_base(number, base) == expected

def test_change_base_zero():
    assert change_base(0, 2) == ""
    assert change_base(0, 3) == ""
    assert change_base(0, 9) == ""

@pytest.mark.parametrize("number,base", [
    (-1, 2),
    (-10, 3),
    (-100, 9),
])
def test_change_base_negative_numbers(number, base):
    with pytest.raises(ValueError):
        change_base(number, base)

@pytest.mark.parametrize("number,base", [
    (10, 0),
    (10, -2),
    (10, 1),
    (10, 10),
])
def test_change_base_invalid_base(number, base):
    with pytest.raises(ValueError):
        change_base(number, base)

def test_change_base_large_numbers():
    assert change_base(1000, 2) == "1111101000"
    assert change_base(1000, 3) == "1101001"
    assert change_base(1000, 9) == "1331"

@pytest.mark.parametrize("number,base", [
    (10, "2"),
    ("10", 2),
    (None, 2),
    (10, None),
])
def test_change_base_invalid_types(number, base):
    with pytest.raises(TypeError):
        change_base(number, base)