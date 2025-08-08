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
from pytest import raises

@pytest.mark.parametrize("a, b, expected", [
    (2, 4, [2, 4]),
    (1, 7, [2, 4, 6]),
    (3, 9, [4, 6, 8]),
    (0, 0, []),
    (-2, 2, []),
    (8, 2, [2, 4, 6, 8]),
    (1, 3, [2]),
    ('a', 'b', TypeError),
    (None, None, TypeError)
])
def test_generate_integers(a, b, expected):
    if isinstance(expected, type) and issubclass(expected, Exception):
        with raises(expected):
            generate_integers(a, b)
    else:
        assert generate_integers(a, b) == expected