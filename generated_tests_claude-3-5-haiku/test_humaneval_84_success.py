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
    if not isinstance(N, int):
        raise TypeError("Input must be an integer")
    if N < 0:
        raise ValueError("Input must be a non-negative integer")
    return str(sum(int(i) for i in str(N)))

def test_solve_single_digit():
    assert solve(5) == '5'

def test_solve_multiple_digits():
    assert solve(123) == '6'

def test_solve_zero():
    assert solve(0) == '0'

def test_solve_large_number():
    assert solve(9999) == '36'

@pytest.mark.parametrize("input_num,expected", [
    (5, '5'),
    (10, '1'),
    (123, '6'),
    (9999, '36'),
    (0, '0'),
    (1000000, '1'),
])
def test_solve_parametrized(input_num, expected):
    assert solve(input_num) == expected

def test_solve_negative_number():
    with pytest.raises(ValueError):
        solve(-5)

def test_solve_non_integer():
    with pytest.raises(TypeError):
        solve('abc')