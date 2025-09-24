# Test cases for HumanEval/131
# Generated using Claude API


def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """

    product = 1
    odd_count = 0
    for digit in str(n):
        int_digit = int(digit)
        if int_digit%2 == 1:
            product= product*int_digit
            odd_count+=1
    if odd_count ==0:
        return 0
    else:
        return product


# Generated test cases:
import pytest
from solution import digits

@pytest.mark.parametrize("n, expected", [
    (123, 27),
    (12345, 120),
    (6789, 945),
    (2468, 0),
    (0, 0),
    (-123, 27),
    (1.23, 6),
    ("abc", ValueError),
    ([1, 2, 3], TypeError),
    ({1: 2}, TypeError),
])
def test_digits(n, expected):
    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            digits(n)
    else:
        assert digits(n) == expected

def test_digits_zero_odd_digits():
    assert digits(2468) == 0

def test_digits_negative_number():
    assert digits(-123) == 27

def test_digits_float_input():
    assert digits(1.23) == 6

def test_digits_string_input():
    with pytest.raises(ValueError):
        digits("abc")

def test_digits_list_input():
    with pytest.raises(TypeError):
        digits([1, 2, 3])

def test_digits_dict_input():
    with pytest.raises(TypeError):
        digits({1: 2})