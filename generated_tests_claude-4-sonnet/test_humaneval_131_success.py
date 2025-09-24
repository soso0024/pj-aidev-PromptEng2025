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

@pytest.mark.parametrize("n,expected", [
    (1, 1),
    (3, 3),
    (5, 5),
    (7, 7),
    (9, 9),
    (13, 3),
    (15, 5),
    (17, 7),
    (19, 9),
    (135, 15),
    (357, 105),
    (1357, 105),
    (13579, 945),
    (2, 0),
    (4, 0),
    (6, 0),
    (8, 0),
    (0, 0),
    (24, 0),
    (246, 0),
    (2468, 0),
    (10, 1),
    (12, 1),
    (14, 1),
    (16, 1),
    (18, 1),
    (20, 0),
    (21, 1),
    (23, 3),
    (25, 5),
    (27, 7),
    (29, 9),
    (123, 3),
    (234, 3),
    (345, 15),
    (456, 5),
    (567, 35),
    (678, 7),
    (789, 63),
    (1234, 3),
    (2345, 15),
    (3456, 15),
    (4567, 35),
    (5678, 35),
    (6789, 63),
    (12345, 15),
    (23456, 15),
    (34567, 105),
    (45678, 35),
    (56789, 315),
    (123456, 15),
    (234567, 105),
    (345678, 105),
    (456789, 315),
    (1234567, 105),
    (2345678, 105),
    (3456789, 945),
    (12345678, 105),
    (23456789, 945),
    (123456789, 945),
    (1000, 1),
    (2000, 0),
    (1001, 1),
    (1010, 1),
    (1100, 1),
    (2002, 0),
    (2020, 0),
    (2200, 0),
    (101, 1),
    (111, 1),
    (131, 3),
    (151, 5),
    (171, 7),
    (191, 9),
    (313, 9),
    (515, 25),
    (717, 49),
    (919, 81),
])
def test_digits(n, expected):
    assert digits(n) == expected

def test_single_digit_odd():
    assert digits(1) == 1
    assert digits(3) == 3
    assert digits(5) == 5
    assert digits(7) == 7
    assert digits(9) == 9

def test_single_digit_even():
    assert digits(0) == 0
    assert digits(2) == 0
    assert digits(4) == 0
    assert digits(6) == 0
    assert digits(8) == 0

def test_all_even_digits():
    assert digits(24) == 0
    assert digits(246) == 0
    assert digits(2468) == 0
    assert digits(24680) == 0

def test_all_odd_digits():
    assert digits(13) == 3
    assert digits(135) == 15
    assert digits(1357) == 105
    assert digits(13579) == 945

def test_mixed_digits():
    assert digits(123) == 3
    assert digits(1234) == 3
    assert digits(12345) == 15
    assert digits(123456) == 15

def test_zeros_in_number():
    assert digits(101) == 1
    assert digits(1001) == 1
    assert digits(10203) == 3
    assert digits(102030) == 3

def test_large_numbers():
    assert digits(987654321) == 945
    assert digits(1111111111) == 1
    assert digits(1357913579) == 893025