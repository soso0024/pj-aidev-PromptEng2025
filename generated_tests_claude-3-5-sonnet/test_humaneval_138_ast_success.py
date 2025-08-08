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

@pytest.mark.parametrize("n,expected", [
    (8, True),    # Minimum valid even number
    (10, True),   # Even number > 8
    (100, True),  # Large even number
    (6, False),   # Even number < 8
    (7, False),   # Odd number < 8
    (9, False),   # Odd number > 8
    (0, False),   # Zero
    (-2, False),  # Negative even
    (-3, False),  # Negative odd
])
def test_is_equal_to_sum_even(n, expected):
    assert is_equal_to_sum_even(n) == expected

def test_is_equal_to_sum_even_type_error():
    with pytest.raises(TypeError):
        is_equal_to_sum_even("not a number")
    with pytest.raises(TypeError):
        is_equal_to_sum_even([1, 2, 3])
    with pytest.raises(TypeError):
        is_equal_to_sum_even(None)

def test_is_equal_to_sum_even_float():
    assert is_equal_to_sum_even(8.0) == True
    assert is_equal_to_sum_even(9.0) == False