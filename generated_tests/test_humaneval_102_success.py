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
    assert choose_num(3, 7) == 6
    assert choose_num(1, 2) == 2
    assert choose_num(10, 15) == 14

@pytest.mark.parametrize("x, y, expected", [
    (5, 5, -1),      # Equal numbers
    (6, 4, -1),      # x > y
    (1, 10, 10),     # Even y
    (3, 9, 8),       # Odd y
    (0, 2, 2),       # Zero x
    (1, 1, -1),      # Minimum equal numbers
    (10, 20, 20),    # Larger even numbers
    (9, 11, 10),     # Consecutive odd numbers
    (8, 9, 8),       # Consecutive numbers
    (100, 99, -1),   # x > y with larger numbers
])
def test_choose_num_parametrized(x, y, expected):
    assert choose_num(x, y) == expected

def test_choose_num_edge_cases():
    assert choose_num(0, 0) == 0
    assert choose_num(-1, 1) == 0
    assert choose_num(-10, -5) == -6
    assert choose_num(-5, -5) == -1

def test_choose_num_large_numbers():
    assert choose_num(1000, 2000) == 2000
    assert choose_num(9999, 10001) == 10000
    assert choose_num(10000, 9999) == -1

def test_choose_num_consecutive_numbers():
    assert choose_num(1, 2) == 2
    assert choose_num(2, 3) == 2
    assert choose_num(3, 4) == 4
    assert choose_num(4, 5) == 4