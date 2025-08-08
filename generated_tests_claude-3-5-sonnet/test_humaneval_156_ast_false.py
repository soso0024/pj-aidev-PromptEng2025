# Test cases for HumanEval/156
# Generated using Claude API


def int_to_mini_roman(number):
    """
    Given a positive integer, obtain its roman numeral equivalent as a string,
    and return it in lowercase.
    Restrictions: 1 <= num <= 1000

    Examples:
    >>> int_to_mini_roman(19) == 'xix'
    >>> int_to_mini_roman(152) == 'clii'
    >>> int_to_mini_roman(426) == 'cdxxvi'
    """

    num = [1, 4, 5, 9, 10, 40, 50, 90,  
           100, 400, 500, 900, 1000] 
    sym = ["I", "IV", "V", "IX", "X", "XL",  
           "L", "XC", "C", "CD", "D", "CM", "M"] 
    i = 12
    res = ''
    while number: 
        div = number // num[i] 
        number %= num[i] 
        while div: 
            res += sym[i] 
            div -= 1
        i -= 1
    return res.lower()


# Generated test cases:
import pytest

def test_basic_numbers():
    assert int_to_mini_roman(1) == "i"
    assert int_to_mini_roman(4) == "iv"
    assert int_to_mini_roman(5) == "v"
    assert int_to_mini_roman(9) == "ix"
    assert int_to_mini_roman(10) == "x"

@pytest.mark.parametrize("number,expected", [
    (1, "i"),
    (2, "ii"),
    (3, "iii"),
    (4, "iv"),
    (5, "v"),
    (6, "vi"),
    (7, "vii"),
    (8, "viii"),
    (9, "ix"),
    (10, "x"),
    (40, "xl"),
    (50, "l"),
    (90, "xc"),
    (100, "c"),
    (400, "cd"),
    (500, "d"),
    (900, "cm"),
    (1000, "m")
])
def test_roman_numerals(number, expected):
    assert int_to_mini_roman(number) == expected

def test_complex_numbers():
    with pytest.raises(ValueError):
        int_to_mini_roman(0)
    with pytest.raises(ValueError):
        int_to_mini_roman(-1)
    with pytest.raises(ValueError):
        int_to_mini_roman(1001)

def test_edge_cases():
    assert int_to_mini_roman(1) == "i"
    assert int_to_mini_roman(1000) == "m"
    assert int_to_mini_roman(444) == "cdxliv"
    assert int_to_mini_roman(999) == "cmxcix"

def test_repeated_numerals():
    assert int_to_mini_roman(3) == "iii"
    assert int_to_mini_roman(30) == "xxx"
    assert int_to_mini_roman(300) == "ccc"

def test_invalid_inputs():
    invalid_inputs = [0, -1, -42, 1001, 2000, 3000, 4000]
    for number in invalid_inputs:
        with pytest.raises(ValueError):
            int_to_mini_roman(number)

def test_special_cases():
    assert int_to_mini_roman(49) == "xlix"
    assert int_to_mini_roman(99) == "xcix"
    assert int_to_mini_roman(499) == "cdxcix"
    assert int_to_mini_roman(999) == "cmxcix"