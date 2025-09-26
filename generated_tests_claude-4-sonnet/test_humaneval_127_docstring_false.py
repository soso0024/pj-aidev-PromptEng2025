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

def intersection(interval1, interval2):
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

@pytest.mark.parametrize("interval1,interval2,expected", [
    ((1, 2), (2, 3), "NO"),
    ((-1, 1), (0, 4), "NO"),
    ((-3, -1), (-5, 5), "YES"),
    ((1, 3), (2, 4), "NO"),
    ((0, 5), (2, 7), "YES"),
    ((1, 10), (5, 8), "YES"),
    ((0, 2), (1, 4), "NO"),
    ((1, 1), (1, 1), "NO"),
    ((0, 0), (0, 0), "NO"),
    ((1, 5), (6, 10), "NO"),
    ((1, 5), (5, 10), "NO"),
    ((1, 6), (5, 10), "NO"),
    ((-10, -5), (-8, -3), "YES"),
    ((-10, 10), (-5, 5), "NO"),
    ((0, 7), (2, 9), "YES"),
    ((1, 8), (3, 10), "YES"),
    ((0, 11), (4, 15), "YES"),
    ((1, 13), (6, 18), "YES"),
    ((0, 17), (5, 22), "NO"),
    ((1, 19), (8, 27), "YES"),
    ((-100, 100), (-50, 50), "NO"),
    ((10, 20), (15, 25), "YES"),
    ((100, 200), (150, 250), "NO"),
    ((0, 1000), (500, 1500), "NO"),
    ((1, 4), (2, 5), "YES"),
    ((5, 10), (8, 15), "YES"),
    ((10, 20), (12, 25), "NO"),
    ((0, 3), (1, 6), "YES"),
    ((2, 9), (4, 11), "YES"),
    ((3, 14), (6, 17), "NO"),
    ((-20, -10), (-15, -5), "YES"),
    ((-30, -20), (-25, -15), "YES"),
    ((-40, -30), (-35, -25), "YES"),
    ((1, 2), (3, 4), "NO"),
    ((5, 6), (7, 8), "NO"),
    ((-5, -4), (-3, -2), "NO"),
    ((0, 1), (1, 2), "NO"),
    ((2, 3), (3, 4), "NO"),
    ((-2, -1), (-1, 0), "NO")
])
def test_intersection_parametrized(interval1, interval2, expected):
    assert intersection(interval1, interval2) == expected

def test_no_intersection_separate_intervals():
    assert intersection((1, 3), (5, 7)) == "NO"
    assert intersection((10, 15), (20, 25)) == "NO"
    assert intersection((-10, -5), (5, 10)) == "NO"

def test_touching_intervals():
    assert intersection((1, 5), (5, 10)) == "NO"
    assert intersection((0, 3), (3, 6)) == "NO"
    assert intersection((-5, 0), (0, 5)) == "NO"

def test_identical_intervals():
    assert intersection((1, 3), (1, 3)) == "YES"
    assert intersection((0, 2), (0, 2)) == "YES"
    assert intersection((-2, 0), (-2, 0)) == "YES"
    assert intersection((5, 6), (5, 6)) == "NO"

def test_one_interval_inside_another():
    assert intersection((1, 10), (3, 7)) == "NO"
    assert intersection((0, 20), (5, 10)) == "YES"
    assert intersection((-10, 10), (-3, 3)) == "NO"

def test_partial_overlap():
    assert intersection((1, 5), (3, 8)) == "YES"
    assert intersection((2, 6), (4, 9)) == "YES"
    assert intersection((0, 4), (2, 7)) == "YES"

def test_single_point_intervals():
    assert intersection((5, 5), (5, 5)) == "NO"
    assert intersection((0, 0), (0, 0)) == "NO"
    assert intersection((-1, -1), (-1, -1)) == "NO"

def test_negative_intervals():
    assert intersection((-10, -5), (-8, -3)) == "YES"
    assert intersection((-20, -15), (-18, -10)) == "YES"
    assert intersection((-5, -1), (-3, 2)) == "YES"

def test_large_intervals():
    assert intersection((0, 1000), (500, 1500)) == "NO"
    assert intersection((100, 200), (150, 250)) == "NO"
    assert intersection((1000, 2000), (1500, 2500)) == "NO"

def test_prime_length_intersections():
    assert intersection((0, 5), (2, 7)) == "YES"
    assert intersection((1, 6), (3, 8)) == "YES"
    assert intersection((0, 8), (3, 10)) == "YES"
    assert intersection((1, 12), (4, 15)) == "NO"

def test_non_prime_length_intersections():
    assert intersection((1, 5), (2, 6)) == "NO"
    assert intersection((0, 7), (1, 8)) == "NO"
    assert intersection((2, 8), (3, 9)) == "YES"
    assert intersection((1, 9), (2, 10)) == "NO"