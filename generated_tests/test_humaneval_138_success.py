# Test cases for HumanEval/138
# Generated using Claude API


def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """

    return n%2 == 0 and n >= 8


# Generated test cases:
import pytest

def test_is_equal_to_sum_even_basic():
    assert is_equal_to_sum_even(8) == True
    assert is_equal_to_sum_even(10) == True
    assert is_equal_to_sum_even(7) == False

@pytest.mark.parametrize("number,expected", [
    (0, False),
    (2, False),
    (6, False),
    (8, True),
    (10, True),
    (100, True),
    (-2, False),
    (-8, False),
    (7, False),
    (9, False),
    (1000000, True)
])
def test_is_equal_to_sum_even_parametrized(number, expected):
    assert is_equal_to_sum_even(number) == expected

def test_is_equal_to_sum_even_edge_cases():
    assert is_equal_to_sum_even(-1000) == False
    assert is_equal_to_sum_even(7.5) == False
    assert is_equal_to_sum_even(8.0) == True

@pytest.mark.parametrize("invalid_input", [
    "string",
    None,
    [],
    {},
])
def test_is_equal_to_sum_even_invalid_inputs(invalid_input):
    with pytest.raises((TypeError, ValueError)):
        is_equal_to_sum_even(invalid_input)

def test_is_equal_to_sum_even_bool_inputs():
    assert is_equal_to_sum_even(True) == False
    assert is_equal_to_sum_even(False) == False