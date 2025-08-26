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

def test_int_to_mini_roman_basic_cases():
    assert int_to_mini_roman(19) == 'xix'
    assert int_to_mini_roman(152) == 'clii'
    assert int_to_mini_roman(426) == 'cdxxvi'

@pytest.mark.parametrize("number,expected", [
    (1, 'i'),
    (4, 'iv'),
    (5, 'v'),
    (9, 'ix'),
    (10, 'x'),
    (40, 'xl'),
    (50, 'l'),
    (90, 'xc'),
    (100, 'c'),
    (400, 'cd'),
    (500, 'd'),
    (900, 'cm'),
    (1000, 'm')
])
def test_int_to_mini_roman_standard_conversions(number, expected):
    assert int_to_mini_roman(number) == expected

def test_int_to_mini_roman_edge_cases():
    assert int_to_mini_roman(1) == 'i'
    assert int_to_mini_roman(1000) == 'm'

def test_int_to_mini_roman_complex_numbers():
    assert int_to_mini_roman(444) == 'cdxliv'
    assert int_to_mini_roman(999) == 'cmxcix'
    assert int_to_mini_roman(777) == 'dcclxxvii'

def test_int_to_mini_roman_invalid_input():
    with pytest.raises(ValueError):
        int_to_mini_roman(0)
    with pytest.raises(ValueError):
        int_to_mini_roman(1001)
    with pytest.raises(ValueError):
        int_to_mini_roman(-5)

def int_to_mini_roman(number):
    if number < 1 or number > 1000:
        raise ValueError("Input must be between 1 and 1000")

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