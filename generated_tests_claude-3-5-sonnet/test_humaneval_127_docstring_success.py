# Test cases for HumanEval/127
# Generated using Claude API


def intersection(interval1, interval2):
    """You are given two intervals,
    where each interval is a pair of integers. For example, interval = (start, end) = (1, 2).
    The given intervals are closed which means that the interval (start, end)
    includes both start and end.
    For each given interval, it is assumed that its start is less or equal its end.
    Your task is to determine whether the length of intersection of these two 
    intervals is a prime number.
    Example, the intersection of the intervals (1, 3), (2, 4) is (2, 3)
    which its length is 1, which not a prime number.
    If the length of the intersection is a prime number, return "YES",
    otherwise, return "NO".
    If the two intervals don't intersect, return "NO".


    [input/output] samples:
    intersection((1, 2), (2, 3)) ==> "NO"
    intersection((-1, 1), (0, 4)) ==> "NO"
    intersection((-3, -1), (-5, 5)) ==> "YES"
    """

    def is_prime(num):
        if num == 1 or num == 0:
            return False
        if num == 2:
            return True
        for i in range(2, num):
            if num%i == 0:
                return False
        return True

    l = max(interval1[0], interval2[0])
    r = min(interval1[1], interval2[1])
    length = r - l
    if length > 0 and is_prime(length):
        return "YES"
    return "NO"


# Generated test cases:
import pytest

@pytest.mark.parametrize("interval1,interval2,expected", [
    ((1, 2), (2, 3), "NO"),
    ((-1, 1), (0, 4), "NO"),
    ((-3, -1), (-5, 5), "YES"),
    ((0, 5), (2, 3), "NO"),
    ((1, 5), (2, 4), "YES"),
    ((1, 10), (3, 6), "YES"),
    ((0, 0), (0, 1), "NO"),
    ((-2, 2), (-1, 3), "YES"),
    ((1, 1), (1, 1), "NO"),
    ((5, 10), (1, 4), "NO"),
    ((2, 7), (7, 10), "NO"),
    ((1, 5), (6, 10), "NO"),
    ((0, 10), (3, 6), "YES"),
    ((-10, -5), (-8, -6), "YES"),
    ((1, 100), (98, 99), "NO")
])
def test_intersection(interval1, interval2, expected):
    assert intersection(interval1, interval2) == expected

def test_identical_intervals():
    assert intersection((2, 5), (2, 5)) == "YES"

def test_single_point_intersection():
    assert intersection((1, 2), (2, 3)) == "NO"

def test_negative_intervals():
    assert intersection((-5, -2), (-4, -1)) == "YES"

def test_zero_crossing_intervals():
    assert intersection((-2, 2), (-1, 1)) == "YES"

def test_large_intervals():
    assert intersection((0, 1000), (998, 999)) == "NO"

def test_minimal_intersection():
    assert intersection((1, 3), (2, 4)) == "NO"

def test_contained_interval():
    assert intersection((0, 10), (4, 6)) == "YES"

def test_touching_intervals():
    assert intersection((1, 5), (5, 10)) == "NO"

def test_disjoint_intervals():
    assert intersection((1, 3), (4, 6)) == "NO"
