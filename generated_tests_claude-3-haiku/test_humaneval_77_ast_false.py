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
from math import pow, round

@pytest.mark.parametrize("input,expected", [
    (0, True),
    (1, True),
    (-1, True),
    (8, True),
    (27, True),
    (64, True),
    (125, True),
    (2, False),
    (3, False),
    (4, False),
    (5, False),
    (6, False),
    (7, False),
    (9, False),
    (10, False),
    (11, False),
    (12, False),
    (13, False),
    (14, False),
    (15, False),
    ("test", TypeError),
    (None, TypeError)
])
def test_iscube(input, expected):
    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            iscube(input)
    else:
        assert iscube(input) == expected