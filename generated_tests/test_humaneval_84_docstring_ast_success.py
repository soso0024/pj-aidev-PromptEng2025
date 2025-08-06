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

@pytest.mark.parametrize("input_n,expected", [
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
def test_solve_valid_inputs(input_n, expected):
    assert solve(input_n) == expected

@pytest.mark.parametrize("input_n", [
    -1,
    -1000
])
def test_solve_invalid_inputs(input_n):
    with pytest.raises(ValueError):
        solve(input_n)

def test_solve_type_error():
    with pytest.raises((ValueError, TypeError)):
        solve("not a number")
    with pytest.raises((ValueError, TypeError)):
        solve([1, 2, 3])
    with pytest.raises((ValueError, TypeError)):
        solve(None)
    with pytest.raises((ValueError, TypeError)):
        solve(1.5)

def test_solve_edge_cases():
    assert solve(10000) == "1"
    assert solve(1) == "1"
    assert solve(0) == "0"

def test_solve_large_valid_inputs():
    assert solve(10001) == "10"