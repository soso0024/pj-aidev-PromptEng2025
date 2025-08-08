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
from polynomial import poly, find_zero

@pytest.mark.parametrize("coefficients,expected", [
    ([1, -1], 1.0),  
    ([-2, 1], 2.0),  
    ([2, -3], 1.5),
    ([1, -2], 0.5),
])
def test_find_zero_basic(coefficients, expected):
    result = find_zero(coefficients)
    assert abs(result - expected) < 1e-6
    assert abs(poly(coefficients, result)) < 1e-6

@pytest.mark.parametrize("coefficients", [
    [-6, 11, -6, 1],
    [1, -5, 6, -2],
])
def test_find_zero_higher_degree(coefficients):
    result = find_zero(coefficients)
    assert abs(poly(coefficients, result)) < 1e-6

def test_find_zero_small_coefficients():
    coefficients = [0.0001, -0.0002]
    result = find_zero(coefficients)
    assert abs(poly(coefficients, result)) < 1e-6

def test_find_zero_large_coefficients():
    coefficients = [1000, -2000]
    result = find_zero(coefficients)
    assert abs(poly(coefficients, result)) < 1e-6

def test_find_zero_alternating_signs():
    coefficients = [2, -3, 1]
    result = find_zero(coefficients)
    assert abs(poly(coefficients, result)) < 1e-6

def test_find_zero_precision():
    coefficients = [1, -2]
    result = find_zero(coefficients)
    assert abs(result - 0.5) < 1e-6

def test_find_zero_boundary():
    coefficients = [-1, 1]
    result = find_zero(coefficients)
    assert abs(result - 1.0) < 1e-6

def test_poly_evaluation():
    assert abs(poly([1, 1], 2) - 3) < 1e-6
    assert abs(poly([1, -1], 1)) < 1e-6
    assert abs(poly([0, 1], 5) - 5) < 1e-6