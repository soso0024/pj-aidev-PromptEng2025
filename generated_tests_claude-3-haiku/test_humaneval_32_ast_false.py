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
import math
import pytest

def poly(xs: list, x: float):
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    if len(xs) % 2 != 0 or max(xs) == 0:
        raise ValueError("Invalid input: xs must have even number of coefficients and largest non-zero coefficient")
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

def test_find_zero_simple():
    assert abs(find_zero([1, -1]) - 1.0) < 1e-10

def test_find_zero_multiple_roots():
    assert abs(find_zero([1, -1, 1]) - 1.0) < 1e-10
    assert abs(find_zero([1, -1, -1]) - 0.0) < 1e-10

def test_find_zero_edge_cases():
    assert abs(find_zero([1]) - (-1.0)) < 1e-10
    assert abs(find_zero([-1]) - 1.0) < 1e-10

@pytest.mark.parametrize("input,expected", [
    ([1, 2, 3], -0.5773502691896258),
    ([1, -2, 1], 1.0),
    ([1, 0, -1], 0.0),
    ([1, 1, 1], -1.0),
    ([1, -1, 1], 0.0)
])
def test_find_zero_with_parameters(input, expected):
    assert abs(find_zero(input) - expected) < 1e-10

def test_find_zero_empty_list():
    with pytest.raises(ValueError):
        find_zero([])