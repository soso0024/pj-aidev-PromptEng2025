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

def test_x_or_y_normal_cases():
    assert x_or_y(5, 'a', 'b') == 'a'
    assert x_or_y(6, 'x', 'y') == 'y'
    assert x_or_y(7, 'hello', 'world') == 'hello'

def test_x_or_y_edge_cases():
    assert x_or_y(1, 'a', 'b') == 'b'
    assert x_or_y(2, 'x', 'y') == 'x'
    assert x_or_y(3, 'hello', 'world') == 'hello'

@pytest.mark.parametrize("n, x, y, expected", [
    (0, 'a', 'b', 'a'),
    (-1, 'x', 'y', 'x'),
    (1.5, 'hello', 'world', TypeError),
    ('test', 'foo', 'bar', TypeError),
    ([4, 5], 'baz', 'qux', TypeError)
])
def test_x_or_y_error_conditions(n, x, y, expected):
    if expected == TypeError:
        with pytest.raises(expected):
            x_or_y(n, x, y)
    else:
        assert x_or_y(n, x, y) == expected