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
from solution import generate_integers

@pytest.mark.parametrize("a, b, expected", [
    (2, 6, [2, 4, 6]),
    (1, 9, [2, 4, 6, 8]),
    (3, 7, [4, 6]),
    (0, 10, [2, 4, 6, 8]),
    (-2, 4, [2, 4]),
    (8, 2, [2, 4, 6, 8]),
    (1, 1, []),
    (0, 0, []),
    (2.5, 6.5, [4, 6]),
])
def test_generate_integers(a, b, expected):
    assert generate_integers(a, b) == expected

def test_generate_integers_empty_range():
    assert generate_integers(10, 2) == [2, 4, 6, 8]

def test_generate_integers_single_even_number():
    assert generate_integers(4, 4) == [4]

def test_generate_integers_single_odd_number():
    assert generate_integers(3, 3) == []

def test_generate_integers_non_numeric_input():
    with pytest.raises(TypeError):
        generate_integers('a', 'b')