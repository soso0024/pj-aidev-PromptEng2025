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
    if len(xs) % 2 != 0:
        raise ValueError("xs must have an even number of coefficients")
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

def test_poly():
    assert poly([1, 2], 0) == 1
    assert poly([1, 2], 1) == 3
    assert poly([1, 2, 3], 2) == 17
    assert poly([-6, 11, -6, 1], 1) == 0

@pytest.mark.parametrize("coefficients,expected", [
    ([1, 2], -0.5),
    ([-6, 11, -6, 1], 1.0),
    ([1, -1], 1.0),
    ([1, -2, 1], 1.0),
    ([1, -3, 3, -1], 1.0),
    ([1, -4, 6, -4, 1], 1.0),
])
def test_find_zero(coefficients, expected):
    assert round(find_zero(coefficients), 2) == expected

def test_find_zero_empty_list():
    with pytest.raises(ValueError):
        find_zero([])

def test_find_zero_odd_number_of_coefficients():
    with pytest.raises(ValueError):
        find_zero([1, 2, 3])