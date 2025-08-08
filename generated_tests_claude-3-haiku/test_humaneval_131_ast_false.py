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
from solution import digits

import pytest

@pytest.mark.parametrize("n, expected", [
    (123, 27),
    (12345, 120),
    (6789, 567),
    (0, 0),
    (-123, 0),
    (1, 1),
    (2, 0),
    (10, 0),
    (11, 1),
    (101, 1),
    (1001, 1),
])
def test_digits(n, expected):
    assert digits(n) == expected

def test_digits_zero_input():
    assert digits(0) == 0

def test_digits_negative_input():
    assert digits(-123) == 0

def test_digits_single_digit_odd():
    assert digits(7) == 7

def test_digits_single_digit_even():
    assert digits(2) == 0

def test_digits_all_digits_even():
    assert digits(2468) == 0

def test_digits_all_digits_odd():
    assert digits(13579) == 945