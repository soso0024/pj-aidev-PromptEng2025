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

def test_add_normal_case():
    assert add([4, 2, 6, 7]) == 2

def test_add_all_odd_indices_even():
    assert add([1, 2, 3, 4, 5, 6]) == 12

def test_add_no_even_numbers_at_odd_indices():
    assert add([1, 1, 3, 3, 5, 5]) == 0

def test_add_minimum_list_length():
    assert add([0, 2]) == 2

def test_add_single_element_list():
    assert add([1, 2]) == 2

@pytest.mark.parametrize("input_list,expected", [
    ([4, 2, 6, 7], 2),
    ([1, 2, 3, 4, 5, 6], 12),
    ([1, 1, 3, 3, 5, 5], 0),
    ([0, 2], 2),
    ([1, 2], 2)
])
def test_add_parametrized(input_list, expected):
    assert add(input_list) == expected

def test_add_empty_list_raises_error():
    with pytest.raises(IndexError):
        add([])

def test_add_none_input():
    with pytest.raises(TypeError):
        add(None)