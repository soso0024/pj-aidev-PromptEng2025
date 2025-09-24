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
    (0, True),
    (1, True),
    (-1, True),
    (8, True),
    (-8, True),
    (27, True),
    (-27, True),
    (64, True),
    (-64, True),
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
])
def test_perfect_cubes(input_val, expected):
    assert iscube(input_val) == expected

@pytest.mark.parametrize("input_val,expected", [
    (2, False),
    (-2, False),
    (3, False),
    (-3, False),
    (4, False),
    (-4, False),
    (5, False),
    (-5, False),
    (6, False),
    (-6, False),
    (7, False),
    (-7, False),
    (9, False),
    (-9, False),
    (10, False),
    (-10, False),
    (15, False),
    (-15, False),
    (16, False),
    (-16, False),
    (25, False),
    (-25, False),
    (26, False),
    (-26, False),
    (28, False),
    (-28, False),
    (50, False),
    (-50, False),
    (63, False),
    (-63, False),
    (65, False),
    (-65, False),
    (100, False),
    (-100, False),
    (124, False),
    (-124, False),
    (126, False),
    (-126, False),
    (200, False),
    (-200, False),
    (215, False),
    (-215, False),
    (217, False),
    (-217, False),
    (500, False),
    (-500, False),
    (999, False),
    (-999, False),
    (1001, False),
    (-1001, False),
    (1330, False),
    (-1330, False),
    (1332, False),
    (-1332, False),
    (1727, False),
    (-1727, False),
    (1729, False),
    (-1729, False),
    (2000, False),
    (-2000, False),
    (2196, False),
    (-2196, False),
    (2198, False),
    (-2198, False),
    (5000, False),
    (-5000, False),
    (10000, False),
    (-10000, False),
    (50000, False),
    (-50000, False),
    (100000, False),
    (-100000, False),
])
def test_non_perfect_cubes(input_val, expected):
    assert iscube(input_val) == expected

def test_zero():
    assert iscube(0) == True

def test_one():
    assert iscube(1) == True
    assert iscube(-1) == True

def test_small_perfect_cubes():
    assert iscube(8) == True
    assert iscube(-8) == True
    assert iscube(27) == True
    assert iscube(-27) == True

def test_large_perfect_cubes():
    assert iscube(1000000) == True
    assert iscube(-1000000) == True
    assert iscube(1331000) == True
    assert iscube(-1331000) == True

def test_floating_point_precision_edge_cases():
    assert iscube(999999999999999999) == False
    assert iscube(-999999999999999999) == False

def test_type_handling():
    assert iscube(8.0) == True
    assert iscube(-8.0) == True
    assert iscube(8.1) == False
    assert iscube(-8.1) == False
