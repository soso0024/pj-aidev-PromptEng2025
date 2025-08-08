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

def test_digits_single_odd_digit():
    assert digits(1) == 1
    assert digits(3) == 3
    assert digits(5) == 5
    assert digits(7) == 7
    assert digits(9) == 9

def test_digits_single_even_digit():
    assert digits(2) == 0
    assert digits(4) == 0
    assert digits(6) == 0
    assert digits(8) == 0

def test_digits_multiple_odd_digits():
    assert digits(135) == 15
    assert digits(357) == 105
    assert digits(579) == 315

def test_digits_mixed_digits():
    assert digits(246) == 0
    assert digits(1357) == 105
    assert digits(2468) == 0

def test_digits_large_numbers():
    assert digits(123456789) == 945
    assert digits(987654321) == 945

def test_digits_zero():
    assert digits(0) == 0

@pytest.mark.parametrize("input,expected", [
    (1, 1),
    (4, 0),
    (235, 15),
    (135, 15),
    (246, 0),
    (357, 105),
    (579, 315),
    (123456789, 945),
    (987654321, 945),
    (0, 0)
])
def test_digits_parametrized(input, expected):
    assert digits(input) == expected
