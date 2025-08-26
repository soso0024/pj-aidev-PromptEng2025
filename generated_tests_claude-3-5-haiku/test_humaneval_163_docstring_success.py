# Test cases for HumanEval/163
# Generated using Claude API


def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """

    lower = max(2, min(a, b))
    upper = min(8, max(a, b))

    return [i for i in range(lower, upper+1) if i % 2 == 0]


# Generated test cases:
import pytest

def test_generate_integers_normal_order():
    assert generate_integers(2, 8) == [2, 4, 6, 8]

def test_generate_integers_reverse_order():
    assert generate_integers(8, 2) == [2, 4, 6, 8]

def test_generate_integers_no_even_digits():
    assert generate_integers(10, 14) == []

def test_generate_integers_single_even_digit():
    assert generate_integers(4, 4) == [4]

def test_generate_integers_lower_bound_less_than_two():
    assert generate_integers(1, 7) == [2, 4, 6]

def test_generate_integers_upper_bound_greater_than_eight():
    assert generate_integers(3, 10) == [4, 6, 8]

def test_generate_integers_both_bounds_outside_range():
    assert generate_integers(1, 10) == [2, 4, 6, 8]

def test_generate_integers_same_bounds_no_match():
    assert generate_integers(3, 5) == [4]

def test_generate_integers_equal_bounds_even():
    assert generate_integers(6, 6) == [6]

def test_generate_integers_equal_bounds_odd():
    assert generate_integers(5, 5) == []
