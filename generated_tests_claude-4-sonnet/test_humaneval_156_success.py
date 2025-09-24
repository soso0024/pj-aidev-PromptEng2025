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

def int_to_mini_roman(number):
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
    (11, "xi"),
    (14, "xiv"),
    (15, "xv"),
    (19, "xix"),
    (20, "xx"),
    (27, "xxvii"),
    (40, "xl"),
    (44, "xliv"),
    (49, "xlix"),
    (50, "l"),
    (58, "lviii"),
    (90, "xc"),
    (94, "xciv"),
    (99, "xcix"),
    (100, "c"),
    (400, "cd"),
    (444, "cdxliv"),
    (500, "d"),
    (900, "cm"),
    (994, "cmxciv"),
    (1000, "m"),
    (1994, "mcmxciv"),
    (3999, "mmmcmxcix")
])
def test_int_to_mini_roman_valid_numbers(number, expected):
    assert int_to_mini_roman(number) == expected

def test_int_to_mini_roman_edge_cases():
    assert int_to_mini_roman(1) == "i"
    assert int_to_mini_roman(3999) == "mmmcmxcix"

def test_int_to_mini_roman_subtractive_notation():
    assert int_to_mini_roman(4) == "iv"
    assert int_to_mini_roman(9) == "ix"
    assert int_to_mini_roman(40) == "xl"
    assert int_to_mini_roman(90) == "xc"
    assert int_to_mini_roman(400) == "cd"
    assert int_to_mini_roman(900) == "cm"

def test_int_to_mini_roman_complex_numbers():
    assert int_to_mini_roman(1984) == "mcmlxxxiv"
    assert int_to_mini_roman(2023) == "mmxxiii"
    assert int_to_mini_roman(3456) == "mmmcdlvi"

def test_int_to_mini_roman_hundreds():
    assert int_to_mini_roman(100) == "c"
    assert int_to_mini_roman(200) == "cc"
    assert int_to_mini_roman(300) == "ccc"
    assert int_to_mini_roman(500) == "d"
    assert int_to_mini_roman(600) == "dc"
    assert int_to_mini_roman(700) == "dcc"
    assert int_to_mini_roman(800) == "dccc"

def test_int_to_mini_roman_tens():
    assert int_to_mini_roman(10) == "x"
    assert int_to_mini_roman(20) == "xx"
    assert int_to_mini_roman(30) == "xxx"
    assert int_to_mini_roman(50) == "l"
    assert int_to_mini_roman(60) == "lx"
    assert int_to_mini_roman(70) == "lxx"
    assert int_to_mini_roman(80) == "lxxx"

def test_int_to_mini_roman_thousands():
    assert int_to_mini_roman(1000) == "m"
    assert int_to_mini_roman(2000) == "mm"
    assert int_to_mini_roman(3000) == "mmm"
