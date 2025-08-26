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
        return '0'
    
    if base > 10:
        hex_chars = '0123456789abcdef'
        ret = ""
        while x > 0:
            ret = hex_chars[x % base] + ret
            x //= base
        return ret

    ret = ""
    while x > 0:
        ret = str(x % base) + ret
        x //= base
    return ret

def test_change_base_normal_cases():
    assert change_base(8, 3) == '22'
    assert change_base(8, 2) == '1000'
    assert change_base(7, 2) == '111'
    assert change_base(15, 2) == '1111'
    assert change_base(15, 16) == 'f'

@pytest.mark.parametrize("number,base,expected", [
    (0, 2, '0'),
    (1, 2, '1'),
    (10, 2, '1010'),
    (10, 3, '101'),
    (10, 4, '22'),
    (10, 5, '20'),
    (10, 6, '14'),
    (10, 7, '13'),
    (10, 8, '12'),
    (10, 9, '11')
])
def test_change_base_parametrized(number, base, expected):
    assert change_base(number, base) == expected

def test_change_base_single_digit():
    for i in range(10):
        assert change_base(i, 2) == bin(i)[2:]

def test_change_base_zero():
    assert change_base(0, 2) == '0'
    assert change_base(0, 3) == '0'
    assert change_base(0, 10) == '0'