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

def test_derivative_example_1():
    assert derivative([3, 1, 2, 4, 5]) == [1, 4, 12, 20]

def test_derivative_example_2():
    assert derivative([1, 2, 3]) == [2, 6]

def test_derivative_empty_list():
    assert derivative([]) == []

def test_derivative_single_constant():
    assert derivative([5]) == []

def test_derivative_linear():
    assert derivative([2, 3]) == [3]

def test_derivative_quadratic():
    assert derivative([1, 2, 3]) == [2, 6]

def test_derivative_cubic():
    assert derivative([0, 1, 2, 3]) == [1, 4, 9]

def test_derivative_with_zeros():
    assert derivative([0, 0, 5, 0, 2]) == [0, 10, 0, 8]

def test_derivative_all_zeros():
    assert derivative([0, 0, 0, 0]) == [0, 0, 0]

def test_derivative_negative_coefficients():
    assert derivative([-1, -2, -3, -4]) == [-2, -6, -12]

def test_derivative_mixed_signs():
    assert derivative([1, -2, 3, -4]) == [-2, 6, -12]

def test_derivative_float_coefficients():
    assert derivative([1.5, 2.5, 3.5]) == [2.5, 7.0]

def test_derivative_large_polynomial():
    assert derivative([1, 2, 3, 4, 5, 6, 7]) == [2, 6, 12, 20, 30, 42]

@pytest.mark.parametrize("input_coeffs,expected", [
    ([0], []),
    ([1, 0], [0]),
    ([0, 1], [1]),
    ([2, 4, 6], [4, 12]),
    ([-5, 10, -15], [10, -30])
])
def test_derivative_parametrized(input_coeffs, expected):
    assert derivative(input_coeffs) == expected
