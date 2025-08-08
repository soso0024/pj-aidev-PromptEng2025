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
from typing import List

def generate_integers(a: int, b: int) -> List[int]:
    lower = max(2, min(a, b))
    upper = min(8, max(a, b))

    return [i for i in range(lower, upper+1) if i % 2 == 0]

import pytest

@pytest.mark.parametrize("a, b, expected", [
    (2, 6, [2, 4, 6]),
    (1, 9, [2, 4, 6, 8]),
    (3, 7, [4, 6]),
    (0, 10, [2, 4, 6, 8]),
    (-2, 4, [2, 4]),
    (8, 2, [2, 4, 6, 8]),
    (1, 1, []),
    (0, 0, []),
    (2.5, 6.5, [2, 4, 6]),
    (10, 2, [2, 4, 6, 8]),
])
def test_generate_integers(a, b, expected):
    from pytest import raises
    if isinstance(expected, type) and issubclass(expected, Exception):
        with raises(expected):
            generate_integers(a, b)
    else:
        assert generate_integers(a, b) == expected

def test_generate_integers_single_even_number():
    assert generate_integers(4, 4) == [4]

def test_generate_integers_single_odd_number():
    assert generate_integers(3, 3) == []

def test_generate_integers_negative_numbers():
    assert generate_integers(-4, -2) == [-4, -2]

def test_generate_integers_zero():
    assert generate_integers(0, 0) == []