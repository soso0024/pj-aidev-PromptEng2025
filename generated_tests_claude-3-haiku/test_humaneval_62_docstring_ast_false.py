# Test cases for HumanEval/62
# Generated using Claude API



def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """

    return [(i * x) for i, x in enumerate(xs)][1:]


# Generated test cases:
import pytest

def test_derivative_empty_list():
    assert derivative([]) == []

@pytest.mark.parametrize("input,expected", [
    ([3, 1, 2, 4, 5], [1, 4, 12, 20]),
    ([1, 2, 3], [2, 6]),
    ([0, 0, 0, 0], [0, 0, 0]),
    ([1], []),
    ([-1, 2, -3, 4], [-2, 6, -12])
])
def test_derivative_valid_input(input, expected):
    assert derivative(input) == expected

def test_derivative_non_list_input():
    with pytest.raises(TypeError):
        derivative(123)

def test_derivative_string_input():
    with pytest.raises(TypeError):
        derivative(['a', 'b', 'c'])

def derivative(xs: list):
    return [(i * x) for i, x in enumerate(xs)][1:]