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
    return sum([lst[i] for i in range(1, len(lst), 2) if lst[i]%2 == 0])

def test_add_example():
    assert add([4, 2, 6, 7]) == 2

def test_add_single_element():
    assert add([5]) == 0

def test_add_two_elements_even_at_odd_index():
    assert add([1, 4]) == 4

def test_add_two_elements_odd_at_odd_index():
    assert add([1, 3]) == 0

def test_add_no_odd_indices():
    assert add([2]) == 0

def test_add_multiple_even_at_odd_indices():
    assert add([1, 2, 3, 4, 5, 6]) == 10

def test_add_multiple_odd_at_odd_indices():
    assert add([1, 3, 2, 5, 4, 7]) == 0

def test_add_mixed_values():
    assert add([0, 8, 1, 2, 3, 4, 5, 6]) == 12

def test_add_all_even_numbers():
    assert add([2, 4, 6, 8, 10, 12]) == 24

def test_add_all_odd_numbers():
    assert add([1, 3, 5, 7, 9, 11]) == 0

def test_add_negative_numbers():
    assert add([1, -2, 3, -4, 5, -6]) == -12

def test_add_zero_at_odd_index():
    assert add([1, 0, 3, 0, 5]) == 0

def test_add_large_list():
    lst = list(range(100))
    expected = sum([lst[i] for i in range(1, len(lst), 2) if lst[i] % 2 == 0])
    assert add(lst) == expected

@pytest.mark.parametrize("input_list,expected", [
    ([1, 2], 2),
    ([1, 3], 0),
    ([5, 4, 3, 2, 1], 6),
    ([10, 20, 30, 40], 60),
    ([1, 1, 1, 1, 1], 0),
    ([2, 2, 2, 2, 2], 4),
    ([-1, -2, -3, -4], -6)
])
def test_add_parametrized(input_list, expected):
    assert add(input_list) == expected