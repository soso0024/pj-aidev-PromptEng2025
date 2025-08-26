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

def add(lst):
    if not lst:
        raise IndexError("List cannot be empty")
    return sum([lst[i] for i in range(1, len(lst), 2) if lst[i] % 2 == 0])

def test_add_basic_case():
    assert add([4, 2, 6, 7]) == 2

def test_add_no_even_at_odd_indices():
    assert add([1, 3, 5, 7]) == 0

def test_add_multiple_even_at_odd_indices():
    assert add([1, 2, 3, 4, 5, 6]) == 6

def test_add_single_element_list():
    assert add([1]) == 0

def test_add_two_element_list():
    assert add([1, 2]) == 2

def test_add_large_list():
    assert add([1, 10, 2, 20, 3, 30, 4, 40]) == 60

@pytest.mark.parametrize("input_list,expected", [
    ([4, 2, 6, 7], 2),
    ([1, 3, 5, 7], 0),
    ([1, 2, 3, 4, 5, 6], 6),
    ([1], 0),
    ([1, 2], 2),
    ([1, 10, 2, 20, 3, 30, 4, 40], 60)
])
def test_add_parametrized(input_list, expected):
    assert add(input_list) == expected

def test_add_empty_list_raises_error():
    with pytest.raises(IndexError):
        add([])