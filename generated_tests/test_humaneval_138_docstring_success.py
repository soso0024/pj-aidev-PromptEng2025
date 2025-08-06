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

def test_is_equal_to_sum_even_basic_true():
    assert is_equal_to_sum_even(8) == True
    assert is_equal_to_sum_even(10) == True
    assert is_equal_to_sum_even(12) == True

def test_is_equal_to_sum_even_basic_false():
    assert is_equal_to_sum_even(4) == False
    assert is_equal_to_sum_even(6) == False
    assert is_equal_to_sum_even(2) == False

def test_is_equal_to_sum_even_odd_numbers():
    assert is_equal_to_sum_even(9) == False
    assert is_equal_to_sum_even(15) == False
    assert is_equal_to_sum_even(21) == False

def test_is_equal_to_sum_even_zero_and_negative():
    assert is_equal_to_sum_even(0) == False
    assert is_equal_to_sum_even(-8) == False
    assert is_equal_to_sum_even(-4) == False

@pytest.mark.parametrize("number,expected", [
    (8, True),
    (10, True),
    (12, True),
    (4, False),
    (6, False),
    (7, False),
    (9, False),
    (0, False),
    (-8, False),
    (100, True),
    (1000, True)
])
def test_is_equal_to_sum_even_parametrized(number, expected):
    assert is_equal_to_sum_even(number) == expected

def test_is_equal_to_sum_even_large_numbers():
    assert is_equal_to_sum_even(1000) == True
    assert is_equal_to_sum_even(10000) == True
    assert is_equal_to_sum_even(999) == False

def test_is_equal_to_sum_even_edge_cases():
    assert is_equal_to_sum_even(8) == True  # Minimum valid number
    assert is_equal_to_sum_even(7) == False  # Just below minimum valid number
    assert is_equal_to_sum_even(9) == False  # Odd number just above minimum
