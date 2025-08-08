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

def test_iscube_positive_cubes():
    assert iscube(1) == True
    assert iscube(8) == True
    assert iscube(27) == True
    assert iscube(64) == True
    assert iscube(125) == True

def test_iscube_negative_cubes():
    assert iscube(-1) == True
    assert iscube(-8) == True
    assert iscube(-27) == True

def test_iscube_zero():
    assert iscube(0) == True

def test_iscube_non_cubes():
    assert iscube(2) == False
    assert iscube(3) == False
    assert iscube(180) == False
    assert iscube(7) == False

@pytest.mark.parametrize("input,expected", [
    (1, True),
    (8, True),
    (27, True),
    (64, True),
    (125, True),
    (-1, True),
    (-8, True),
    (-27, True),
    (0, True),
    (2, False),
    (3, False),
    (180, False),
    (7, False)
])
def test_iscube_parametrized(input, expected):
    assert iscube(input) == expected

def test_large_cubes():
    assert iscube(1000000) == True
    assert iscube(1000001) == False
