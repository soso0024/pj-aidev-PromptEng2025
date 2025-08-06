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

def test_rounded_avg_basic():
    assert rounded_avg(1, 3) == "0b10"
    assert rounded_avg(2, 4) == "0b11"

def test_rounded_avg_same_number():
    assert rounded_avg(5, 5) == "0b101"
    assert rounded_avg(1, 1) == "0b1"

def test_rounded_avg_invalid_input():
    assert rounded_avg(5, 3) == -1
    assert rounded_avg(10, 5) == -1

def test_rounded_avg_zero():
    assert rounded_avg(0, 2) == "0b1"

@pytest.mark.parametrize("n, m, expected", [
    (1, 5, "0b11"),
    (2, 6, "0b100"),
    (0, 3, "0b10"),
    (10, 12, "0b1011"),
    (-2, 2, "0b0"),
    (5, 5, "0b101"),
    (100, 102, "0b1100101"),
])
def test_rounded_avg_parametrized(n, m, expected):
    assert rounded_avg(n, m) == expected

@pytest.mark.parametrize("n, m", [
    (5, 4),
    (10, 8),
    (100, 99),
    (1000, 999),
])
def test_rounded_avg_invalid_inputs_parametrized(n, m):
    assert rounded_avg(n, m) == -1

def test_rounded_avg_large_numbers():
    assert rounded_avg(998, 1000) == "0b1111100111"

def test_rounded_avg_negative_numbers():
    assert rounded_avg(-3, -1) == "-0b10"
    assert rounded_avg(-5, -3) == "-0b100"

def test_rounded_avg_mixed_numbers():
    assert rounded_avg(-2, 2) == "0b0"
    assert rounded_avg(-1, 1) == "0b0"