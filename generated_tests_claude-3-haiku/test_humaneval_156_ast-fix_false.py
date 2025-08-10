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
    (0, ''),
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
    (1000, 'm'),
    (1994, 'mcmxciv'),
    (3999, 'mcmxcix'),
    (-1, ValueError),
    (4000, ValueError)
])
def test_int_to_mini_roman(number, expected):
    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            int_to_mini_roman(number)
    else:
        assert int_to_mini_roman(number) == expected