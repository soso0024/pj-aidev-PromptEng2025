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
            ret += [x]
        else:
            x = 0
            for j in range(1,i+1): x += j
            ret += [x]
    return ret

def test_f_zero():
    assert f(0) == []

def test_f_one():
    assert f(1) == [1]

def test_f_two():
    assert f(2) == [1, 2]

def test_f_three():
    assert f(3) == [1, 2, 6]

def test_f_four():
    assert f(4) == [1, 2, 6, 24]

def test_f_five():
    assert f(5) == [1, 2, 6, 24, 15]

def test_f_six():
    assert f(6) == [1, 2, 6, 24, 15, 720]

def test_f_seven():
    assert f(7) == [1, 2, 6, 24, 15, 720, 28]

def test_f_eight():
    assert f(8) == [1, 2, 6, 24, 15, 720, 28, 40320]

@pytest.mark.parametrize("n,expected", [
    (1, [1]),
    (2, [1, 2]),
    (3, [1, 2, 6]),
    (4, [1, 2, 6, 24]),
    (5, [1, 2, 6, 24, 15]),
    (6, [1, 2, 6, 24, 15, 720]),
    (10, [1, 2, 6, 24, 15, 720, 28, 40320, 45, 3628800])
])
def test_f_parametrized(n, expected):
    assert f(n) == expected

def test_f_large_number():
    result = f(12)
    assert len(result) == 12
    assert result[0] == 1  # sum 1 to 1
    assert result[1] == 2  # factorial of 2
    assert result[2] == 6  # sum 1 to 3
    assert result[3] == 24  # factorial of 4
    assert result[10] == 66  # sum 1 to 11
    assert result[11] == 479001600  # factorial of 12

def test_f_negative():
    assert f(-1) == []
    assert f(-5) == []
