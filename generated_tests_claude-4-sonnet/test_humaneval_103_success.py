# Test cases for HumanEval/103
# Generated using Claude API


def rounded_avg(n, m):
    """You are given two positive integers n and m, and your task is to compute the
    average of the integers from n through m (including n and m). 
    Round the answer to the nearest integer and convert that to binary.
    If n is greater than m, return -1.
    Example:
    rounded_avg(1, 5) => "0b11"
    rounded_avg(7, 5) => -1
    rounded_avg(10, 20) => "0b1111"
    rounded_avg(20, 33) => "0b11010"
    """

    if m < n:
        return -1
    summation = 0
    for i in range(n, m+1):
        summation += i
    return bin(round(summation/(m - n + 1)))


# Generated test cases:
import pytest

def rounded_avg(n, m):
    if m < n:
        return -1
    summation = 0
    for i in range(n, m+1):
        summation += i
    return bin(round(summation/(m - n + 1)))

def test_rounded_avg_invalid_range():
    assert rounded_avg(5, 3) == -1
    assert rounded_avg(10, 5) == -1
    assert rounded_avg(1, 0) == -1
    assert rounded_avg(-5, -10) == -1

def test_rounded_avg_single_number():
    assert rounded_avg(5, 5) == bin(5)
    assert rounded_avg(0, 0) == bin(0)
    assert rounded_avg(-3, -3) == bin(-3)
    assert rounded_avg(10, 10) == bin(10)

def test_rounded_avg_small_ranges():
    assert rounded_avg(1, 2) == bin(round((1+2)/2))
    assert rounded_avg(3, 4) == bin(round((3+4)/2))
    assert rounded_avg(-2, -1) == bin(round((-2+-1)/2))
    assert rounded_avg(0, 1) == bin(round((0+1)/2))

def test_rounded_avg_larger_ranges():
    assert rounded_avg(1, 5) == bin(round((1+2+3+4+5)/5))
    assert rounded_avg(7, 13) == bin(round((7+8+9+10+11+12+13)/7))
    assert rounded_avg(2, 6) == bin(round((2+3+4+5+6)/5))

def test_rounded_avg_negative_ranges():
    assert rounded_avg(-5, -1) == bin(round((-5+-4+-3+-2+-1)/5))
    assert rounded_avg(-10, -8) == bin(round((-10+-9+-8)/3))
    assert rounded_avg(-3, 0) == bin(round((-3+-2+-1+0)/4))

def test_rounded_avg_zero_included():
    assert rounded_avg(-1, 1) == bin(round((-1+0+1)/3))
    assert rounded_avg(-2, 2) == bin(round((-2+-1+0+1+2)/5))
    assert rounded_avg(0, 3) == bin(round((0+1+2+3)/4))

@pytest.mark.parametrize("n,m,expected", [
    (1, 3, bin(2)),
    (2, 4, bin(3)),
    (5, 7, bin(6)),
    (10, 12, bin(11)),
    (-4, -2, bin(-3)),
    (0, 2, bin(1))
])
def test_rounded_avg_parametrized(n, m, expected):
    assert rounded_avg(n, m) == expected

def test_rounded_avg_large_numbers():
    assert rounded_avg(100, 102) == bin(round((100+101+102)/3))
    assert rounded_avg(1000, 1000) == bin(1000)
    assert rounded_avg(50, 60) == bin(round(sum(range(50, 61))/11))
