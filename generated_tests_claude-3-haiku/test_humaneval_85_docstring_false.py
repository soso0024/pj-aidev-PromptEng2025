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

def test_add_empty_list():
    assert add([]) == 0

def test_add_single_element_list():
    assert add([4]) == 0

def test_add_even_elements_at_odd_indices():
    assert add([4, 2, 6, 7]) == 8

def test_add_no_even_elements_at_odd_indices():
    assert add([1, 3, 5, 7]) == 0

def test_add_list_with_negative_numbers():
    assert add([-2, 4, -6, 8]) == 4

@pytest.mark.parametrize("input,expected", [
    ([4, 2, 6, 7, 8, 9, 10], 16),
    ([1, 2, 3, 4, 5, 6, 7, 8], 12),
    ([10, 20, 30, 40, 50], 20),
    ([-10, -20, -30, -40, -50], -50)
])
def test_add_various_inputs(input, expected):
    assert add(input) == expected

def test_add_single_element_list_with_even_number():
    assert add([4]) == 0

def test_add_single_element_list_with_odd_number():
    assert add([3]) == 0

def test_add_list_with_only_one_even_element_at_odd_index():
    assert add([1, 2, 3, 4, 5]) == 2