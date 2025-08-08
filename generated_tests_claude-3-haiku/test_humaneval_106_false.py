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
    ret = []
    for i in range(1,n+1):
        if i%2 == 0:
            x = 1
            for j in range(1,i+1): x *= j
            ret.append(x)
        else:
            x = 0
            for j in range(1,i+1): x += j
            ret.append(x)
    return ret

def test_f_empty_input():
    assert f(0) == []

@pytest.mark.parametrize("n,expected", [
    (1, [1]),
    (2, [1, 2]),
    (3, [0, 2, 6]),
    (4, [1, 2, 6, 24]),
    (5, [0, 2, 6, 24, 15]),
])
def test_f_normal_cases(n, expected):
    assert f(n) == expected

def test_f_negative_input():
    with pytest.raises(ValueError):
        f(-1)

def test_f_float_input():
    with pytest.raises(TypeError):
        f(2.5)

def test_f_string_input():
    with pytest.raises(TypeError):
        f("3")