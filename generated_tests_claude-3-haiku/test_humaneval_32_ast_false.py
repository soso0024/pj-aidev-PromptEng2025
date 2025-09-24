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

def poly(xs, x):
    result = 0
    for coeff in xs:
        result = result * x + coeff
    return result

def find_zero(xs: list):
    begin, end = -1., 1.
    while poly(xs, begin) * poly(xs, end) > 0:
        if begin == 0 or end == 0:
            return 0.0
        begin *= 2.0
        end *= 2.0
    while abs(end - begin) > 1e-10:
        center = (begin + end) / 2.0
        if poly(xs, center) * poly(xs, begin) > 0:
            begin = center
        else:
            end = center
    return (begin + end) / 2.0

def test_find_zero_simple():
    assert abs(find_zero([1, -1]) - 1.0) < 1e-10

def test_find_zero_multiple_roots():
    assert abs(find_zero([1, -1, 1]) - 1.0) < 1e-10
    assert abs(find_zero([1, -1, -1]) - 0.0) < 1e-10

def test_find_zero_edge_cases():
    assert abs(find_zero([0]) - 0.0) < 1e-10
    assert abs(find_zero([1, 0]) - 0.0) < 1e-10
    assert find_zero([1, 1]) is None

@pytest.mark.parametrize("coefficients,expected", [
    ([1, -1, 1], 1.0),
    ([1, -1, -1], 0.0),
    ([0], 0.0),
    ([1, 0], 0.0),
    ([1, 1], None)
])
def test_find_zero_with_parameters(coefficients, expected):
    result = find_zero(coefficients)
    if expected is None:
        assert result is None
    else:
        assert abs(result - expected) < 1e-10