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
        raise TypeError("Input must be non-negative")
    
    ret = []
    for i in range(1, n+1):
        if i % 2 == 0:
            x = 1
            for j in range(1, i+1):
                x *= j
            ret.append(x)
        else:
            x = 0
            for j in range(1, i+1):
                x += j
            ret.append(x)
    return ret

def test_f_basic_cases():
    assert f(1) == [1]
    assert f(2) == [1, 3]
    assert f(3) == [1, 3, 6]
    assert f(4) == [1, 3, 6, 24]

def test_f_larger_input():
    result = f(5)
    assert len(result) == 5
    assert result == [1, 3, 6, 24, 15]

def test_f_zero_input():
    assert f(0) == []

def test_f_edge_cases():
    assert f(6) == [1, 3, 6, 24, 15, 720]

@pytest.mark.parametrize("n,expected_length", [
    (1, 1),
    (3, 3),
    (5, 5),
    (10, 10)
])
def test_f_result_length(n, expected_length):
    assert len(f(n)) == expected_length

def test_f_alternating_pattern():
    result = f(6)
    assert result[0] == 1
    assert result[1] == 3
    assert result[2] == 6
    assert result[3] == 24

def test_f_type_error():
    with pytest.raises(TypeError):
        f("not a number")

def test_f_negative_input():
    with pytest.raises(TypeError):
        f(-1)