# Test cases for HumanEval/102
# Generated using Claude API


def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """

    if x > y:
        return -1
    if y % 2 == 0:
        return y
    if x == y:
        return -1
    return y - 1


# Generated test cases:
import pytest

def choose_num(x, y):
    if x > y:
        return -1
    if y % 2 == 0:
        return y
    if x == y:
        return -1
    return y - 1

@pytest.mark.parametrize("x,y,expected", [
    (1, 2, 2),
    (2, 4, 4),
    (3, 6, 6),
    (1, 3, 2),
    (2, 5, 4),
    (4, 7, 6),
    (5, 5, -1),
    (3, 3, -1),
    (7, 7, -1),
    (10, 5, -1),
    (8, 3, -1),
    (15, 10, -1),
    (0, 0, 0),
    (0, 1, 0),
    (0, 2, 2),
    (1, 1, -1),
    (2, 2, 2),
    (-5, -2, -2),
    (-5, -3, -4),
    (-3, -3, -1),
    (-10, -5, -6),
    (-1, 1, 0),
    (-2, 2, 2),
    (100, 101, 100),
    (100, 102, 102),
    (99, 100, 100),
    (99, 101, 100),
    (1000, 1001, 1000),
    (1000, 1002, 1002)
])
def test_choose_num(x, y, expected):
    assert choose_num(x, y) == expected

def test_choose_num_x_greater_than_y():
    assert choose_num(10, 5) == -1
    assert choose_num(100, 50) == -1
    assert choose_num(1, 0) == -1

def test_choose_num_y_even():
    assert choose_num(1, 2) == 2
    assert choose_num(5, 10) == 10
    assert choose_num(0, 4) == 4

def test_choose_num_x_equals_y_odd():
    assert choose_num(1, 1) == -1
    assert choose_num(3, 3) == -1
    assert choose_num(99, 99) == -1

def test_choose_num_x_equals_y_even():
    assert choose_num(2, 2) == 2
    assert choose_num(4, 4) == 4
    assert choose_num(100, 100) == 100

def test_choose_num_y_odd_x_less_than_y():
    assert choose_num(1, 3) == 2
    assert choose_num(2, 5) == 4
    assert choose_num(10, 15) == 14

def test_choose_num_negative_numbers():
    assert choose_num(-5, -2) == -2
    assert choose_num(-5, -3) == -4
    assert choose_num(-3, -3) == -1
    assert choose_num(-2, -5) == -1

def test_choose_num_zero_cases():
    assert choose_num(0, 0) == 0
    assert choose_num(0, 1) == 0
    assert choose_num(0, 2) == 2
    assert choose_num(-1, 0) == 0