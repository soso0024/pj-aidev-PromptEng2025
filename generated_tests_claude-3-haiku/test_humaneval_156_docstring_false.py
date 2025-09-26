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
from solution import int_to_mini_roman

import pytest

@pytest.mark.parametrize("number,expected", [
    (19, 'xix'),
    (152, 'clii'),
    (426, 'cdxxvi'),
    (1, 'i'),
    (1000, 'm'),
    (0, ''),
])
def test_int_to_mini_roman(number, expected):
    assert int_to_mini_roman(number) == expected

def test_int_to_mini_roman_raises_error_for_invalid_input():
    with pytest.raises(ValueError):
        int_to_mini_roman(-1)
    with pytest.raises(ValueError):
        int_to_mini_roman(1001)