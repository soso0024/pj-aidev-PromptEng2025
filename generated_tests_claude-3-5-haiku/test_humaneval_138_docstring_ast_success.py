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

def test_is_equal_to_sum_even_basic_cases():
    assert is_equal_to_sum_even(8) == True
    assert is_equal_to_sum_even(10) == True
    assert is_equal_to_sum_even(12) == True
    assert is_equal_to_sum_even(14) == True

def test_is_equal_to_sum_even_negative_cases():
    assert is_equal_to_sum_even(4) == False
    assert is_equal_to_sum_even(6) == False
    assert is_equal_to_sum_even(7) == False
    assert is_equal_to_sum_even(3) == False

def test_is_equal_to_sum_even_boundary_cases():
    assert is_equal_to_sum_even(8) == True
    assert is_equal_to_sum_even(16) == True
    assert is_equal_to_sum_even(32) == True

@pytest.mark.parametrize("input,expected", [
    (8, True),
    (10, True),
    (12, True),
    (14, True),
    (4, False),
    (6, False),
    (7, False),
    (3, False)
])
def test_is_equal_to_sum_even_parametrized(input, expected):
    assert is_equal_to_sum_even(input) == expected

def test_is_equal_to_sum_even_large_numbers():
    assert is_equal_to_sum_even(100) == True
    assert is_equal_to_sum_even(1000) == True

def test_is_equal_to_sum_even_zero_and_negative():
    assert is_equal_to_sum_even(0) == False
    assert is_equal_to_sum_even(-8) == False
