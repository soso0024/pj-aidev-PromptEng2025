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
    ([1, 2], [2, 3], "NO"),
    ([1, 3], [2, 4], "NO"),
    ([1, 4], [2, 5], "YES"),
    ([1, 6], [2, 7], "NO"),
    ([1, 8], [2, 9], "NO"),
    ([1, 9], [2, 10], "YES"),
    ([1, 10], [2, 11], "NO"),
    ([1, 12], [2, 13], "NO"),
    ([1, 14], [2, 15], "NO"),
    ([1, 16], [2, 17], "NO"),
    ([1, 18], [2, 19], "NO"),
    ([1, 20], [2, 21], "NO"),
    ([5, 10], [8, 15], "YES"),
    ([10, 20], [15, 25], "YES"),
    ([0, 5], [3, 8], "YES"),
    ([0, 10], [5, 15], "YES"),
    ([1, 100], [50, 150], "NO"),
])
def test_intersection_normal_cases(interval1, interval2, expected):
    assert intersection(interval1, interval2) == expected

@pytest.mark.parametrize("interval1,interval2,expected", [
    ([1, 2], [3, 4], "NO"),
    ([5, 6], [1, 2], "NO"),
    ([1, 5], [6, 10], "NO"),
    ([10, 15], [1, 5], "NO"),
    ([0, 0], [1, 1], "NO"),
    ([-5, -3], [-2, 0], "NO"),
    ([-10, -5], [-8, -3], "YES"),
])
def test_intersection_no_overlap(interval1, interval2, expected):
    assert intersection(interval1, interval2) == expected

@pytest.mark.parametrize("interval1,interval2,expected", [
    ([1, 2], [2, 3], "NO"),
    ([5, 8], [8, 10], "NO"),
    ([0, 5], [5, 10], "NO"),
    ([-5, 0], [0, 5], "NO"),
])
def test_intersection_touching_endpoints(interval1, interval2, expected):
    assert intersection(interval1, interval2) == expected

@pytest.mark.parametrize("interval1,interval2,expected", [
    ([1, 3], [1, 3], "YES"),
    ([0, 5], [0, 5], "YES"),
    ([2, 4], [2, 4], "YES"),
    ([1, 2], [1, 2], "NO"),
    ([5, 6], [5, 6], "NO"),
    ([0, 1], [0, 1], "NO"),
])
def test_intersection_identical_intervals(interval1, interval2, expected):
    assert intersection(interval1, interval2) == expected

@pytest.mark.parametrize("interval1,interval2,expected", [
    ([1, 10], [3, 5], "YES"),
    ([0, 20], [5, 10], "YES"),
    ([2, 8], [3, 6], "YES"),
    ([1, 6], [2, 4], "YES"),
    ([0, 10], [1, 2], "NO"),
    ([5, 15], [8, 9], "NO"),
])
def test_intersection_one_contains_other(interval1, interval2, expected):
    assert intersection(interval1, interval2) == expected

@pytest.mark.parametrize("interval1,interval2,expected", [
    ([-10, -5], [-8, -3], "YES"),
    ([-5, 0], [-3, 2], "YES"),
    ([-10, 5], [-5, 10], "NO"),
    ([-1, 1], [0, 2], "NO"),
    ([-3, 3], [-1, 1], "YES"),
])
def test_intersection_negative_numbers(interval1, interval2, expected):
    assert intersection(interval1, interval2) == expected

@pytest.mark.parametrize("interval1,interval2,expected", [
    ([0, 2], [1, 3], "NO"),
    ([0, 3], [1, 4], "YES"),
    ([0, 1], [0, 2], "NO"),
    ([0, 5], [2, 7], "YES"),
])
def test_intersection_with_zero(interval1, interval2, expected):
    assert intersection(interval1, interval2) == expected

@pytest.mark.parametrize("interval1,interval2,expected", [
    ([1, 1000], [500, 1500], "NO"),
    ([1, 100], [50, 150], "NO"),
    ([1, 1000], [1, 1000], "NO"),
    ([1, 998], [1, 998], "YES"),
])
def test_intersection_large_numbers(interval1, interval2, expected):
    assert intersection(interval1, interval2) == expected

def test_intersection_prime_lengths():
    assert intersection([1, 3], [2, 4]) == "NO"
    assert intersection([1, 4], [2, 5]) == "YES"
    assert intersection([1, 6], [2, 7]) == "NO"
    assert intersection([1, 8], [2, 9]) == "NO"
    assert intersection([1, 12], [2, 13]) == "NO"
    assert intersection([1, 14], [2, 15]) == "NO"
    assert intersection([1, 18], [2, 19]) == "NO"

def test_intersection_non_prime_lengths():
    assert intersection([1, 2], [2, 3]) == "NO"
    assert intersection([1, 10], [2, 11]) == "NO"
    assert intersection([1, 16], [2, 17]) == "NO"
    assert intersection([0, 10], [1, 2]) == "NO"
    assert intersection([5, 15], [8, 9]) == "NO"