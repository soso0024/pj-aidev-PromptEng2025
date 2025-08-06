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

def test_basic_ascending():
    assert generate_integers(2, 8) == [2, 4, 6, 8]

def test_basic_descending():
    assert generate_integers(8, 2) == [2, 4, 6, 8]

def test_no_even_numbers():
    assert generate_integers(10, 14) == []

def test_same_number():
    assert generate_integers(4, 4) == [4]

def test_outside_range():
    assert generate_integers(1, 1) == []
    assert generate_integers(9, 15) == []

@pytest.mark.parametrize("a, b, expected", [
    (2, 8, [2, 4, 6, 8]),
    (8, 2, [2, 4, 6, 8]),
    (3, 7, [4, 6]),
    (1, 9, [2, 4, 6, 8]),
    (5, 5, []),
    (2, 4, [2, 4]),
    (0, 10, [2, 4, 6, 8]),
    (10, 0, [2, 4, 6, 8]),
    (100, 200, []),
    (-5, 5, [2, 4])
])
def test_multiple_cases(a, b, expected):
    assert generate_integers(a, b) == expected

def test_edge_values():
    assert generate_integers(0, 0) == []
    assert generate_integers(-1, -1) == []
    assert generate_integers(1, 2) == [2]
    assert generate_integers(8, 9) == [8]

def test_large_numbers():
    assert generate_integers(1000, 2000) == []
    assert generate_integers(-1000, 1000) == [2, 4, 6, 8]

def test_boundary_conditions():
    assert generate_integers(2, 2) == [2]
    assert generate_integers(8, 8) == [8]
    assert generate_integers(7, 9) == [8]
