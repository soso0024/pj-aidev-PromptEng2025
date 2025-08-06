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

def test_basic_true_cases():
    assert is_equal_to_sum_even(8) == True
    assert is_equal_to_sum_even(10) == True
    assert is_equal_to_sum_even(12) == True
    assert is_equal_to_sum_even(100) == True

def test_basic_false_cases():
    assert is_equal_to_sum_even(4) == False
    assert is_equal_to_sum_even(6) == False
    assert is_equal_to_sum_even(2) == False

def test_odd_numbers():
    assert is_equal_to_sum_even(9) == False
    assert is_equal_to_sum_even(11) == False
    assert is_equal_to_sum_even(15) == False

def test_zero_and_negative():
    assert is_equal_to_sum_even(0) == False
    assert is_equal_to_sum_even(-8) == False
    assert is_equal_to_sum_even(-2) == False

@pytest.mark.parametrize("number,expected", [
    (8, True),
    (10, True),
    (6, False),
    (4, False),
    (9, False),
    (0, False),
    (-8, False),
    (100, True),
    (1000, True),
])
def test_parametrized_cases(number, expected):
    assert is_equal_to_sum_even(number) == expected

@pytest.mark.parametrize("input_val", [
    "8",
    None,
    [],
    {},
])
def test_invalid_inputs(input_val):
    with pytest.raises((TypeError, AttributeError)):
        is_equal_to_sum_even(input_val)

def test_large_numbers():
    assert is_equal_to_sum_even(1000000) == True
    assert is_equal_to_sum_even(999999) == False

def test_float_inputs():
    assert is_equal_to_sum_even(2.5) == False
    assert is_equal_to_sum_even(8.0) == True