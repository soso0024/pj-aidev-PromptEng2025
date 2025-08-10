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
from your_module import is_equal_to_sum_even
import pytest

@pytest.mark.parametrize("n,expected", [
    (8, True),
    (10, True),
    (12, True),
    (7, False),
    (9, False),
    (11, False),
    (0, False),
    (-2, False),
    (-4, False),
    (-1, False),
    (-3, False),
    (-5, False),
])
def test_is_equal_to_sum_even(n, expected):
    assert is_equal_to_sum_even(n) == expected

def test_is_equal_to_sum_even_type_error():
    with pytest.raises(TypeError):
        is_equal_to_sum_even("not_a_number")