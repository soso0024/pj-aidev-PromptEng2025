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
    assert int_to_mini_roman(1) == 'i'
    assert int_to_mini_roman(4) == 'iv'
    assert int_to_mini_roman(9) == 'ix'
    assert int_to_mini_roman(14) == 'xiv'
    assert int_to_mini_roman(49) == 'xlix'
    assert int_to_mini_roman(99) == 'xcix'
    assert int_to_mini_roman(500) == 'd'
    assert int_to_mini_roman(999) == 'cmxcix'

@pytest.mark.parametrize("number,expected", [
    (1, 'i'),
    (4, 'iv'),
    (5, 'v'),
    (9, 'ix'),
    (10, 'x'),
    (14, 'xiv'),
    (40, 'xl'),
    (50, 'l'),
    (90, 'xc'),
    (100, 'c'),
    (400, 'cd'),
    (500, 'd'),
    (900, 'cm'),
    (1000, 'm'),
    (3999, 'mmmcmxcix')
])
def test_int_to_mini_roman_parametrized(number, expected):
    assert int_to_mini_roman(number) == expected

def test_int_to_mini_roman_zero():
    with pytest.raises(ValueError):
        int_to_mini_roman(0)

def test_int_to_mini_roman_negative():
    with pytest.raises(ValueError):
        int_to_mini_roman(-1)

def test_int_to_mini_roman_large_number():
    with pytest.raises(ValueError):
        int_to_mini_roman(4000)

def int_to_mini_roman(number):
    if number <= 0 or number >= 4000:
        raise ValueError("Input must be between 1 and 3999")
    
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