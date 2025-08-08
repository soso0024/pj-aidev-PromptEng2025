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

def test_empty_list():
    assert derivative([]) == []

def test_single_element():
    assert derivative([5]) == []

def test_two_elements():
    assert derivative([1, 2]) == [2]

def test_multiple_elements():
    assert derivative([1, 2, 3]) == [2, 6]

def test_zeros():
    assert derivative([0, 0, 0, 0]) == [0, 0, 0]

def test_negative_numbers():
    assert derivative([-1, -2, -3]) == [-2, -6]

def test_mixed_numbers():
    assert derivative([1, -2, 3, -4]) == [-2, 6, -12]

@pytest.mark.parametrize("input_list,expected", [
    ([1, 2, 3, 4], [2, 6, 12]),
    ([0], []),
    ([1.5, 2.5], [2.5]),
    ([-1, 0, 1], [0, 2]),
    ([10, -10, 10], [-10, 20])
])
def test_derivative_parametrize(input_list, expected):
    assert derivative(input_list) == expected

def test_large_numbers():
    assert derivative([1000, 2000, 3000]) == [2000, 6000]

def test_floating_point():
    result = derivative([0.5, 1.5, 2.5])
    assert len(result) == 2
    assert abs(result[0] - 1.5) < 1e-10
    assert abs(result[1] - 5.0) < 1e-10

@pytest.mark.xfail(raises=TypeError)
def test_invalid_input_none():
    derivative(None)

@pytest.mark.xfail(raises=TypeError)
def test_invalid_input_string():
    derivative(['a', 'b', 'c'])

@pytest.mark.xfail(raises=TypeError)
def test_invalid_input_mixed():
    derivative([1, 'a', 2.5])
