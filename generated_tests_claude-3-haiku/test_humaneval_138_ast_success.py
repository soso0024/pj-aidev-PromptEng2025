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

@pytest.mark.parametrize("n, expected", [
    (8, True),
    (10, True),
    (12, True),
    (7, False),
    (9, False),
    (11, False),
    (0, False),
    (-2, False),
    (float(8), True),
    (float(7), False),
    (None, TypeError),
    ('8', TypeError),
])
def test_is_equal_to_sum_even(n, expected):
    if expected is TypeError:
        with pytest.raises(TypeError):
            is_equal_to_sum_even(n)
    else:
        assert is_equal_to_sum_even(n) == expected

def is_equal_to_sum_even(n):
    return n%2 == 0 and n >= 8
