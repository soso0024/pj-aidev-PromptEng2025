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

def test_basic_range():
    assert generate_integers(2, 6) == [2, 4, 6]
    assert generate_integers(6, 2) == [2, 4, 6]

def test_range_with_odd_numbers():
    assert generate_integers(3, 7) == [4, 6]
    assert generate_integers(7, 3) == [4, 6]

def test_range_at_boundaries():
    assert generate_integers(1, 9) == [2, 4, 6, 8]
    assert generate_integers(9, 1) == [2, 4, 6, 8]

def test_range_outside_boundaries():
    assert generate_integers(0, 10) == [2, 4, 6, 8]
    assert generate_integers(-5, 15) == [2, 4, 6, 8]

def test_single_number():
    assert generate_integers(4, 4) == [4]
    assert generate_integers(3, 3) == []

def test_small_range():
    assert generate_integers(2, 3) == [2]
    assert generate_integers(3, 2) == [2]

@pytest.mark.parametrize("a, b, expected", [
    (2, 8, [2, 4, 6, 8]),
    (8, 2, [2, 4, 6, 8]),
    (1, 4, [2, 4]),
    (4, 1, [2, 4]),
    (5, 7, [6]),
    (7, 5, [6]),
    (1, 2, [2]),
    (2, 1, [2]),
])
def test_various_ranges(a, b, expected):
    assert generate_integers(a, b) == expected

def test_empty_ranges():
    assert generate_integers(3, 3) == []
    assert generate_integers(5, 5) == []
    assert generate_integers(7, 7) == []

def test_edge_cases():
    assert generate_integers(1, 1) == []
    assert generate_integers(9, 9) == []
    assert generate_integers(8, 8) == [8]
    assert generate_integers(2, 2) == [2]
