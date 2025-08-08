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
    return sum(coef * (x ** power) for power, coef in enumerate(xs))

def find_zero(xs: list):
    if len(xs) == 1 and xs[0] == 0:
        raise ZeroDivisionError("Constant polynomial with zero coefficient")
    
    begin, end = -1., 1.
    max_iterations = 1000
    iterations = 0
    
    while poly(xs, begin) * poly(xs, end) > 0:
        begin *= 2.0
        end *= 2.0
        iterations += 1
        if iterations > max_iterations:
            raise RecursionError("No real roots found")
    
    iterations = 0
    while end - begin > 1e-10:
        center = (begin + end) / 2.0
        if poly(xs, center) * poly(xs, begin) > 0:
            begin = center
        else:
            end = center
        
        iterations += 1
        if iterations > max_iterations:
            break
    
    return begin

def test_find_zero_linear():
    assert math.isclose(find_zero([1, -1]), 1.0, abs_tol=1e-10)

def test_find_zero_quadratic():
    assert math.isclose(find_zero([1, 0, -1]), 1.0, abs_tol=1e-10)

def test_find_zero_cubic():
    assert math.isclose(find_zero([1, 0, -1, 0]), 1.0, abs_tol=1e-10)

def test_find_zero_complex_polynomial():
    result = find_zero([1, -3, 3, -1])
    assert math.isclose(result, 1.0, abs_tol=1e-10)

def test_find_zero_near_zero():
    result = find_zero([1, 1])
    assert math.isclose(result, -1.0, abs_tol=1e-10)

@pytest.mark.parametrize("coefficients,expected", [
    ([1, -1], 1.0),
    ([1, 0, -1], 1.0),
    ([1, 0, -1, 0], 1.0),
    ([1, -3, 3, -1], 1.0),
    ([1, 1], -1.0)
])
def test_find_zero_parametrized(coefficients, expected):
    result = find_zero(coefficients)
    assert math.isclose(result, expected, abs_tol=1e-10)

def test_find_zero_constant_polynomial():
    with pytest.raises(ZeroDivisionError):
        find_zero([0])

def test_find_zero_no_real_roots():
    with pytest.raises(RecursionError):
        find_zero([1, 1, 1])