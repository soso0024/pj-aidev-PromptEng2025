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
    assert rounded_avg(1, 5) == "0b11"
    assert rounded_avg(10, 20) == "0b1111"
    assert rounded_avg(20, 33) == "0b11010"

@pytest.mark.parametrize("n,m,expected", [
    (7, 5, -1),
    (0, 0, "0b0"),
    (1, 1, "0b1"),
    (100, 100, "0b1100100"),
    (1, 100, "0b110010")
])
def test_rounded_avg_edge_cases(n, m, expected):
    assert rounded_avg(n, m) == expected

def test_rounded_avg_error_handling():
    with pytest.raises(TypeError):
        rounded_avg("a", 5)
    with pytest.raises(TypeError):
        rounded_avg(1, "b")