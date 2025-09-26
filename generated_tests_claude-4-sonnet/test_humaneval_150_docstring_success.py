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

def test_x_or_y_prime_numbers():
    assert x_or_y(2, 10, 20) == 10
    assert x_or_y(3, 10, 20) == 10
    assert x_or_y(5, 10, 20) == 10
    assert x_or_y(7, 34, 12) == 34
    assert x_or_y(11, 100, 200) == 100
    assert x_or_y(13, 'prime', 'not_prime') == 'prime'
    assert x_or_y(17, True, False) == True
    assert x_or_y(19, [1, 2], [3, 4]) == [1, 2]

def test_x_or_y_composite_numbers():
    assert x_or_y(4, 10, 20) == 20
    assert x_or_y(6, 10, 20) == 20
    assert x_or_y(8, 10, 20) == 20
    assert x_or_y(9, 10, 20) == 20
    assert x_or_y(10, 10, 20) == 20
    assert x_or_y(12, 10, 20) == 20
    assert x_or_y(15, 8, 5) == 5
    assert x_or_y(16, 'prime', 'not_prime') == 'not_prime'
    assert x_or_y(18, True, False) == False
    assert x_or_y(20, [1, 2], [3, 4]) == [3, 4]

def test_x_or_y_edge_cases():
    assert x_or_y(1, 10, 20) == 20
    assert x_or_y(0, 10, 20) == 10
    assert x_or_y(-1, 10, 20) == 10
    assert x_or_y(-5, 10, 20) == 10

def test_x_or_y_large_primes():
    assert x_or_y(23, 'x', 'y') == 'x'
    assert x_or_y(29, 'x', 'y') == 'x'
    assert x_or_y(31, 'x', 'y') == 'x'
    assert x_or_y(37, 'x', 'y') == 'x'

def test_x_or_y_large_composites():
    assert x_or_y(21, 'x', 'y') == 'y'
    assert x_or_y(25, 'x', 'y') == 'y'
    assert x_or_y(27, 'x', 'y') == 'y'
    assert x_or_y(33, 'x', 'y') == 'y'

@pytest.mark.parametrize("n,x,y,expected", [
    (2, 1, 0, 1),
    (3, 1, 0, 1),
    (4, 1, 0, 0),
    (5, 1, 0, 1),
    (6, 1, 0, 0),
    (7, 1, 0, 1),
    (8, 1, 0, 0),
    (9, 1, 0, 0),
    (10, 1, 0, 0),
    (11, 1, 0, 1)
])
def test_x_or_y_parametrized(n, x, y, expected):
    assert x_or_y(n, x, y) == expected

def test_x_or_y_different_types():
    assert x_or_y(2, None, 'not_none') == None
    assert x_or_y(4, None, 'not_none') == 'not_none'
    assert x_or_y(3, 0, 1) == 0
    assert x_or_y(6, 0, 1) == 1
    assert x_or_y(5, [], {}) == []
    assert x_or_y(8, [], {}) == {}
