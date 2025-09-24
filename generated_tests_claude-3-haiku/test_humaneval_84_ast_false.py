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

def test_solve_positive_integer():
    assert solve(123) == '6'
    assert solve(456) == '15'
    assert solve(789) == '24'

def test_solve_zero():
    assert solve(0) == '0'

def test_solve_negative_integer():
    with pytest.raises(TypeError):
        solve(-123)

def test_solve_float():
    with pytest.raises(TypeError):
        solve(3.14)

@pytest.mark.parametrize("input,expected", [
    ('123', '6'),
    ('456', '15'),
    ('789', '24'),
    ('0', '0'),
    ('-123', TypeError),
    ('3.14', TypeError)
])
def test_solve_parametrize(input, expected):
    if expected is TypeError:
        with pytest.raises(TypeError):
            solve(int(input))
    else:
        assert solve(int(input)) == expected