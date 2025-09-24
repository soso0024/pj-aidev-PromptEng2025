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

def digits(n):
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

def test_single_odd_digit():
    assert digits(1) == 1
    assert digits(3) == 3
    assert digits(5) == 5
    assert digits(7) == 7
    assert digits(9) == 9

def test_single_even_digit():
    assert digits(2) == 0
    assert digits(4) == 0
    assert digits(6) == 0
    assert digits(8) == 0
    assert digits(0) == 0

def test_multiple_digits_with_odds():
    assert digits(235) == 15
    assert digits(13) == 3
    assert digits(579) == 315
    assert digits(1357) == 105

def test_multiple_digits_all_even():
    assert digits(24) == 0
    assert digits(2468) == 0
    assert digits(2020) == 0
    assert digits(8642) == 0

def test_mixed_digits_with_zeros():
    assert digits(102) == 1
    assert digits(305) == 15
    assert digits(1000) == 1
    assert digits(2030) == 3

def test_large_numbers():
    assert digits(123456789) == 945
    assert digits(1111) == 1
    assert digits(2222) == 0
    assert digits(13579) == 945

def test_numbers_with_repeated_odd_digits():
    assert digits(111) == 1
    assert digits(333) == 27
    assert digits(555) == 125
    assert digits(1313) == 9

def test_numbers_starting_with_zero():
    assert digits(10) == 1
    assert digits(20) == 0
    assert digits(101) == 1
    assert digits(202) == 0

@pytest.mark.parametrize("input_n,expected", [
    (1, 1),
    (4, 0),
    (235, 15),
    (12, 1),
    (246, 0),
    (135, 15),
    (97531, 945),
    (2468, 0),
    (10203, 3),
    (99, 81)
])
def test_parametrized_cases(input_n, expected):
    assert digits(input_n) == expected
