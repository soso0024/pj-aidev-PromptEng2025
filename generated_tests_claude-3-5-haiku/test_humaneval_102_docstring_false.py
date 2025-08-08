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

def test_choose_num_normal_cases():
    assert choose_num(12, 15) == 14
    assert choose_num(10, 20) == 20
    assert choose_num(11, 19) == 18

def test_choose_num_edge_cases():
    assert choose_num(13, 12) == -1
    assert choose_num(10, 10) == -1
    assert choose_num(11, 11) == -1

@pytest.mark.parametrize("x,y,expected", [
    (12, 15, 14),
    (10, 20, 20),
    (11, 19, 18),
    (13, 12, -1),
    (10, 10, -1),
    (11, 11, -1),
    (0, 10, 10),
    (1, 9, 8),
    (100, 200, 200)
])
def test_choose_num_parametrized(x, y, expected):
    assert choose_num(x, y) == expected

def test_choose_num_large_numbers():
    assert choose_num(1000000, 2000000) == 2000000

def test_choose_num_negative_numbers():
    assert choose_num(-10, 10) == 10
    assert choose_num(-20, -10) == -1