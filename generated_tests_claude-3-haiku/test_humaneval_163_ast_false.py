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
from your_module import generate_integers

import pytest

@pytest.mark.parametrize("a, b, expected", [
    (2, 4, [2, 4]),
    (3, 7, [4, 6]),
    (1, 8, [2, 4, 6, 8]),
    (8, 2, [2, 4, 6, 8]),
    (-1, 3, [2]),
    (4, 4, [4]),
    (1, 1, []),
])
def test_generate_integers(a, b, expected):
    assert generate_integers(a, b) == expected

def test_generate_integers_negative_values():
    with pytest.raises(ValueError):
        generate_integers(-1, -3)

def test_generate_integers_zero_values():
    with pytest.raises(ValueError):
        generate_integers(0, 0)