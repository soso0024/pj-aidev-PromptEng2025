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

def test_single_digit_odd():
    assert digits(1) == 1
    assert digits(3) == 3
    assert digits(5) == 5
    assert digits(7) == 7
    assert digits(9) == 9

def test_single_digit_even():
    assert digits(2) == 0
    assert digits(4) == 0
    assert digits(6) == 0
    assert digits(8) == 0
    assert digits(0) == 0

def test_multiple_digits():
    assert digits(123) == 3
    assert digits(235) == 15
    assert digits(246) == 0
    assert digits(135) == 15
    assert digits(999) == 729

def test_large_numbers():
    assert digits(12345) == 15
    assert digits(98765) == 315
    assert digits(24680) == 0
    assert digits(11111) == 1

@pytest.mark.parametrize("input_n,expected", [
    (1, 1),
    (4, 0),
    (235, 15),
    (246, 0),
    (999, 729),
    (12345, 15),
    (24680, 0),
    (11111, 1),
    (9876543, 945),
])
def test_digits_parametrized(input_n, expected):
    assert digits(input_n) == expected

def test_edge_cases():
    assert digits(1000000001) == 1
    assert digits(2468642) == 0
    assert digits(1357913) == 2835

def test_consecutive_odds():
    assert digits(111) == 1
    assert digits(333) == 27
    assert digits(555) == 125
    assert digits(135135) == 225

def test_consecutive_evens():
    assert digits(222) == 0
    assert digits(444) == 0
    assert digits(666) == 0
    assert digits(888) == 0

def test_alternating_digits():
    assert digits(121212) == 1
    assert digits(454545) == 125
    assert digits(898989) == 729