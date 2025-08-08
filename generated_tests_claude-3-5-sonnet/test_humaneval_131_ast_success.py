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

def test_digits_single_digit():
    assert digits(5) == 5
    assert digits(2) == 0
    assert digits(9) == 9

def test_digits_multiple_digits():
    assert digits(123) == 3
    assert digits(456) == 5
    assert digits(789) == 63

def test_digits_no_odd():
    assert digits(2468) == 0
    assert digits(20) == 0

def test_digits_all_odd():
    assert digits(135) == 15
    assert digits(777) == 343

def test_digits_mixed():
    assert digits(12345) == 15
    assert digits(98765) == 315

def test_digits_zero():
    assert digits(0) == 0

def test_digits_large_numbers():
    assert digits(1000001) == 1
    assert digits(9999999) == 9**7

@pytest.mark.parametrize("input_num,expected", [
    (123, 3),
    (246, 0),
    (135, 15),
    (777, 343),
    (2468, 0),
    (11111, 1),
    (98765, 315),
    (0, 0),
    (5, 5)
])
def test_digits_parametrized(input_num, expected):
    assert digits(input_num) == expected

def test_digits_single_even():
    assert digits(2) == 0
    assert digits(4) == 0
    assert digits(6) == 0
    assert digits(8) == 0

def test_digits_single_odd():
    assert digits(1) == 1
    assert digits(3) == 3
    assert digits(5) == 5
    assert digits(7) == 7
    assert digits(9) == 9