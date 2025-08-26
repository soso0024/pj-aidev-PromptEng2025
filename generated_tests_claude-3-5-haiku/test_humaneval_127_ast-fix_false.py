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
from typing import Tuple

def intersection(interval1: Tuple[int, int], interval2: Tuple[int, int]) -> str:
    def is_prime(num):
        if num <= 1:
            return False
        if num == 2:
            return True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    interval1 = sorted(interval1)
    interval2 = sorted(interval2)

    l = max(interval1[0], interval2[0])
    r = min(interval1[1], interval2[1])
    length = r - l + 1
    if length > 0 and is_prime(length - 1):
        return "YES"
    return "NO"

def test_intersection():
    assert intersection((1, 2), (2, 3)) == "NO"
    assert intersection((-1, 1), (0, 4)) == "NO"
    assert intersection((-3, -1), (-5, 5)) == "YES"
    assert intersection((1, 3), (2, 4)) == "NO"
    assert intersection((1, 5), (3, 7)) == "YES"

def test_edge_cases():
    assert intersection((0, 0), (0, 0)) == "NO"
    assert intersection((-10, -5), (-8, -3)) == "YES"
    assert intersection((10, 20), (15, 25)) == "NO"

def test_no_intersection():
    assert intersection((1, 2), (3, 4)) == "NO"
    assert intersection((-5, -3), (0, 2)) == "NO"

def test_single_point_intersection():
    assert intersection((1, 2), (2, 3)) == "NO"
    assert intersection((0, 1), (1, 2)) == "NO"