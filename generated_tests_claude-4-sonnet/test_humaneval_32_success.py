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

def poly(xs, x):
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

def test_find_zero_linear_positive_slope():
    xs = [-1, 1]  # x - 1 = 0, root at x = 1
    result = find_zero(xs)
    assert abs(result - 1.0) < 1e-9

def test_find_zero_linear_negative_slope():
    xs = [1, -1]  # -x + 1 = 0, root at x = 1
    result = find_zero(xs)
    assert abs(result - 1.0) < 1e-9

def test_find_zero_quadratic():
    xs = [-1, 0, 1]  # x^2 - 1 = 0, roots at x = ±1
    result = find_zero(xs)
    assert abs(result - (-1.0)) < 1e-9 or abs(result - 1.0) < 1e-9

def test_find_zero_quadratic_shifted():
    xs = [-4, 0, 1]  # x^2 - 4 = 0, roots at x = ±2
    result = find_zero(xs)
    assert abs(result - (-2.0)) < 1e-9 or abs(result - 2.0) < 1e-9

def test_find_zero_higher_degree():
    xs = [0, -1, 0, 1]  # x^3 - x = x(x^2 - 1) = 0, roots at x = 0, ±1
    result = find_zero(xs)
    assert abs(result) < 1e-9 or abs(result - (-1.0)) < 1e-9 or abs(result - 1.0) < 1e-9

def test_find_zero_large_coefficients():
    xs = [-1000, 1000]  # 1000x - 1000 = 0, root at x = 1
    result = find_zero(xs)
    assert abs(result - 1.0) < 1e-9

def test_find_zero_small_coefficients():
    xs = [-1e-6, 1e-6]  # 1e-6 * x - 1e-6 = 0, root at x = 1
    result = find_zero(xs)
    assert abs(result - 1.0) < 1e-9

def test_find_zero_fractional_root():
    xs = [-0.5, 1]  # x - 0.5 = 0, root at x = 0.5
    result = find_zero(xs)
    assert abs(result - 0.5) < 1e-9

def test_find_zero_negative_root():
    xs = [2, 1]  # x + 2 = 0, root at x = -2
    result = find_zero(xs)
    assert abs(result - (-2.0)) < 1e-9