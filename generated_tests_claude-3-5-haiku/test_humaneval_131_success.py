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

def test_digits_normal_cases():
    assert digits(1234) == 3
    assert digits(5678) == 35
    assert digits(2468) == 0
    assert digits(13579) == 945

def test_digits_single_digit():
    assert digits(1) == 1
    assert digits(2) == 0
    assert digits(9) == 9

def test_digits_zero():
    assert digits(0) == 0

def test_digits_large_numbers():
    assert digits(123456789) == 945
    assert digits(987654321) == 945

@pytest.mark.parametrize("input_num,expected", [
    (1234, 3),
    (5678, 35),
    (2468, 0),
    (13579, 945),
    (1, 1),
    (2, 0),
    (9, 9),
    (0, 0),
    (123456789, 945),
    (987654321, 945)
])
def test_digits_parametrized(input_num, expected):
    assert digits(input_num) == expected