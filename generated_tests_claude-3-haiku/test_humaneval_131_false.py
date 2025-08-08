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

def test_digits_zero():
    assert digits(0) == 0

def test_digits_negative():
    with pytest.raises(ValueError):
        digits(-42)

def test_digits_positive():
    assert digits(12345) == 15

@pytest.mark.parametrize("input,expected", [
    (123, 6),
    (1357, 105),
    (2468, 0),
    (10000, 0),
    (99999, 945)
])
def test_digits_parametrized(input, expected):
    assert digits(input) == expected

def test_digits_string():
    with pytest.raises(ValueError):
        digits("abc")