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

@pytest.mark.parametrize("x, y, expected", [
    (12, 15, 14),
    (13, 13, -1),
    (1, 4, 4),
    (2, 2, 2),
    (3, 3, -1),
    (1, 1000, 1000),
    (999, 1000, 1000),
    (1000, 999, -1),
    (1, 2, 2),
    (2, 3, 2),
    (3, 4, 4),
    (13, 12, -1),
    (100, 200, 200),
    (201, 201, -1),
    (200, 200, 200),
])
def test_choose_num_parametrized(x, y, expected):
    assert choose_num(x, y) == expected

def test_choose_num_equal_odd_numbers():
    assert choose_num(3, 3) == -1

def test_choose_num_equal_even_numbers():
    assert choose_num(4, 4) == 4

def test_choose_num_reversed_range():
    assert choose_num(10, 5) == -1

def test_choose_num_consecutive_numbers():
    assert choose_num(7, 8) == 8

def test_choose_num_all_odd_range():
    assert choose_num(3, 5) == 4

def test_choose_num_large_numbers():
    assert choose_num(1000, 2000) == 2000

def test_choose_num_minimal_range():
    assert choose_num(1, 2) == 2
