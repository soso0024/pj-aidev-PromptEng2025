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
    assert choose_num(3, 5) == 4
    assert choose_num(2, 4) == 4
    assert choose_num(1, 3) == 2

def test_choose_num_edge_cases():
    assert choose_num(5, 5) == -1
    assert choose_num(10, 5) == -1
    assert choose_num(1, 2) == 2

def test_choose_num_error_handling():
    with pytest.raises(TypeError):
        choose_num("a", "b")
    with pytest.raises(TypeError):
        choose_num(1.5, 2.5)

@pytest.mark.parametrize("x,y,expected", [
    (3, 5, 4),
    (2, 4, 4),
    (1, 3, 2),
    (5, 5, -1),
    (10, 5, -1),
    (1, 2, 2),
    ("a", "b", TypeError),
    (1.5, 2.5, TypeError)
])
def test_choose_num_all_cases(x, y, expected):
    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            choose_num(x, y)
    else:
        assert choose_num(x, y) == expected