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

def test_x_or_y_normal_case():
    assert x_or_y(5, 'x', 'y') == 'x'
    assert x_or_y(6, 'x', 'y') == 'y'

def test_x_or_y_edge_cases():
    assert x_or_y(1, 'x', 'y') == 'y'
    assert x_or_y(2, 'x', 'y') == 'x'
    assert x_or_y(3, 'x', 'y') == 'x'

@pytest.mark.parametrize("n, x, y, expected", [
    (1, 'x', 'y', 'y'),
    (2, 'x', 'y', 'x'),
    (3, 'x', 'y', 'x'),
    (4, 'x', 'y', 'y'),
    (5, 'x', 'y', 'x'),
    (6, 'x', 'y', 'y'),
])
def test_x_or_y_parametrized(n, x, y, expected):
    assert x_or_y(n, x, y) == expected

def test_x_or_y_type_errors():
    with pytest.raises(TypeError):
        x_or_y('a', 'x', 'y')
    with pytest.raises(TypeError):
        x_or_y(1.5, 'x', 'y')
    with pytest.raises(TypeError):
        x_or_y(1, 1, 'y')
    with pytest.raises(TypeError):
        x_or_y(1, 'x', 1)