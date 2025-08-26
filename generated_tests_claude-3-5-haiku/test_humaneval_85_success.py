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
    assert add([1, 2, 3, 4, 5, 6]) == 12

def test_add_empty_list():
    assert add([]) == 0

def test_add_no_even_indices():
    assert add([1, 3, 5, 7]) == 0

def test_add_all_even_indices():
    assert add([1, 2, 3, 4, 5, 6, 7, 8]) == 20

def test_add_negative_numbers():
    assert add([1, -2, 3, -4, 5, -6]) == -12

def test_add_zero_values():
    assert add([1, 0, 3, 0, 5, 6]) == 6

@pytest.mark.parametrize("input_list,expected", [
    ([1, 2, 3, 4, 5, 6], 12),
    ([], 0),
    ([1, 3, 5, 7], 0),
    ([1, 2, 3, 4, 5, 6, 7, 8], 20),
    ([1, -2, 3, -4, 5, -6], -12),
    ([1, 0, 3, 0, 5, 6], 6)
])
def test_add_parametrized(input_list, expected):
    assert add(input_list) == expected

def test_add_single_element():
    assert add([1]) == 0

def test_add_two_elements():
    assert add([1, 2]) == 2