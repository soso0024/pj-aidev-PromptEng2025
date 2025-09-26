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


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
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


def test_find_zero_linear_polynomial():
    result = find_zero([1, 2])
    assert abs(result - (-0.5)) < 1e-9


def test_find_zero_cubic_polynomial():
    result = find_zero([-6, 11, -6, 1])
    assert abs(result - 1.0) < 1e-9


def test_find_zero_quadratic_polynomial():
    result = find_zero([2, -3, 1])
    assert abs(poly([2, -3, 1], result)) < 1e-9


def test_find_zero_quartic_polynomial():
    result = find_zero([1, 0, -2, 0, 1])
    assert abs(poly([1, 0, -2, 0, 1], result)) < 1e-9


def test_find_zero_negative_constant():
    result = find_zero([-4, 2])
    assert abs(result - 2.0) < 1e-9


def test_find_zero_large_coefficients():
    result = find_zero([100, -50, 1])
    assert abs(poly([100, -50, 1], result)) < 1e-8


def test_find_zero_small_coefficients():
    result = find_zero([0.001, 0.002])
    assert abs(result - (-0.5)) < 1e-9


def test_find_zero_alternating_signs():
    result = find_zero([1, -1, 1, -1])
    assert abs(poly([1, -1, 1, -1], result)) < 1e-9


def test_find_zero_zero_middle_coefficients():
    result = find_zero([1, 0, 0, 1])
    assert abs(poly([1, 0, 0, 1], result)) < 1e-9


def test_find_zero_high_degree_even():
    result = find_zero([1, 0, 0, 0, 0, 1])
    assert abs(poly([1, 0, 0, 0, 0, 1], result)) < 1e-9


def test_find_zero_precision():
    result = find_zero([1, 2])
    poly_result = poly([1, 2], result)
    assert abs(poly_result) < 1e-9


def test_find_zero_different_quadratic():
    result = find_zero([-1, 0, 1])
    assert abs(result - (-1.0)) < 1e-9 or abs(result - 1.0) < 1e-9


def test_find_zero_fractional_coefficients():
    result = find_zero([0.5, 1.5])
    assert abs(result - (-1.0/3.0)) < 1e-9


def test_find_zero_large_degree():
    coeffs = [1, 0, 0, 0, 0, 0, 0, 1]
    result = find_zero(coeffs)
    assert abs(poly(coeffs, result)) < 1e-9