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

@pytest.mark.parametrize("input_val,expected", [
    (1, True),
    (2, False),
    (-1, True),
    (64, True),
    (0, True),
    (180, False),
    (8, True),
    (27, True),
    (-8, True),
    (-27, True),
    (100, False),
    (1000, True),
    (-1000, True),
    (999, False),
    (125, True),
    (-125, True),
    (216, True),
    (-216, True),
    (10, False),
    (50, False),
    (512, True),
    (-512, True)
])
def test_iscube_parametrized(input_val, expected):
    assert iscube(input_val) == expected

def test_iscube_large_numbers():
    assert iscube(1000000) == True
    assert iscube(-1000000) == True
    assert iscube(1000001) == False

def test_iscube_small_numbers():
    assert iscube(1) == True
    assert iscube(-1) == True
    assert iscube(0) == True

def test_iscube_perfect_cubes():
    for i in range(-5, 6):
        assert iscube(i**3) == True

def test_iscube_non_cubes():
    non_cubes = [2, 3, 4, 5, 6, 7, 9, 10]
    for i in non_cubes:
        assert iscube(i) == False