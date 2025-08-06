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

@pytest.mark.parametrize("input_n,expected", [
    (1, 1),
    (4, 0),
    (235, 15),
    (2468, 0),
    (13579, 945),
    (1111, 1),
    (2222, 0),
    (9, 9),
    (10, 1),
    (100, 1),
    (999, 729),
    (246810, 1),
    (135791, 945),
])
def test_digits_normal_cases(input_n, expected):
    assert digits(input_n) == expected

@pytest.mark.parametrize("input_n", [
    0,
    1,
    9,
    10,
    99,
    100,
    999,
    1000,
    9999,
])
def test_digits_positive_input(input_n):
    result = digits(input_n)
    assert isinstance(result, int)
    assert result >= 0

def test_digits_single_digit():
    assert digits(1) == 1
    assert digits(2) == 0
    assert digits(3) == 3
    assert digits(4) == 0
    assert digits(5) == 5
    assert digits(6) == 0
    assert digits(7) == 7
    assert digits(8) == 0
    assert digits(9) == 9

def test_digits_all_even():
    assert digits(2) == 0
    assert digits(24) == 0
    assert digits(2468) == 0
    assert digits(86420) == 0

def test_digits_all_odd():
    assert digits(1) == 1
    assert digits(35) == 15
    assert digits(357) == 105
    assert digits(13579) == 945

@pytest.mark.parametrize("input_n", [
    123456789,
    987654321,
    112233445,
    998877665,
])
def test_digits_large_numbers(input_n):
    result = digits(input_n)
    assert isinstance(result, int)
    assert result >= 0