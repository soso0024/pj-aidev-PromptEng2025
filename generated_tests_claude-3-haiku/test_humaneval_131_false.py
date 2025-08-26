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

def test_digits_positive_number():
    assert digits(1234) == 24
    assert digits(579) == 63
    assert digits(13579) == 945

def test_digits_negative_number():
    assert digits(-1234) == 24
    assert digits(-579) == 63
    assert digits(-13579) == 945

def test_digits_zero():
    assert digits(0) == 0

def test_digits_single_digit_odd():
    assert digits(7) == 7

def test_digits_single_digit_even():
    assert digits(4) == 0

def test_digits_all_even_digits():
    assert digits(2468) == 0

@pytest.mark.parametrize("input_value,expected", [
    ('abc', TypeError),
    (None, TypeError),
    ([1, 2, 3], TypeError)
])
def test_digits_invalid_input(input_value, expected):
    with pytest.raises(expected):
        digits(str(input_value))