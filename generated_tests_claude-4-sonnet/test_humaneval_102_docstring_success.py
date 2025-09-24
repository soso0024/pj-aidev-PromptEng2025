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
    (12, 15, 14),
    (13, 12, -1),
    (1, 1, -1),
    (2, 2, 2),
    (1, 2, 2),
    (1, 3, 2),
    (1, 4, 4),
    (2, 4, 4),
    (3, 4, 4),
    (5, 5, -1),
    (6, 6, 6),
    (10, 20, 20),
    (11, 20, 20),
    (10, 21, 20),
    (11, 21, 20),
    (1, 100, 100),
    (1, 101, 100),
    (50, 100, 100),
    (51, 100, 100),
    (50, 101, 100),
    (51, 101, 100),
    (100, 50, -1),
    (101, 100, -1),
    (7, 9, 8),
    (8, 9, 8),
    (9, 9, -1),
    (10, 10, 10),
    (15, 17, 16),
    (16, 17, 16),
    (17, 17, -1),
    (18, 18, 18)
])
def test_choose_num(x, y, expected):
    assert choose_num(x, y) == expected

def test_choose_num_edge_cases():
    assert choose_num(1, 1000000) == 1000000
    assert choose_num(1, 999999) == 999998
    assert choose_num(999999, 1000000) == 1000000
    assert choose_num(999999, 999999) == -1
    assert choose_num(1000000, 1000000) == 1000000

def test_choose_num_consecutive_numbers():
    assert choose_num(1, 2) == 2
    assert choose_num(2, 3) == 2
    assert choose_num(3, 4) == 4
    assert choose_num(4, 5) == 4
    assert choose_num(5, 6) == 6

def test_choose_num_same_parity():
    assert choose_num(2, 8) == 8
    assert choose_num(4, 10) == 10
    assert choose_num(1, 9) == 8
    assert choose_num(3, 11) == 10
