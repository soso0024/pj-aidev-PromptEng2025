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

def test_generate_integers_normal_ascending():
    assert generate_integers(2, 8) == [2, 4, 6, 8]

def test_generate_integers_normal_descending():
    assert generate_integers(8, 2) == [2, 4, 6, 8]

def test_generate_integers_no_even_numbers():
    assert generate_integers(10, 14) == []

def test_generate_integers_single_even_number():
    assert generate_integers(4, 4) == [4]

def test_generate_integers_lower_bound():
    assert generate_integers(1, 3) == [2]

def test_generate_integers_upper_bound():
    assert generate_integers(7, 9) == [8]

def test_generate_integers_outside_range():
    assert generate_integers(1, 1) == []

@pytest.mark.parametrize("a,b,expected", [
    (2, 8, [2, 4, 6, 8]),
    (8, 2, [2, 4, 6, 8]),
    (10, 14, []),
    (4, 4, [4]),
    (1, 3, [2]),
    (7, 9, [8]),
    (1, 1, [])
])
def test_generate_integers_parametrized(a, b, expected):
    assert generate_integers(a, b) == expected
