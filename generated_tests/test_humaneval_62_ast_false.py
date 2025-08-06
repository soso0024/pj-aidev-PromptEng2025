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

def test_derivative_empty_list():
    assert derivative([]) == []

def test_derivative_single_element():
    assert derivative([1]) == []

def test_derivative_two_elements():
    assert derivative([1, 2]) == [2]

def test_derivative_multiple_elements():
    assert derivative([1, 2, 3]) == [2, 6]

def test_derivative_with_zeros():
    assert derivative([0, 0, 0, 0]) == [0, 0, 0]

def test_derivative_with_negative():
    assert derivative([-1, -2, -3]) == [-2, -6]

@pytest.mark.parametrize("input_list,expected", [
    ([1, 2, 3, 4], [2, 6, 12]),
    ([0, 1, 2, 3], [1, 4, 9]),
    ([-2, -1, 0, 1], [-1, 0, 3]),
    ([1.5, 2.5, 3.5], [2.5, 7.0]),
    ([0, 0], [0]),
])
def test_derivative_parametrized(input_list, expected):
    assert derivative(input_list) == expected

@pytest.mark.parametrize("invalid_input", [
    None,
    42,
])
def test_derivative_invalid_input(invalid_input):
    with pytest.raises(TypeError):
        derivative(invalid_input)

def test_derivative_nested_lists():
    with pytest.raises(TypeError):
        derivative([[1, 2], [3, 4]])
        derivative([1, [2, 3]])

def test_derivative_non_numeric():
    with pytest.raises(TypeError):
        derivative(['a', 'b', 'c'])

def test_derivative_tuple_input():
    result = derivative((1, 2, 3))
    assert result == [2, 6]

def test_derivative_string_input():
    with pytest.raises(TypeError):
        derivative("string")