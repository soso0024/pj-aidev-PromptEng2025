# Test cases for HumanEval/30
# Generated using Claude API



def get_positive(l: list):
    """Return only positive numbers in the list.
    >>> get_positive([-1, 2, -4, 5, 6])
    [2, 5, 6]
    >>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [5, 3, 2, 3, 9, 123, 1]
    """

    return [e for e in l if e > 0]


# Generated test cases:
import pytest

def test_get_positive_empty_list():
    assert get_positive([]) == []

def test_get_positive_all_positive():
    assert get_positive([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_get_positive_all_negative():
    assert get_positive([-1, -2, -3, -4, -5]) == []

def test_get_positive_mixed():
    assert get_positive([-1, 2, -3, 4, -5]) == [2, 4]

@pytest.mark.parametrize("input,expected", [
    ([0, 0, 0], []),
    ([1, 0, -1], [1]),
    ([-10, 0, 10], [10]),
    ([1.5, -2.3, 3.7], [1.5, 3.7]),
    ([1, 2, 3], [1, 2, 3])
])
def test_get_positive_parametrized(input, expected):
    assert get_positive(input) == expected

def test_get_positive_none_input():
    with pytest.raises(TypeError):
        get_positive(None)

def get_positive(l: list):
    return [e for e in l if isinstance(e, (int, float)) and e > 0]