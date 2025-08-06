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
import time

def test_basic_numbers():
    assert int_to_mini_roman(1) == 'i'
    assert int_to_mini_roman(5) == 'v'
    assert int_to_mini_roman(10) == 'x'
    assert int_to_mini_roman(50) == 'l'
    assert int_to_mini_roman(100) == 'c'
    assert int_to_mini_roman(500) == 'd'
    assert int_to_mini_roman(1000) == 'm'

@pytest.mark.parametrize("number,expected", [
    (4, "iv"),
    (9, "ix"),
    (40, "xl"),
    (90, "xc"),
    (400, "cd"),
    (900, "cm"),
])
def test_subtractive_numbers(number, expected):
    assert int_to_mini_roman(number) == expected

@pytest.mark.parametrize("number,expected", [
    (3, "iii"),
    (19, "xix"),
    (152, "clii"),
    (426, "cdxxvi"),
    (999, "cmxcix"),
    (2, "ii"),
    (58, "lviii"),
    (144, "cxliv"),
    (678, "dclxxviii"),
])
def test_complex_numbers(number, expected):
    assert int_to_mini_roman(number) == expected

def test_edge_cases():
    assert int_to_mini_roman(1) == 'i'
    assert int_to_mini_roman(1000) == 'm'

@pytest.mark.parametrize("invalid_input", [
    0,
    -1,
    1001,
    10000,
])
def test_invalid_inputs(invalid_input):
    with pytest.raises(ValueError):
        int_to_mini_roman(invalid_input)

def test_type_errors():
    with pytest.raises(TypeError):
        int_to_mini_roman("123")
    with pytest.raises(TypeError):
        int_to_mini_roman(12.34)
    with pytest.raises(TypeError):
        int_to_mini_roman(None)

def test_timeout():
    start = time.time()
    int_to_mini_roman(999)
    duration = time.time() - start
    assert duration < 1.0, f"Function took {duration} seconds, which exceeds the 1 second limit"

if __name__ == '__main__':
    pytest.main([__file__])