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

@pytest.mark.parametrize("N,expected", [
    (1000, "1"),
    (150, "110"),
    (147, "1100"),
    (0, "0"),
    (1, "1"),
    (9999, "100100"),
    (123, "110"),
    (555, "1111"),
    (100, "1"),
    (999, "11011")
])
def test_solve_valid_inputs(N, expected):
    assert solve(N) == expected

def test_solve_zero():
    assert solve(0) == "0"

def test_solve_single_digit():
    assert solve(5) == "101"

@pytest.mark.parametrize("N", [-1, -100])
def test_solve_invalid_inputs(N):
    with pytest.raises(ValueError):
        solve(N)

@pytest.mark.parametrize("N", [1.5, None, True])
def test_solve_invalid_types(N):
    with pytest.raises((TypeError, ValueError)):
        solve(N)

def test_solve_max_valid_input():
    assert solve(10000) == "1"

def test_solve_repeated_digits():
    assert solve(111) == "11"

def test_solve_all_nines():
    assert solve(9999) == "100100"

def test_solve_binary_sum_edge_cases():
    assert solve(198) == "10010"  # sum is 18
    assert solve(999) == "11011"  # sum is 27