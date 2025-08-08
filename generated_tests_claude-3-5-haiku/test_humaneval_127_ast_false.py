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

def test_intersection_prime_length_intervals():
    assert intersection([1, 5], [3, 7]) == "YES"
    assert intersection([2, 6], [4, 8]) == "YES"

def test_intersection_non_prime_length_intervals():
    assert intersection([1, 4], [3, 6]) == "NO"
    assert intersection([2, 6], [5, 9]) == "NO"

def test_intersection_no_overlap():
    assert intersection([1, 3], [4, 6]) == "NO"
    assert intersection([7, 9], [1, 3]) == "NO"

def test_intersection_edge_cases():
    assert intersection([2, 2], [2, 2]) == "NO"
    assert intersection([0, 1], [1, 2]) == "NO"

def test_intersection_large_intervals():
    assert intersection([10, 20], [15, 25]) == "YES"
    assert intersection([100, 200], [150, 250]) == "YES"

def test_intersection_zero_length_intervals():
    assert intersection([5, 5], [5, 7]) == "NO"
    assert intersection([3, 3], [3, 3]) == "NO"

def test_intersection_negative_intervals():
    assert intersection([-5, -1], [-3, 2]) == "YES"
    assert intersection([-10, -5], [-8, -3]) == "NO"