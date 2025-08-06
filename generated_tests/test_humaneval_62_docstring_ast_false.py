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

def test_basic_polynomial():
    assert derivative([3, 1, 2, 4, 5]) == [1, 4, 12, 20]
    assert derivative([1, 2, 3]) == [2, 6]

@pytest.mark.parametrize("input_poly,expected", [
    ([0, 0, 0, 0], [0, 0, 0]),
    ([1, 0, 0, 0], [0, 0, 0]),
    ([1, 1], [1]),
    ([5], []),
    ([1, 2, 3, 4, 5, 6], [2, 6, 12, 20, 30]),
])
def test_polynomial_derivatives(input_poly, expected):
    assert derivative(input_poly) == expected

def test_empty_list():
    assert derivative([]) == []

def test_single_constant():
    assert derivative([42]) == []

def test_linear_polynomial():
    assert derivative([0, 1]) == [1]

def test_quadratic_polynomial():
    assert derivative([1, -3, 2]) == [-3, 4]

def test_negative_coefficients():
    assert derivative([-1, -2, -3, -4]) == [-2, -6, -12]

def test_large_coefficients():
    assert derivative([1000, 2000, 3000]) == [2000, 6000]

def test_list_type():
    with pytest.raises(TypeError):
        derivative("not a list")

def test_non_numeric_elements():
    with pytest.raises(TypeError):
        derivative([1, "2", 3])