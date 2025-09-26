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

def generate_integers(a, b):
    lower = max(2, min(a, b))
    upper = min(8, max(a, b))
    return [i for i in range(lower, upper+1) if i % 2 == 0]

@pytest.mark.parametrize("a,b,expected", [
    (2, 8, [2, 4, 6, 8]),
    (8, 2, [2, 4, 6, 8]),
    (10, 14, []),
    (1, 1, []),
    (1, 2, [2]),
    (2, 2, [2]),
    (3, 3, []),
    (4, 4, [4]),
    (5, 5, []),
    (6, 6, [6]),
    (7, 7, []),
    (8, 8, [8]),
    (9, 9, []),
    (1, 9, [2, 4, 6, 8]),
    (9, 1, [2, 4, 6, 8]),
    (0, 10, [2, 4, 6, 8]),
    (10, 0, [2, 4, 6, 8]),
    (3, 7, [4, 6]),
    (7, 3, [4, 6]),
    (1, 3, [2]),
    (3, 1, [2]),
    (5, 9, [6, 8]),
    (9, 5, [6, 8]),
    (1, 8, [2, 4, 6, 8]),
    (8, 1, [2, 4, 6, 8]),
    (2, 9, [2, 4, 6, 8]),
    (9, 2, [2, 4, 6, 8]),
    (0, 0, []),
    (100, 200, []),
    (-5, -1, []),
    (-10, 15, [2, 4, 6, 8]),
    (15, -10, [2, 4, 6, 8])
])
def test_generate_integers(a, b, expected):
    assert generate_integers(a, b) == expected

def test_generate_integers_basic_cases():
    assert generate_integers(2, 8) == [2, 4, 6, 8]
    assert generate_integers(8, 2) == [2, 4, 6, 8]
    assert generate_integers(10, 14) == []

def test_generate_integers_edge_cases():
    assert generate_integers(1, 1) == []
    assert generate_integers(9, 9) == []
    assert generate_integers(0, 0) == []

def test_generate_integers_boundary_values():
    assert generate_integers(2, 2) == [2]
    assert generate_integers(8, 8) == [8]
    assert generate_integers(1, 8) == [2, 4, 6, 8]
    assert generate_integers(2, 9) == [2, 4, 6, 8]

def test_generate_integers_reversed_order():
    assert generate_integers(8, 2) == [2, 4, 6, 8]
    assert generate_integers(7, 3) == [4, 6]
    assert generate_integers(9, 1) == [2, 4, 6, 8]

def test_generate_integers_large_numbers():
    assert generate_integers(100, 200) == []
    assert generate_integers(0, 100) == [2, 4, 6, 8]
    assert generate_integers(-100, 100) == [2, 4, 6, 8]

def test_generate_integers_negative_numbers():
    assert generate_integers(-5, -1) == []
    assert generate_integers(-10, 5) == [2, 4]
    assert generate_integers(-1, -5) == []