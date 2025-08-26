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

def test_generate_integers_normal_range():
    assert generate_integers(2, 8) == [2, 4, 6, 8]

def test_generate_integers_reverse_order():
    assert generate_integers(8, 2) == [2, 4, 6, 8]

def test_generate_integers_lower_bound():
    assert generate_integers(1, 3) == [2]

def test_generate_integers_upper_bound():
    assert generate_integers(7, 10) == [8]

def test_generate_integers_no_even_numbers():
    assert generate_integers(1, 3) == [2]

def test_generate_integers_single_number():
    assert generate_integers(4, 4) == [4]

def test_generate_integers_large_range():
    assert generate_integers(1, 20) == [2, 4, 6, 8]

def test_generate_integers_negative_numbers():
    assert generate_integers(-5, 5) == [2, 4]

def test_generate_integers_equal_bounds():
    assert generate_integers(4, 4) == [4]

def test_generate_integers_zero_included():
    assert generate_integers(-2, 2) == [2]
