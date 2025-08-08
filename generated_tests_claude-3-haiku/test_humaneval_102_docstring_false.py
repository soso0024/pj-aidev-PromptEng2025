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
from your_module import choose_num
import pytest

@pytest.mark.parametrize("x, y, expected", [
    (12, 15, 14),
    (13, 12, -1),
    (10, 10, -1),
    (5, 8, 8),
    (8, 5, -1),
    (0, 10, 8),
    (10, 0, -1),
    (5, 5, 4),
    (5, -5, -1)
])
def test_choose_num(x, y, expected):
    assert choose_num(x, y) == expected

def test_choose_num_type_error():
    with pytest.raises(TypeError):
        choose_num("a", "b")

def test_choose_num_value_error():
    with pytest.raises(ValueError):
        choose_num(-1, 10)
        choose_num(10, -1)