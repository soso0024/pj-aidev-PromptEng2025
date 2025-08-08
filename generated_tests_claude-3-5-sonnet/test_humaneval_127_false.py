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
    ((1, 4), (2, 6), "YES"),  # length 2 (prime)
    ((1, 5), (3, 8), "YES"),  # length 2 (prime)
    ((2, 10), (1, 5), "YES"), # length 3 (prime)
    ((1, 10), (4, 6), "YES"),  # length 2 (prime)
    ((5, 10), (1, 4), "NO"),  # no intersection
    ((1, 3), (4, 6), "NO"),   # no intersection
    ((1, 5), (1, 5), "NO"),   # length 4 (not prime)
    ((2, 8), (4, 6), "YES"),   # length 2 (prime)
    ((0, 2), (1, 3), "NO"),   # length 1 (not prime)
    ((5, 5), (5, 5), "NO"),   # zero length
    ((10, 20), (15, 16), "NO"), # length 1 (not prime)
    ((1, 100), (98, 99), "NO"), # length 1 (not prime)
    ((0, 10), (0, 5), "NO"),    # length 5 (not prime)
    ((2, 7), (4, 9), "YES"),    # length 3 (prime)
    ((1, 10), (3, 8), "NO"),    # length 5 (not prime)
])
def test_intersection(interval1, interval2, expected):
    assert intersection(interval1, interval2) == expected

def test_intersection_same_intervals():
    assert intersection((1, 4), (1, 4)) == "NO"  # length 3 (not prime)

def test_intersection_touching_intervals():
    assert intersection((1, 3), (3, 5)) == "NO"  # length 0 (not prime)

def test_intersection_contained_interval():
    assert intersection((1, 10), (3, 5)) == "YES"  # length 2 (prime)

def test_intersection_large_numbers():
    assert intersection((1000, 1005), (1002, 1007)) == "YES"  # length 3 (prime)

def test_intersection_zero_length():
    assert intersection((5, 5), (4, 6)) == "NO"  # length 0 (not prime)