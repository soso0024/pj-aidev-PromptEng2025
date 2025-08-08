# Test cases for HumanEval/85
# Generated using Claude API


def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """

    return sum([lst[i] for i in range(1, len(lst), 2) if lst[i]%2 == 0])


# Generated test cases:
import pytest

def test_basic_list():
    assert add([4, 2, 6, 7]) == 2

def test_no_even_numbers_at_odd_indices():
    assert add([1, 3, 5, 7]) == 0

def test_all_even_numbers_at_odd_indices():
    assert add([1, 2, 3, 4, 5, 6]) == 6

def test_single_even_at_odd_index():
    assert add([1, 8, 3, 5]) == 8

@pytest.mark.parametrize("input_list,expected", [
    ([1, 2, 3, 4, 5, 6], 6),
    ([4, 2, 6, 7], 2),
    ([1, 3, 5, 7], 0),
    ([2, 4, 6, 8], 12),
    ([1, 2], 2),
    ([1, 2, 3, 4, 5, 6, 7, 8], 14),
])
def test_various_lists(input_list, expected):
    assert add(input_list) == expected

def test_list_with_negative_numbers():
    assert add([1, -2, 3, -4]) == -6

def test_minimal_list():
    assert add([1, 2]) == 2

@pytest.mark.parametrize("invalid_input", [
    None,
    "string",
    123,
])
def test_invalid_inputs(invalid_input):
    with pytest.raises((TypeError, AttributeError)):
        add(invalid_input)

def test_empty_list():
    with pytest.raises(IndexError):
        add([])

def test_large_numbers():
    assert add([1000, 2000, 3000, 4000]) == 6000

def test_list_with_zeros():
    assert add([0, 0, 0, 0]) == 0

def test_large_list():
    large_list = list(range(1000))
    expected = sum([x for i, x in enumerate(large_list) if i % 2 == 1 and x % 2 == 0])
    assert add(large_list) == expected