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
    assert choose_num(1, 4) == 4
    assert choose_num(2, 8) == 8

def test_choose_num_x_equals_y():
    assert choose_num(5, 5) == -1
    assert choose_num(3, 3) == -1

def test_choose_num_y_odd():
    assert choose_num(4, 7) == 6
    assert choose_num(1, 3) == 2

@pytest.mark.parametrize("x, y, expected", [
    (1, 2, 2),    # even y
    (2, 3, 2),    # odd y
    (5, 4, -1),   # x > y
    (3, 3, -1),   # x = y
    (0, 1, 0),    # y odd, x = 0
    (1, 10, 10),  # large even y
    (1, 9, 8),    # large odd y
    (0, 0, 0),    # x = y = 0
])
def test_choose_num_parametrized(x, y, expected):
    assert choose_num(x, y) == expected

@pytest.mark.parametrize("x, y", [
    (-1, 5),
    (5, -1),
    (-2, -2),
])
def test_choose_num_negative_inputs(x, y):
    result = choose_num(x, y)
    assert isinstance(result, int)

def test_choose_num_zero_inputs():
    assert choose_num(0, 2) == 2
    assert choose_num(0, 1) == 0

def test_choose_num_sequential_numbers():
    assert choose_num(1, 2) == 2
    assert choose_num(2, 3) == 2
    assert choose_num(3, 4) == 4

def test_choose_num_large_numbers():
    assert choose_num(100, 1000) == 1000
    assert choose_num(999, 1001) == 1000
