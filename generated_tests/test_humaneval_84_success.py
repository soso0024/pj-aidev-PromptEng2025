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
    assert solve(1) == "1"

def test_solve_multiple_digits():
    assert solve(123) == "110"  # 1+2+3 = 6 -> 110
    assert solve(999) == "11011"  # 9+9+9 = 27 -> 11011

def test_solve_zero():
    assert solve(0) == "0"

def test_solve_large_numbers():
    assert solve(54321) == "1111"  # 5+4+3+2+1 = 15 -> 1111
    assert solve(99999) == "101101"  # 9+9+9+9+9 = 45 -> 101101

@pytest.mark.parametrize("input_n,expected", [
    (12, "11"),
    (45, "1001"),
    (100, "1"),
    (678, "10101"),
    (1234, "1010")
])
def test_solve_parametrized(input_n, expected):
    assert solve(input_n) == expected

def test_solve_special_cases():
    assert solve(1000000) == "1"  # 1+0+0+0+0+0+0 = 1 -> 1
    assert solve(11111) == "101"  # 1+1+1+1+1 = 5 -> 101

@pytest.mark.parametrize("input_n", [-1, -100, -999])
def test_solve_negative_numbers(input_n):
    with pytest.raises(ValueError):
        solve(input_n)

def test_solve_non_integer_input():
    with pytest.raises((TypeError, ValueError)):
        solve("abc")
    with pytest.raises((TypeError, ValueError)):
        solve(12.34)
    with pytest.raises((TypeError, ValueError)):
        solve(None)