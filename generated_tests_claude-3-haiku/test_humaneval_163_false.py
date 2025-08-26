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

def test_generate_integers_normal_case():
    assert generate_integers(3, 7) == [4, 6]

def test_generate_integers_equal_inputs():
    assert generate_integers(5, 5) == [6]

def test_generate_integers_negative_inputs():
    assert generate_integers(-3, -1) == []

def test_generate_integers_out_of_range_inputs():
    assert generate_integers(1, 9) == [2, 4, 6, 8]

@pytest.mark.parametrize("a,b,expected", [
    (3, 7, [4, 6]),
    (5, 5, [6]),
    (-3, -1, []),
    (1, 9, [2, 4, 6, 8]),
    (0, 0, []),
    (8, 2, [2, 4, 6, 8]),
    (-5, 5, [2, 4, 6])
])
def test_generate_integers_parametrized(a, b, expected):
    assert generate_integers(a, b) == expected

def test_generate_integers_invalid_inputs():
    with pytest.raises(TypeError):
        generate_integers('a', 'b')