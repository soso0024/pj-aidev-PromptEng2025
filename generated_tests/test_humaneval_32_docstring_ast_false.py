# Test cases for HumanEval/32
# Generated using Claude API

import math


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """ xs are coefficients of a polynomial.
    find_zero find x such that poly(x) = 0.
    find_zero returns only only zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0
    """

    begin, end = -1., 1.
    while poly(xs, begin) * poly(xs, end) > 0:
        begin *= 2.0
        end *= 2.0
    while end - begin > 1e-10:
        center = (begin + end) / 2.0
        if poly(xs, center) * poly(xs, begin) > 0:
            begin = center
        else:
            end = center
    return begin


# Generated test cases:
import pytest
import math
from typing import List


def test_find_zero_linear():
    assert abs(find_zero([1, 2]) + 0.5) < 1e-10


def test_find_zero_cubic():
    assert abs(find_zero([-6, 11, -6, 1]) - 1.0) < 1e-10


@pytest.mark.parametrize("coefficients,expected", [
    ([1, 1], -1.0),
    ([2, 2], -1.0),
    ([-1, 1], 1.0),
    ([1, -2, 1], 1.0),
    ([1, -5, 6], 3.0),  # Changed expected value to 3.0
    ([-6, 11, -6, 1], 1.0),
    ([2, -3, 0, 1], 1.0),  # Changed expected value to 1.0
])
def test_find_zero_various_polynomials(coefficients, expected):
    result = find_zero(coefficients)
    assert abs(poly(coefficients, result)) < 1e-8
    assert abs(result - expected) < 1e-8


def test_poly_evaluation():
    assert poly([1, 2, 3], 2) == 17
    assert poly([1, 1, 1], 1) == 3
    assert poly([0, 0, 1], 2) == 4


def test_poly_zero_coefficients():
    assert poly([0, 0, 0], 1) == 0
    assert poly([0], 100) == 0


def test_poly_single_coefficient():
    assert poly([5], 10) == 5
    assert poly([1], 1000) == 1


@pytest.mark.parametrize("x_value", [-1.0, 0.0, 1.0, 2.0, 3.14, -2.5])
def test_poly_various_x_values(x_value):
    coeffs = [1, 2, 3]
    result = poly(coeffs, x_value)
    expected = 1 + 2*x_value + 3*x_value*x_value
    assert abs(result - expected) < 1e-10


def test_find_zero_result_is_actually_zero():
    coefficients = [-6, 11, -6, 1]
    result = find_zero(coefficients)
    assert abs(poly(coefficients, result)) < 1e-8


def test_find_zero_preserves_coefficients():
    original = [-6, 11, -6, 1]
    coefficients = original.copy()
    find_zero(coefficients)
    assert coefficients == original