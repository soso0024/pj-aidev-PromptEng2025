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

def test_choose_num_valid_range():
    assert choose_num(12, 15) == 14
    assert choose_num(10, 14) == 14
    assert choose_num(8, 12) == 12

def test_choose_num_invalid_range():
    assert choose_num(13, 12) == -1
    assert choose_num(11, 11) == -1

def test_choose_num_negative_inputs():
    assert choose_num(-5, 10) == -1
    assert choose_num(10, -5) == -1
    assert choose_num(-10, -5) == -1

def test_choose_num_zero_inputs():
    assert choose_num(0, 10) == 0
    assert choose_num(10, 0) == -1
    assert choose_num(0, 0) == -1

@pytest.mark.parametrize("x,y,expected", [
    (12, 15, 14),
    (10, 14, 14),
    (8, 12, 12),
    (13, 12, -1),
    (11, 11, -1),
    (-5, 10, -1),
    (10, -5, -1),
    (-10, -5, -1),
    (0, 10, 0),
    (10, 0, -1),
    (0, 0, -1)
])
def test_choose_num_parametrized(x, y, expected):
    assert choose_num(x, y) == expected