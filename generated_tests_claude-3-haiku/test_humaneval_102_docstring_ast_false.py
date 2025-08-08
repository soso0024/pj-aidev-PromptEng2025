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
    assert choose_num(10, 12) == 12
    assert choose_num(4, 8) == 8

def test_choose_num_invalid_range():
    assert choose_num(13, 12) == -1
    assert choose_num(7, 7) == -1

def test_choose_num_negative_inputs():
    assert choose_num(-5, 5) == -1
    assert choose_num(5, -5) == -1

@pytest.mark.parametrize("x,y,expected", [
    (12, 15, 14),
    (10, 12, 12),
    (4, 8, 8),
    (13, 12, -1),
    (7, 7, -1),
    (-5, 5, -1),
    (5, -5, -1)
])
def test_choose_num_all_cases(x, y, expected):
    assert choose_num(x, y) == expected

def choose_num(x, y):
    if x > y:
        return -1
    if y % 2 == 0:
        return y
    if x == y:
        return -1
    return y - 1