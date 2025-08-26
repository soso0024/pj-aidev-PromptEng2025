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

def f(n):
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n < 0:
        raise ValueError("Input must be non-negative")
    
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

def test_f_normal_cases():
    assert f(5) == [1, 2, 6, 24, 15]
    assert f(3) == [1, 2, 6]
    assert f(1) == [1]

def test_f_edge_cases():
    assert f(0) == []
    assert f(2) == [1, 2]

@pytest.mark.parametrize("n,expected", [
    (4, [1, 2, 6, 24]),
    (6, [1, 2, 6, 24, 15, 720]),
    (7, [1, 2, 6, 24, 15, 720, 28])
])
def test_f_parametrized(n, expected):
    assert f(n) == expected

def test_f_type_error():
    with pytest.raises(TypeError):
        f("not a number")
    with pytest.raises(TypeError):
        f(None)

def test_f_negative_input():
    with pytest.raises(ValueError):
        f(-1)