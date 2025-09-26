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

def test_is_equal_to_sum_even():
    assert is_equal_to_sum_even(8) == True
    assert is_equal_to_sum_even(10) == True
    assert is_equal_to_sum_even(12) == True
    assert is_equal_to_sum_even(7) == False
    assert is_equal_to_sum_even(9) == False
    assert is_equal_to_sum_even(11) == False
    assert is_equal_to_sum_even(0) == False
    assert is_equal_to_sum_even(-2) == False
    assert is_equal_to_sum_even(-4) == False

@pytest.mark.parametrize("input,expected", [
    (8, True),
    (10, True),
    (12, True),
    (7, False),
    (9, False),
    (11, False),
    (0, False),
    (-2, False),
    (-4, False)
])
def test_is_equal_to_sum_even_parametrized(input, expected):
    assert is_equal_to_sum_even(input) == expected