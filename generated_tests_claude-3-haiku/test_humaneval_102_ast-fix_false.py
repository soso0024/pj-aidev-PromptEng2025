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

def test_choose_num_x_greater_than_y():
    assert choose_num(10, 5) == -1

def test_choose_num_y_even():
    assert choose_num(5, 6) == 6

def test_choose_num_x_equal_to_y():
    assert choose_num(5, 5) == -1

def test_choose_num_y_odd():
    assert choose_num(5, 7) == 6

@pytest.mark.parametrize("x,y,expected", [
    (10, 5, -1),
    (5, 6, 6),
    (5, 5, -1),
    (5, 7, 6),
    (0, 0, 0),
    (-5, 5, -1),
    (5, -5, -1)
])
def test_choose_num_parametrized(x, y, expected):
    assert choose_num(x, y) == expected

def choose_num(x, y):
    if x > y:
        return -1
    if y % 2 == 0:
        return y
    if x == y:
        return -1
    return y - 1