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

def test_single_element():
    assert f(1) == [1]

def test_two_elements():
    assert f(2) == [1, 2]

def test_basic_sequence():
    assert f(4) == [1, 2, 6, 24]

def test_larger_sequence():
    assert f(6) == [1, 2, 6, 24, 15, 720]

@pytest.mark.parametrize("n,expected", [
    (3, [1, 2, 6]),
    (5, [1, 2, 6, 24, 15]),
    (7, [1, 2, 6, 24, 15, 720, 28])
])
def test_various_lengths(n, expected):
    assert f(n) == expected

def test_negative_input():
    assert f(-1) == []

@pytest.mark.parametrize("n", [1.5, "3", None, [1, 2], {}])
def test_invalid_types(n):
    with pytest.raises((TypeError, ValueError)):
        f(n)

def test_large_number():
    result = f(10)
    assert len(result) == 10
    assert result[-1] == 3628800  # 10!

def test_alternating_pattern():
    result = f(4)
    # Odd indices should be sums, even indices should be factorials
    assert result[0] == 1  # sum of numbers from 1 to 1
    assert result[1] == 2  # factorial of 2
    assert result[2] == 6  # sum of numbers from 1 to 3
    assert result[3] == 24  # factorial of 4
