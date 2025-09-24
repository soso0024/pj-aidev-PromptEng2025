# Test cases for HumanEval/150
# Generated using Claude API


def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """

    if n == 1:
        return y
    for i in range(2, n):
        if n % i == 0:
            return y
            break
    else:
        return x


# Generated test cases:
import pytest

def x_or_y(n, x, y):
    if n == 1:
        return y
    for i in range(2, n):
        if n % i == 0:
            return y
            break
    else:
        return x

@pytest.mark.parametrize("n,x,y,expected", [
    (1, 5, 10, 10),
    (1, 'a', 'b', 'b'),
    (1, [], {}, {}),
    (2, 5, 10, 5),
    (3, 5, 10, 5),
    (5, 5, 10, 5),
    (7, 5, 10, 5),
    (11, 5, 10, 5),
    (13, 5, 10, 5),
    (17, 5, 10, 5),
    (19, 5, 10, 5),
    (23, 5, 10, 5),
    (4, 5, 10, 10),
    (6, 5, 10, 10),
    (8, 5, 10, 10),
    (9, 5, 10, 10),
    (10, 5, 10, 10),
    (12, 5, 10, 10),
    (15, 5, 10, 10),
    (16, 5, 10, 10),
    (18, 5, 10, 10),
    (20, 5, 10, 10),
    (21, 5, 10, 10),
    (22, 5, 10, 10),
    (24, 5, 10, 10),
    (25, 5, 10, 10),
    (26, 5, 10, 10),
    (27, 5, 10, 10),
    (28, 5, 10, 10),
    (100, 5, 10, 10),
    (101, 5, 10, 5),
    (103, 5, 10, 5),
    (107, 5, 10, 5),
    (109, 5, 10, 5),
    (113, 5, 10, 5),
])
def test_x_or_y_parametrized(n, x, y, expected):
    assert x_or_y(n, x, y) == expected

def test_x_or_y_with_strings():
    assert x_or_y(2, 'prime', 'composite') == 'prime'
    assert x_or_y(4, 'prime', 'composite') == 'composite'
    assert x_or_y(1, 'prime', 'composite') == 'composite'

def test_x_or_y_with_different_types():
    assert x_or_y(2, [1, 2, 3], {'a': 1}) == [1, 2, 3]
    assert x_or_y(4, [1, 2, 3], {'a': 1}) == {'a': 1}
    assert x_or_y(1, [1, 2, 3], {'a': 1}) == {'a': 1}

def test_x_or_y_with_none_values():
    assert x_or_y(2, None, 'composite') == None
    assert x_or_y(4, 'prime', None) == None
    assert x_or_y(1, 'prime', None) == None

def test_x_or_y_with_zero_values():
    assert x_or_y(2, 0, 1) == 0
    assert x_or_y(4, 0, 1) == 1
    assert x_or_y(1, 0, 1) == 1

def test_x_or_y_with_negative_values():
    assert x_or_y(2, -5, -10) == -5
    assert x_or_y(4, -5, -10) == -10
    assert x_or_y(1, -5, -10) == -10

def test_x_or_y_large_primes():
    assert x_or_y(997, 'x', 'y') == 'x'
    assert x_or_y(1009, 'x', 'y') == 'x'
    assert x_or_y(1013, 'x', 'y') == 'x'

def test_x_or_y_large_composites():
    assert x_or_y(1000, 'x', 'y') == 'y'
    assert x_or_y(1001, 'x', 'y') == 'y'
    assert x_or_y(1002, 'x', 'y') == 'y'
