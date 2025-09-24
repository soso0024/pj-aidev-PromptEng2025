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

def test_change_base_examples():
    assert change_base(8, 3) == "22"
    assert change_base(8, 2) == "1000"
    assert change_base(7, 2) == "111"

def test_change_base_zero():
    assert change_base(0, 2) == ""
    assert change_base(0, 3) == ""
    assert change_base(0, 9) == ""

def test_change_base_one():
    assert change_base(1, 2) == "1"
    assert change_base(1, 3) == "1"
    assert change_base(1, 9) == "1"

@pytest.mark.parametrize("x,base,expected", [
    (10, 2, "1010"),
    (15, 2, "1111"),
    (16, 2, "10000"),
    (27, 3, "1000"),
    (26, 3, "222"),
    (100, 5, "400"),
    (255, 8, "377"),
    (512, 9, "628")
])
def test_change_base_various_cases(x, base, expected):
    assert change_base(x, base) == expected

def test_change_base_large_numbers():
    assert change_base(1000, 2) == "1111101000"
    assert change_base(999, 3) == "1101000"
    assert change_base(1024, 8) == "2000"

def test_change_base_all_bases():
    for base in range(2, 10):
        result = change_base(10, base)
        assert isinstance(result, str)
        assert len(result) > 0

def test_change_base_edge_values():
    assert change_base(2, 2) == "10"
    assert change_base(3, 3) == "10"
    assert change_base(9, 9) == "10"
    assert change_base(8, 9) == "8"