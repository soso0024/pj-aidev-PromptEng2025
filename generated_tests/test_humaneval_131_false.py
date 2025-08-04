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

def test_digits_basic():
    assert digits(123) == 3
    assert digits(456) == 5

def test_digits_no_odd():
    assert digits(2468) == 0
    assert digits(0) == 0

def test_digits_all_odd():
    assert digits(135) == 15
    assert digits(111) == 1

def test_digits_mixed():
    assert digits(12345) == 15
    assert digits(98765) == 945

def test_digits_single():
    assert digits(1) == 1
    assert digits(2) == 0

def test_digits_large_numbers():
    assert digits(123456789) == 945
    assert digits(999999999) == 387420489

@pytest.mark.parametrize("input_n,expected", [
    (123, 3),
    (456, 5),
    (2468, 0),
    (135, 15),
    (111, 1),
    (2222, 0),
    (9875, 945),
    (1000, 1),
    (2000, 0),
    (9999, 6561)
])
def test_digits_parametrized(input_n, expected):
    assert digits(input_n) == expected

def test_digits_zero():
    assert digits(0) == 0

def test_digits_leading_zeros():
    assert digits(12) == 1
    assert digits(123) == 3

def test_digits_consecutive_odds():
    assert digits(11111) == 1
    assert digits(13579) == 945

def test_digits_consecutive_evens():
    assert digits(2468) == 0
    assert digits(24680) == 0