# Test cases for HumanEval/77
# Generated using Claude API


def iscube(a):
    '''
    Write a function that takes an integer a and returns True 
    if this ingeger is a cube of some integer number.
    Note: you may assume the input is always valid.
    Examples:
    iscube(1) ==> True
    iscube(2) ==> False
    iscube(-1) ==> True
    iscube(64) ==> True
    iscube(0) ==> True
    iscube(180) ==> False
    '''

    a = abs(a)
    return int(round(a ** (1. / 3))) ** 3 == a


# Generated test cases:
import pytest
from math import pow

@pytest.mark.parametrize("input,expected", [
    (1, True),
    (2, False),
    (-1, True),
    (64, True),
    (0, True),
    (180, False),
    (-8, True),
    (125, True),
    (0.5, False),
    (0, True),
    (1000, False),
    (-1000, True)
])
def test_iscube(input, expected):
    assert iscube(input) == expected