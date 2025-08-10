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

def derivative(xs: list):
    return [(i * x) for i, x in enumerate(xs)][1:]

def test_derivative_empty_list():
    assert derivative([]) == []

@pytest.mark.parametrize("input,expected", [
    ([1, 2, 3], [2, 6]),
    ([0, 0, 0], [0, 0]),
    ([1, -2, 3], [-2, 6]),
    ([1.5, 2.3, -4.1], [2.3, -8.2]),
    ([-1, -2, -3], [-2, -6])
])
def test_derivative_normal_cases(input, expected):
    assert derivative(input) == expected

def test_derivative_single_element_list():
    assert derivative([42]) == []

def test_derivative_type_error():
    with pytest.raises(TypeError):
        derivative(42)