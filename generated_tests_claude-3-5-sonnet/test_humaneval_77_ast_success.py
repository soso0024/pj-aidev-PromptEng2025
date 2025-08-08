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
    assert iscube(8) == True
    assert iscube(27) == True
    assert iscube(64) == True
    assert iscube(125) == True

def test_iscube_negative_cubes():
    assert iscube(-8) == True
    assert iscube(-27) == True
    assert iscube(-64) == True

def test_iscube_non_cubes():
    assert iscube(7) == False
    assert iscube(10) == False
    assert iscube(100) == False

@pytest.mark.parametrize("input_val,expected", [
    (0, True),
    (1, True),
    (-1, True),
    (1000, True),
    (-1000, True),
    (12, False),
    (-12, False),
    (99, False)
])
def test_iscube_parametrized(input_val, expected):
    assert iscube(input_val) == expected

def test_iscube_large_numbers():
    assert iscube(1000000) == True  # 100^3
    assert iscube(1000001) == False

def test_iscube_floating_point():
    assert iscube(8.0) == True
    assert iscube(8.1) == False
    assert iscube(-8.0) == True

def test_iscube_near_cubes():
    assert iscube(26.99999) == False
    assert iscube(27.00001) == False

@pytest.mark.parametrize("input_val", [
    "string",
    None,
    [],
    {},
    (1, 2)
])
def test_iscube_invalid_inputs(input_val):
    with pytest.raises((TypeError, ValueError)):
        iscube(input_val)
