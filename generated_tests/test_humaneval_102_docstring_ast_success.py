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

def test_choose_num_basic():
    assert choose_num(12, 15) == 14
    assert choose_num(1, 4) == 4
    assert choose_num(2, 2) == 2

@pytest.mark.parametrize("x, y, expected", [
    (12, 15, 14),
    (13, 12, -1),
    (1, 1, -1),
    (2, 2, 2),
    (1, 4, 4),
    (3, 5, 4),
    (10, 20, 20),
    (11, 11, -1),
    (1, 2, 2),
    (2, 3, 2),
])
def test_choose_num_parametrized(x, y, expected):
    assert choose_num(x, y) == expected

def test_choose_num_edge_cases():
    assert choose_num(999999, 1000000) == 1000000
    assert choose_num(1000000, 999999) == -1
    assert choose_num(1, 1) == -1
    assert choose_num(2, 2) == 2

def test_choose_num_consecutive_numbers():
    assert choose_num(1, 2) == 2
    assert choose_num(2, 3) == 2
    assert choose_num(3, 4) == 4

def test_choose_num_odd_range():
    assert choose_num(3, 5) == 4
    assert choose_num(5, 7) == 6
    assert choose_num(7, 9) == 8

def test_choose_num_even_range():
    assert choose_num(2, 4) == 4
    assert choose_num(4, 6) == 6
    assert choose_num(6, 8) == 8

def test_choose_num_same_numbers():
    assert choose_num(1, 1) == -1
    assert choose_num(2, 2) == 2
    assert choose_num(3, 3) == -1
    assert choose_num(4, 4) == 4

def test_choose_num_no_even():
    assert choose_num(1, 1) == -1
    assert choose_num(3, 3) == -1
    assert choose_num(5, 5) == -1
