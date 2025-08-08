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

@pytest.mark.parametrize("n, m, expected", [
    (1, 5, "0b11"),
    (7, 5, -1),
    (10, 20, "0b1111"),
    (20, 33, "0b11010"),
    (1, 1, "0b1"),
    (100, 100, "0b1100100"),
    (5, 10, "0b1000"),
    (1, 3, "0b10"),
    (50, 55, "0b110100"),
    (999, 1000, "0b1111101000"),
])
def test_rounded_avg_various_inputs(n, m, expected):
    assert rounded_avg(n, m) == expected

def test_rounded_avg_equal_numbers():
    assert rounded_avg(5, 5) == "0b101"

def test_rounded_avg_consecutive_numbers():
    assert rounded_avg(4, 5) == "0b100"

def test_rounded_avg_large_range():
    assert rounded_avg(1, 1000) == "0b111110100"

def test_rounded_avg_negative_range():
    assert rounded_avg(10, 5) == -1

def test_rounded_avg_large_numbers():
    assert rounded_avg(9998, 10000) == "0b10011100001111"

def test_rounded_avg_minimal_difference():
    assert rounded_avg(999, 1000) == "0b1111101000"

def test_rounded_avg_single_digit():
    assert rounded_avg(1, 2) == "0b10"

def test_rounded_avg_boundary_case():
    assert rounded_avg(999999, 1000000) == "0b11110100001001000000"