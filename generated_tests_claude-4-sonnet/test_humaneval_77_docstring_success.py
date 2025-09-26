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

def iscube(a):
    a = abs(a)
    return int(round(a ** (1. / 3))) ** 3 == a

@pytest.mark.parametrize("input_val,expected", [
    (1, True),
    (2, False),
    (-1, True),
    (64, True),
    (0, True),
    (180, False),
    (8, True),
    (-8, True),
    (27, True),
    (-27, True),
    (125, True),
    (-125, True),
    (216, True),
    (-216, True),
    (343, True),
    (-343, True),
    (512, True),
    (-512, True),
    (729, True),
    (-729, True),
    (1000, True),
    (-1000, True),
    (1331, True),
    (-1331, True),
    (1728, True),
    (-1728, True),
    (2197, True),
    (-2197, True),
    (2744, True),
    (-2744, True),
    (3375, True),
    (-3375, True),
    (4096, True),
    (-4096, True),
    (4913, True),
    (-4913, True),
    (5832, True),
    (-5832, True),
    (6859, True),
    (-6859, True),
    (8000, True),
    (-8000, True),
    (9261, True),
    (-9261, True),
    (10648, True),
    (-10648, True),
    (12167, True),
    (-12167, True),
    (13824, True),
    (-13824, True),
    (15625, True),
    (-15625, True),
    (17576, True),
    (-17576, True),
    (19683, True),
    (-19683, True),
    (21952, True),
    (-21952, True),
    (24389, True),
    (-24389, True),
    (27000, True),
    (-27000, True),
    (29791, True),
    (-29791, True),
    (32768, True),
    (-32768, True),
    (35937, True),
    (-35937, True),
    (39304, True),
    (-39304, True),
    (42875, True),
    (-42875, True),
    (46656, True),
    (-46656, True),
    (50653, True),
    (-50653, True),
    (54872, True),
    (-54872, True),
    (59319, True),
    (-59319, True),
    (64000, True),
    (-64000, True),
    (68921, True),
    (-68921, True),
    (74088, True),
    (-74088, True),
    (79507, True),
    (-79507, True),
    (85184, True),
    (-85184, True),
    (91125, True),
    (-91125, True),
    (97336, True),
    (-97336, True),
    (103823, True),
    (-103823, True),
    (110592, True),
    (-110592, True),
    (117649, True),
    (-117649, True),
    (125000, True),
    (-125000, True),
    (3, False),
    (4, False),
    (5, False),
    (6, False),
    (7, False),
    (9, False),
    (10, False),
    (15, False),
    (16, False),
    (25, False),
    (26, False),
    (28, False),
    (63, False),
    (65, False),
    (100, False),
    (124, False),
    (126, False),
    (179, False),
    (181, False),
    (215, False),
    (217, False),
    (342, False),
    (344, False),
    (511, False),
    (513, False),
    (728, False),
    (730, False),
    (999, False),
    (1001, False),
    (-3, False),
    (-4, False),
    (-5, False),
    (-6, False),
    (-7, False),
    (-9, False),
    (-10, False),
    (-15, False),
    (-16, False),
    (-25, False),
    (-26, False),
    (-28, False),
    (-63, False),
    (-65, False),
    (-100, False),
    (-124, False),
    (-126, False),
    (-179, False),
    (-181, False),
    (-215, False),
    (-217, False),
    (-342, False),
    (-344, False),
    (-511, False),
    (-513, False),
    (-728, False),
    (-730, False),
    (-999, False),
    (-1001, False)
])
def test_iscube_parametrized(input_val, expected):
    assert iscube(input_val) == expected

def test_iscube_zero():
    assert iscube(0) == True

def test_iscube_one():
    assert iscube(1) == True

def test_iscube_negative_one():
    assert iscube(-1) == True

def test_iscube_small_perfect_cubes():
    perfect_cubes = [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
    for cube in perfect_cubes:
        assert iscube(cube) == True
        assert iscube(-cube) == True

def test_iscube_non_cubes():
    non_cubes = [2, 3, 4, 5, 6, 7, 9, 10, 15, 16, 25, 26, 28, 63, 65]
    for non_cube in non_cubes:
        assert iscube(non_cube) == False
        assert iscube(-non_cube) == False

def test_iscube_large_numbers():
    assert iscube(1000000) == True
    assert iscube(-1000000) == True
    assert iscube(999999) == False
    assert iscube(-999999) == False
