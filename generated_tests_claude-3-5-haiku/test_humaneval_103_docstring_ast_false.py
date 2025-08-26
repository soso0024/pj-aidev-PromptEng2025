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

def test_rounded_avg_normal_cases():
    assert rounded_avg(1, 5) == "0b11"
    assert rounded_avg(10, 20) == "0b1111"
    assert rounded_avg(20, 33) == "0b11010"

def test_rounded_avg_edge_cases():
    assert rounded_avg(7, 5) == -1
    assert rounded_avg(5, 5) == "0b101"

@pytest.mark.parametrize("n,m,expected", [
    (1, 5, "0b11"),
    (10, 20, "0b1111"),
    (20, 33, "0b11010"),
    (7, 5, -1),
    (5, 5, "0b101"),
    (100, 200, "0b11001010")
])
def test_rounded_avg_parametrized(n, m, expected):
    assert rounded_avg(n, m) == expected

def test_rounded_avg_large_range():
    assert rounded_avg(1, 1000) is not None

def test_rounded_avg_zero_range():
    assert rounded_avg(0, 0) == "0b0"

def test_rounded_avg_negative_input():
    with pytest.raises(ValueError):
        rounded_avg(-1, 5)
    with pytest.raises(ValueError):
        rounded_avg(1, -5)