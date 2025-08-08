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

def test_change_base_normal_cases():
    assert change_base(8, 3) == '22'
    assert change_base(8, 2) == '1000'
    assert change_base(7, 2) == '111'
    assert change_base(15, 2) == '1111'
    assert change_base(10, 3) == '101'

@pytest.mark.parametrize("x,base,expected", [
    (0, 2, ''),
    (1, 2, '1'),
    (1, 3, '1'),
    (10, 10, '10')
])
def test_change_base_edge_cases(x, base, expected):
    assert change_base(x, base) == expected

def test_change_base_single_digit():
    assert change_base(5, 2) == '101'
    assert change_base(9, 3) == '100'

def test_change_base_larger_numbers():
    assert change_base(255, 2) == '11111111'
    assert change_base(100, 5) == '400'

@pytest.mark.parametrize("x,base", [
    (10, 1),
    (5, 0),
    (5, 11)
])
def test_change_base_invalid_base(x, base):
    with pytest.raises(ValueError):
        change_base(x, base)

def test_change_base_zero():
    assert change_base(0, 2) == ''