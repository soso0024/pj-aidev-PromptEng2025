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
    assert choose_num(3, 6) == 6
    assert choose_num(0, 8) == 8

def test_choose_num_x_equals_y():
    assert choose_num(5, 5) == -1

def test_choose_num_y_odd_not_equal():
    assert choose_num(3, 7) == 6
    assert choose_num(2, 5) == 4

@pytest.mark.parametrize("x,y,expected", [
    (1, 2, 2),
    (3, 6, 6),
    (5, 5, -1),
    (10, 5, -1),
    (2, 7, 6),
    (0, 9, 8),
    (4, 4, 4)
])
def test_choose_num_parametrized(x, y, expected):
    assert choose_num(x, y) == expected