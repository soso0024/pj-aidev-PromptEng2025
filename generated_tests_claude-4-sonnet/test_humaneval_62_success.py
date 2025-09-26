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

def test_derivative_single_element():
    assert derivative([5]) == []

def test_derivative_two_elements():
    assert derivative([3, 7]) == [7]

def test_derivative_constant_polynomial():
    assert derivative([42]) == []

def test_derivative_linear_polynomial():
    assert derivative([2, 5]) == [5]

def test_derivative_quadratic_polynomial():
    assert derivative([1, 2, 3]) == [2, 6]

def test_derivative_cubic_polynomial():
    assert derivative([4, 3, 2, 1]) == [3, 4, 3]

def test_derivative_with_zeros():
    assert derivative([0, 0, 5, 0]) == [0, 10, 0]

def test_derivative_with_negative_coefficients():
    assert derivative([-1, -2, -3]) == [-2, -6]

def test_derivative_with_mixed_signs():
    assert derivative([1, -2, 3, -4]) == [-2, 6, -12]

def test_derivative_with_floats():
    assert derivative([1.5, 2.5, 3.5]) == [2.5, 7.0]

def test_derivative_large_polynomial():
    input_poly = [1, 2, 3, 4, 5, 6]
    expected = [2, 6, 12, 20, 30]
    assert derivative(input_poly) == expected

@pytest.mark.parametrize("input_list,expected", [
    ([0], []),
    ([1, 0], [0]),
    ([0, 1], [1]),
    ([1, 1, 1], [1, 2]),
    ([2, 4, 6, 8], [4, 12, 24])
])
def test_derivative_parametrized(input_list, expected):
    assert derivative(input_list) == expected

def test_derivative_all_zeros():
    assert derivative([0, 0, 0, 0]) == [0, 0, 0]

def test_derivative_alternating_signs():
    assert derivative([1, -1, 1, -1]) == [-1, 2, -3]
