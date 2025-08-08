# Test cases for HumanEval/83
# Generated using Claude API


def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    if n == 1: return 1
    return 18 * (10 ** (n - 2))


# Generated test cases:
from your_module import starts_one_ends
import pytest

@pytest.mark.parametrize("n,expected", [
    (1, 1),
    (2, 18),
    (3, 180),
    (4, 1800),
    (0, pytest.raises(ValueError)),
    (-1, pytest.raises(ValueError)),
    ('a', pytest.raises(TypeError)),
    (1.5, pytest.raises(TypeError))
])
def test_starts_one_ends(n, expected):
    if isinstance(expected, type) and issubclass(expected, Exception):
        with expected:
            assert starts_one_ends(n) == expected.value
    else:
        assert starts_one_ends(n) == expected