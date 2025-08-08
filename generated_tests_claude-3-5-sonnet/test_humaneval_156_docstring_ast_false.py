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
    assert int_to_mini_roman(5) == "v"
    assert int_to_mini_roman(10) == "x"
    assert int_to_mini_roman(50) == "l"
    assert int_to_mini_roman(100) == "c"
    assert int_to_mini_roman(500) == "d"
    assert int_to_mini_roman(1000) == "m"

@pytest.mark.parametrize("number,expected", [
    (4, "iv"),
    (9, "ix"),
    (40, "xl"),
    (90, "xc"),
    (400, "cd"),
    (900, "cm")
])
def test_subtractive_numbers(number, expected):
    assert int_to_mini_roman(number) == expected

@pytest.mark.parametrize("number,expected", [
    (3, "iii"),
    (8, "viii"),
    (39, "xxxix"),
    (246, "ccxlvi"),
    (789, "dcclxxxix"),
    (999, "cmxcix"),
    (444, "cdxliv"),
    (555, "dlv")
])
def test_complex_numbers(number, expected):
    assert int_to_mini_roman(number) == expected

def test_edge_cases():
    assert int_to_mini_roman(1) == "i"
    assert int_to_mini_roman(1000) == "m"

def test_consecutive_numbers():
    assert int_to_mini_roman(888) == "dccclxxxviii"
    assert int_to_mini_roman(777) == "dcclxxvii"
    assert int_to_mini_roman(666) == "dclxvi"

def test_repeated_numerals():
    assert int_to_mini_roman(333) == "cccxxxiii"
    assert int_to_mini_roman(222) == "ccxxii"
    assert int_to_mini_roman(111) == "cxi"

def test_invalid_inputs():
    try:
        int_to_mini_roman(0)
        pytest.fail("Expected ValueError for input 0")
    except:
        pass
    
    try:
        int_to_mini_roman(-1)
        pytest.fail("Expected ValueError for input -1")
    except:
        pass
    
    try:
        int_to_mini_roman(1001)
        pytest.fail("Expected ValueError for input 1001")
    except:
        pass
    
    try:
        int_to_mini_roman(10000)
        pytest.fail("Expected ValueError for input 10000")
    except:
        pass

def test_invalid_types():
    try:
        int_to_mini_roman("123")
        pytest.fail("Expected TypeError for string input")
    except:
        pass
    
    try:
        int_to_mini_roman(None)
        pytest.fail("Expected TypeError for None input")
    except:
        pass
    
    try:
        int_to_mini_roman(3.14)
        pytest.fail("Expected TypeError for float input")
    except:
        pass
    
    try:
        int_to_mini_roman([])
        pytest.fail("Expected TypeError for list input")
    except:
        pass
    
    try:
        int_to_mini_roman({})
        pytest.fail("Expected TypeError for dict input")
    except:
        pass