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
    assert add([1]) == 0
    assert add([2]) == 2

def test_add_even_elements():
    assert add([1, 2, 3, 4, 5, 6]) == 12
    assert add([2, 3, 4, 5, 6, 7]) == 10

def test_add_odd_elements():
    assert add([1, 3, 5, 7]) == 0

@pytest.mark.parametrize("input,expected", [
    ([1, 2, 3, 4, 5, 6, 7, 8], 20),
    ([2, 4, 6, 8, 10, 12], 30),
    ([1, 3, 5, 7, 9, 11], 0),
])
def test_add_with_parametrize(input, expected):
    assert add(input) == expected

def test_add_with_negative_numbers():
    assert add([-1, -2, -3, -4, -5, -6]) == -6

def test_add_with_non_numeric_elements():
    with pytest.raises(TypeError):
        add([1, 2, "3", 4, 5, 6])