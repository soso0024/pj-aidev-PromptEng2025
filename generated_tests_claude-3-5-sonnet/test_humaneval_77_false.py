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
import math

@pytest.mark.parametrize("number,expected", [
    (0, True),
    (1, True),
    (8, True),
    (27, True),
    (64, True),
    (-8, True),
    (-27, True),
    (-64, True),
    (2, False),
    (9, False),
    (10, False),
    (-10, False),
    (100, False),
    (-100, False),
    (1000000, True),
    (-1000000, True),
    (1000001, False),
    (-1000001, False),
    (0.0, True),
    (8.0, True),
    (8.1, False),
    (-8.0, True),
    (-8.1, False),
    (float('inf'), False),
    (-float('inf'), False)
])
def test_iscube_parametrized(number, expected):
    if isinstance(number, (int, float)) and math.isinf(number):
        with pytest.raises(OverflowError):
            iscube(number)
    else:
        assert iscube(number) == expected

def test_iscube_with_none():
    with pytest.raises(TypeError):
        iscube(None)

def test_iscube_with_string():
    with pytest.raises(TypeError):
        iscube("8")

def test_iscube_with_complex():
    with pytest.raises((TypeError, ValueError)):
        iscube(complex(1, 2))

def test_iscube_with_list():
    with pytest.raises(TypeError):
        iscube([8])

def test_iscube_with_dict():
    with pytest.raises(TypeError):
        iscube({8: 8})