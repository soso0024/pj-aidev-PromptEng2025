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

def is_prime(num):
    if num == 1 or num == 0:
        return False
    if num == 2:
        return True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def intersection(interval1, interval2):
    l = max(interval1[0], interval2[0])
    r = min(interval1[1], interval2[1])
    length = r - l
    if length > 0 and is_prime(length):
        return "YES"
    return "NO"

@pytest.mark.parametrize("interval1, interval2, expected", [
    ((1, 5), (3, 7), "YES"),
    ((2, 6), (4, 8), "YES"),
    ((1, 4), (5, 9), "NO"),
    ((1, 3), (3, 5), "YES"),
    ((1, 2), (2, 3), "NO"),
    ((1, 1), (1, 1), "YES"),
    ((0, 0), (0, 0), "YES"),
    ((1, 2), (3, 4), "NO"),
    ((1, 10), (2, 9), "YES"),
    ((1, 100), (50, 150), "YES"),
])
def test_intersection(interval1, interval2, expected):
    assert intersection(interval1, interval2) == expected

@pytest.mark.parametrize("interval1, interval2", [
    ((1, 0), (3, 7)),
    ((2, -1), (4, 8)),
    ((1, 4), (5, 3)),
    ((1, 3), (5, 3)),
    ((1, 2), (0, 3)),
    ((1, 1), (1, 1, 1)),
    ((0, 0, 0), (0, 0)),
    ((1, 2, 3), (3, 4)),
    ((1, 10), (2,)),
    ((1, 100), (50, 150, 200)),
])
def test_intersection_invalid_input(interval1, interval2):
    with pytest.raises(TypeError):
        intersection(interval1, interval2)