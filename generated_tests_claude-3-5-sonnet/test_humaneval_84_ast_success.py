# Test cases for HumanEval/84
# Generated using Claude API


def solve(N):
    """Given a positive integer N, return the total sum of its digits in binary.
    
    Example
        For N = 1000, the sum of digits will be 1 the output should be "1".
        For N = 150, the sum of digits will be 6 the output should be "110".
        For N = 147, the sum of digits will be 12 the output should be "1100".
    
    Variables:
        @N integer
             Constraints: 0 ≤ N ≤ 10000.
    Output:
         a string of binary number
    """

    return bin(sum(int(i) for i in str(N)))[2:]


# Generated test cases:
import pytest

def test_solve_single_digit():
    assert solve(5) == "101"
    assert solve(9) == "1001"
    assert solve(0) == "0"

def test_solve_multiple_digits():
    assert solve(123) == "110"  # 1+2+3=6 -> 110
    assert solve(999) == "11011"  # 9+9+9=27 -> 11011
    assert solve(100) == "1"  # 1+0+0=1 -> 1

@pytest.mark.parametrize("input_n,expected", [
    (123456789, "101101"),  # sum=45 -> 101101
    (1000000, "1"),  # sum=1 -> 1
    (888888, "110000"),  # sum=48 -> 110000
    (101010, "11"),  # sum=3 -> 11
])
def test_solve_large_numbers(input_n, expected):
    assert solve(input_n) == expected

@pytest.mark.parametrize("input_n,expected", [
    (1, "1"),
    (10, "1"),
    (11, "10"),
    (99, "10010"),
])
def test_solve_edge_cases(input_n, expected):
    assert solve(input_n) == expected

def test_solve_zero():
    assert solve(0) == "0"

@pytest.mark.parametrize("input_n", [
    0,
    1,
    10000
])
def test_solve_valid_range(input_n):
    result = solve(input_n)
    assert all(c in '01' for c in result)
    assert isinstance(result, str)