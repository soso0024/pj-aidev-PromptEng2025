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
    if len(xs) <= 1:
        return []
    return [0] + [(i * x) for i, x in enumerate(xs)][1:]

def test_derivative_normal_case():
    assert derivative([1, 2, 3, 4]) == [0, 2, 6, 12]

def test_derivative_empty_list():
    assert derivative([]) == []

def test_derivative_single_element():
    assert derivative([5]) == []

def test_derivative_zero_list():
    assert derivative([0, 0, 0, 0]) == [0, 0, 0, 0]

def test_derivative_negative_numbers():
    assert derivative([-1, -2, -3, -4]) == [0, -2, -6, -12]

def test_derivative_mixed_numbers():
    assert derivative([1, -2, 3, -4]) == [0, -2, 6, -12]

@pytest.mark.parametrize("input_list,expected", [
    ([1, 2, 3, 4], [0, 2, 6, 12]),
    ([], []),
    ([5], []),
    ([0, 0, 0, 0], [0, 0, 0, 0]),
    ([-1, -2, -3, -4], [0, -2, -6, -12]),
    ([1, -2, 3, -4], [0, -2, 6, -12])
])
def test_derivative_parametrized(input_list, expected):
    assert derivative(input_list) == expected