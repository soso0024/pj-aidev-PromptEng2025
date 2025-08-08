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
    assert add([1, 2, 3, 4, 5, 6]) == 2

def test_add_empty_list():
    with pytest.raises(IndexError):
        add([])

def test_add_no_even_indices():
    assert add([1, 3, 5, 7]) == 0

def test_add_all_even_indices():
    assert add([1, 2, 3, 4, 5, 6]) == 2

def test_add_negative_numbers():
    assert add([1, -2, 3, -4, 5, -6]) == -2

def test_add_single_element_list():
    assert add([1]) == 0

@pytest.mark.parametrize("input_list,expected", [
    ([1, 2, 3, 4, 5, 6], 2),
    ([1, 3, 5, 7], 0),
    ([1, -2, 3, -4, 5, -6], -2),
    ([1], 0)
])
def test_add_parametrized(input_list, expected):
    assert add(input_list) == expected

def test_add_large_list():
    large_list = list(range(1000))
    assert add(large_list) == sum(x for i, x in enumerate(large_list[1::2]) if x % 2 == 0)