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
    assert generate_integers(2, 8) == [2, 4, 6, 8]
    assert generate_integers(8, 2) == [2, 4, 6, 8]

def test_generate_integers_empty_range():
    assert generate_integers(10, 14) == []

@pytest.mark.parametrize("a,b,expected", [
    (0, 8, [2, 4, 6, 8]),
    (2, 0, [2]),
    (-2, 8, [2, 4, 6, 8]),
    (2, -8, [2])
])
def test_generate_integers_edge_cases(a, b, expected):
    assert generate_integers(a, b) == expected

def test_generate_integers_invalid_input():
    with pytest.raises(TypeError):
        generate_integers('a', 8)
    with pytest.raises(TypeError):
        generate_integers(2, 'b')
