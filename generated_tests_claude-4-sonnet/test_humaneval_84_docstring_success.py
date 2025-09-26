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

def solve(N):
    return bin(sum(int(i) for i in str(N)))[2:]

def test_solve_example_cases():
    assert solve(1000) == "1"
    assert solve(150) == "110"
    assert solve(147) == "1100"

def test_solve_edge_cases():
    assert solve(0) == "0"
    assert solve(1) == "1"
    assert solve(9) == "1001"
    assert solve(10000) == "1"

def test_solve_single_digits():
    assert solve(2) == "10"
    assert solve(3) == "11"
    assert solve(4) == "100"
    assert solve(5) == "101"
    assert solve(6) == "110"
    assert solve(7) == "111"
    assert solve(8) == "1000"

def test_solve_two_digit_numbers():
    assert solve(11) == "10"
    assert solve(19) == "1010"
    assert solve(99) == "10010"
    assert solve(12) == "11"
    assert solve(23) == "101"

def test_solve_three_digit_numbers():
    assert solve(100) == "1"
    assert solve(111) == "11"
    assert solve(123) == "110"
    assert solve(456) == "1111"
    assert solve(789) == "11000"
    assert solve(999) == "11011"

def test_solve_four_digit_numbers():
    assert solve(1111) == "100"
    assert solve(1234) == "1010"
    assert solve(5678) == "11010"
    assert solve(9999) == "100100"

@pytest.mark.parametrize("n,expected", [
    (0, "0"),
    (1, "1"),
    (10, "1"),
    (20, "10"),
    (30, "11"),
    (40, "100"),
    (50, "101"),
    (60, "110"),
    (70, "111"),
    (80, "1000"),
    (90, "1001"),
    (101, "10"),
    (202, "100"),
    (303, "110"),
    (404, "1000"),
    (505, "1010"),
    (606, "1100"),
    (707, "1110"),
    (808, "10000"),
    (909, "10010")
])
def test_solve_parametrized(n, expected):
    assert solve(n) == expected
