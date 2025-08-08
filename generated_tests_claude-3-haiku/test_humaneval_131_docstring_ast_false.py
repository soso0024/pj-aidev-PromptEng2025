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

@pytest.mark.parametrize("n, expected", [
    (1, 1),
    (4, 0),
    (235, 15),
    (0, 0),
    (-1, ValueError),
    (3.14, TypeError),
    ("abc", TypeError)
])
def test_digits(n, expected):
    if isinstance(n, (float, str)):
        with pytest.raises(expected):
            digits(n)
    elif n < 0:
        with pytest.raises(ValueError):
            digits(n)
    else:
        assert digits(n) == expected

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
        if digit.isdigit():
            int_digit = int(digit)
            if int_digit % 2 == 1:
                product *= int_digit
                odd_count += 1
    if odd_count == 0:
        return 0
    else:
        return product