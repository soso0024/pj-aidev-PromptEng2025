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

    return [i for i in range(lower, upper+1) if i % 2 == 0 and i <= 8 and i >= 2]

def test_generate_integers_normal_range():
    assert generate_integers(2, 8) == [2, 4, 6, 8]
    assert generate_integers(3, 7) == [4, 6]

def test_generate_integers_reversed_range():
    assert generate_integers(8, 2) == [2, 4, 6, 8]
    assert generate_integers(7, 3) == [4, 6]

def test_generate_integers_lower_bound():
    assert generate_integers(1, 3) == [2]
    assert generate_integers(0, 4) == [2, 4]

def test_generate_integers_upper_bound():
    assert generate_integers(6, 10) == [6, 8]
    assert generate_integers(9, 12) == [10]

def test_generate_integers_same_value():
    assert generate_integers(4, 4) == [4]
    assert generate_integers(3, 3) == []

@pytest.mark.parametrize("a,b,expected", [
    (2, 8, [2, 4, 6, 8]),
    (3, 7, [4, 6]),
    (1, 3, [2]),
    (6, 10, [6, 8]),
    (9, 12, [10]),
    (4, 4, [4]),
    (3, 3, [])
])
def test_generate_integers_parametrized(a, b, expected):
    assert generate_integers(a, b) == expected