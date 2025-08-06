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

def test_basic_polynomial():
    assert derivative([3, 1, 2, 4, 5]) == [1, 4, 12, 20]
    assert derivative([1, 2, 3]) == [2, 6]

@pytest.mark.parametrize("input_list,expected", [
    ([0, 0, 0, 0], [0, 0, 0]),
    ([1, 0, 0, 0], [0, 0, 0]),
    ([1, 1], [1]),
    ([5], []),
    ([], []),
])
def test_edge_cases(input_list, expected):
    assert derivative(input_list) == expected

@pytest.mark.parametrize("input_list,expected", [
    ([1, 2, 3, 4, 5], [2, 6, 12, 20]),
    ([-1, -2, -3], [-2, -6]),
    ([0.5, 1.5, 2.5], [1.5, 5.0]),
    ([10, -10, 10, -10], [-10, 20, -30]),
])
def test_various_coefficients(input_list, expected):
    assert derivative(input_list) == expected

def test_single_term():
    assert derivative([42]) == []

def test_linear():
    assert derivative([1, 1]) == [1]

def test_quadratic():
    assert derivative([1, 2, 1]) == [2, 2]

@pytest.mark.parametrize("input_list", [
    None,
    123,
    [1, None, 3],
    ["a", "b", "c"],
    [{}, {}, {}],
])
def test_invalid_inputs(input_list):
    with pytest.raises((TypeError, ValueError)):
        derivative(input_list)