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

def test_add_basic():
    assert add([4, 2, 6, 7]) == 2
    assert add([1, 2, 3, 4]) == 2
    assert add([1, 4, 3, 4, 5, 6]) == 4

def test_add_no_even_at_odd():
    assert add([1, 1, 3, 3, 5, 7]) == 0
    assert add([2, 3, 4, 5, 6, 7]) == 0

def test_add_all_even():
    assert add([2, 2, 2, 2, 2, 2]) == 6
    assert add([4, 4, 4, 4]) == 4

def test_add_minimal():
    assert add([1, 2]) == 2
    assert add([1, 3]) == 0

@pytest.mark.parametrize("input_lst,expected", [
    ([1, 2, 3, 4, 5, 6], 6),
    ([0, 2, 0, 4, 0, 6], 6),
    ([7, 8, 9, 10, 11, 12], 18),
    ([1, 0, 3, 0, 5, 0], 0),
])
def test_add_parametrized(input_lst, expected):
    assert add(input_lst) == expected

def test_add_large_numbers():
    assert add([100, 200, 300, 400, 500, 600]) == 600
    assert add([1000, 2000, 3000, 4000]) == 2000

def test_add_negative_numbers():
    assert add([-1, -2, -3, -4, -5, -6]) == -6
    assert add([-2, -4, -6, -8]) == -4

@pytest.mark.parametrize("input_lst", [
    [],
    None,
])
def test_add_invalid_input(input_lst):
    with pytest.raises((IndexError, TypeError)):
        add(input_lst)

def test_add_single_element():
    with pytest.raises(IndexError):
        add([1])