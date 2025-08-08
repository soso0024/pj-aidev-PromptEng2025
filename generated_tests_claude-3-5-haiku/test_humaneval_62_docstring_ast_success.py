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
    if not isinstance(xs, list):
        raise TypeError("Input must be a list")
    return [(i * x) for i, x in enumerate(xs)][1:]

def test_derivative_normal_cases():
    assert derivative([3, 1, 2, 4, 5]) == [1, 4, 12, 20]
    assert derivative([1, 2, 3]) == [2, 6]
    assert derivative([5, 0, 0, 2]) == [0, 0, 6]

def test_derivative_edge_cases():
    assert derivative([]) == []
    assert derivative([42]) == []
    assert derivative([0, 0, 0, 0]) == [0, 0, 0]

@pytest.mark.parametrize("input_list,expected", [
    ([1, 2, 3, 4], [2, 6, 12]),
    ([10, 0, 5, 0, 2], [0, 10, 0, 8]),
    ([-1, -2, -3], [-2, -6])
])
def test_derivative_parametrized(input_list, expected):
    assert derivative(input_list) == expected

def test_derivative_type_handling():
    with pytest.raises(TypeError):
        derivative(None)
    with pytest.raises(TypeError):
        derivative("not a list")