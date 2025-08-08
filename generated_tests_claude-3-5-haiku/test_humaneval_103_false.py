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

def test_rounded_avg_normal_case():
    assert rounded_avg(1, 3) == '0b10'
    assert rounded_avg(3, 5) == '0b11'

def test_rounded_avg_single_number():
    assert rounded_avg(4, 4) == '0b100'

def test_rounded_avg_invalid_range():
    assert rounded_avg(5, 3) == -1

def test_rounded_avg_zero_range():
    assert rounded_avg(0, 0) == '0b0'

def test_rounded_avg_large_range():
    assert rounded_avg(1, 10) == '0b101'

@pytest.mark.parametrize("n,m,expected", [
    (1, 3, '0b10'),
    (3, 5, '0b11'),
    (4, 4, '0b100'),
    (5, 3, -1),
    (0, 0, '0b0'),
    (1, 10, '0b101')
])
def test_rounded_avg_parametrized(n, m, expected):
    assert rounded_avg(n, m) == expected