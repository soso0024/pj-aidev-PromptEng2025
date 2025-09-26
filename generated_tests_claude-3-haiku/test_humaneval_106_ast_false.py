# Test cases for HumanEval/106
# Generated using Claude API


def f(n):
    """ Implement the function f that takes n as a parameter,
    and returns a list of size n, such that the value of the element at index i is the factorial of i if i is even
    or the sum of numbers from 1 to i otherwise.
    i starts from 1.
    the factorial of i is the multiplication of the numbers from 1 to i (1 * 2 * ... * i).
    Example:
    f(5) == [1, 2, 6, 24, 15]
    """

    ret = []
    for i in range(1,n+1):
        if i%2 == 0:
            x = 1
            for j in range(1,i+1): x *= j
            ret += [x]
        else:
            x = 0
            for j in range(1,i+1): x += j
            ret += [x]
    return ret


# Generated test cases:
import pytest

def test_f_normal_cases():
    assert f(5) == [1, 2, 6, 24, 15]
    assert f(10) == [1, 2, 6, 24, 120, 0, 28, 36, 45, 165]

def test_f_edge_cases():
    assert f(0) == []
    assert f(1) == [0]
    assert f(2) == [1, 3]

def test_f_negative_input():
    with pytest.raises(ValueError):
        f(-1)