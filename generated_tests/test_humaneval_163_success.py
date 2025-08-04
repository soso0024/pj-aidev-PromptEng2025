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

def test_generate_integers_basic():
    assert generate_integers(2, 8) == [2, 4, 6, 8]
    assert generate_integers(8, 2) == [2, 4, 6, 8]

def test_generate_integers_small_range():
    assert generate_integers(2, 4) == [2, 4]
    assert generate_integers(4, 2) == [2, 4]

@pytest.mark.parametrize("a, b, expected", [
    (1, 5, [2, 4]),
    (5, 1, [2, 4]),
    (0, 3, [2]),
    (3, 0, [2]),
    (7, 9, [8]),
    (9, 7, [8]),
    (2, 2, [2]),
    (-1, 4, [2, 4]),
    (4, -1, [2, 4]),
    (10, 15, []),
    (15, 10, []),
    (-5, -1, []),
    (0, 0, []),
])
def test_generate_integers_edge_cases(a, b, expected):
    assert generate_integers(a, b) == expected

def test_generate_integers_bounds():
    assert generate_integers(1, 10) == [2, 4, 6, 8]
    assert generate_integers(10, 1) == [2, 4, 6, 8]
    assert generate_integers(-10, 20) == [2, 4, 6, 8]
    assert generate_integers(20, -10) == [2, 4, 6, 8]

def test_generate_integers_single_value():
    assert generate_integers(4, 4) == [4]
    assert generate_integers(3, 3) == []
    assert generate_integers(8, 8) == [8]

def test_generate_integers_no_evens():
    assert generate_integers(3, 3) == []
    assert generate_integers(5, 5) == []
    assert generate_integers(7, 7) == []
