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

def test_basic_positive_numbers():
    assert get_positive([1, 2, 3]) == [1, 2, 3]

def test_mixed_numbers():
    assert get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]

def test_all_negative():
    assert get_positive([-1, -2, -3]) == []

def test_empty_list():
    assert get_positive([]) == []

def test_with_zero():
    assert get_positive([0, 1, -1]) == [1]

def test_large_numbers():
    assert get_positive([1000000, -1000000]) == [1000000]

def test_decimal_numbers():
    assert get_positive([0.5, -0.5, 1.5, -1.5]) == [0.5, 1.5]

@pytest.mark.parametrize("input_list,expected", [
    ([1, 2, 3], [1, 2, 3]),
    ([-1, -2, -3], []),
    ([0, 0, 0], []),
    ([1, -1, 2, -2], [1, 2]),
    ([0.1, -0.1, 1.1, -1.1], [0.1, 1.1])
])
def test_multiple_cases(input_list, expected):
    assert get_positive(input_list) == expected

def test_single_element():
    assert get_positive([1]) == [1]
    assert get_positive([-1]) == []

def test_repeated_numbers():
    assert get_positive([1, 1, 1, -1, -1]) == [1, 1, 1]

@pytest.mark.parametrize("invalid_input", [
    None,
    "string",
    123,
    True
])
def test_invalid_input_type(invalid_input):
    with pytest.raises(TypeError):
        get_positive(invalid_input)
