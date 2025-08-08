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
    (10000, "1"),
    (-1, ValueError),
    (10001, ValueError)
])
def test_solve(N, expected):
    from solve import solve
    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            assert solve(N) == str(expected)
    else:
        assert solve(N) == expected