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
    assert add([4, 2, 6, 7]) == 2

def test_add_all_even_elements_at_odd_indices():
    assert add([2, 4, 6, 8]) == 10

def test_add_no_even_elements_at_odd_indices():
    assert add([1, 3, 5, 7]) == 0

@pytest.mark.parametrize("input,expected", [
    ([4, 2, 6, 8, 10], 12),
    ([1, 2, 3, 4, 5, 6], 10),
    ([-2, 4, -6, 8], 2),
    ([100, 200, 300, 400], 600)
])
def test_add_various_inputs(input, expected):
    assert add(input) == expected

def test_add_with_non_integer_elements():
    with pytest.raises(TypeError):
        add([1, 2.0, 3, 'a'])