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

def test_empty_input():
    assert f(0) == []

def test_single_input():
    assert f(1) == [1]

def test_two_inputs():
    assert f(2) == [1, 2]

def test_larger_sequence():
    assert f(5) == [1, 2, 6, 24, 15]

@pytest.mark.parametrize("input_n, expected", [
    (3, [1, 2, 6]),
    (4, [1, 2, 6, 24]),
    (6, [1, 2, 6, 24, 15, 720])
])
def test_various_inputs(input_n, expected):
    assert f(input_n) == expected

@pytest.mark.parametrize("invalid_input", [-1, -100])
def test_negative_inputs(invalid_input):
    assert f(invalid_input) == []

def test_alternating_pattern():
    result = f(4)
    # Odd indices (1,3) should be sums
    assert result[0] == 1  # sum of numbers up to 1
    assert result[2] == 6  # sum of numbers up to 3
    # Even indices (2,4) should be factorials
    assert result[1] == 2  # factorial of 2
    assert result[3] == 24  # factorial of 4

def test_large_input():
    result = f(10)
    assert len(result) == 10
    assert result[-1] == 3628800  # 10!

@pytest.mark.parametrize("input_type", [
    1.5,
    "string",
    None,
    [],
    {}
])
def test_invalid_types(input_type):
    with pytest.raises((TypeError, ValueError)):
        f(input_type)
