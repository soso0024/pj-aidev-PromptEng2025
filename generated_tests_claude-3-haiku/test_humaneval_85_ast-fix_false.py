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
    """Given a non-empty list of integers lst. add the even elements that are at odd indices."""
    return sum(lst[i] for i in range(1, len(lst), 2) if lst[i] % 2 == 0)

def test_add_empty_list():
    assert add([]) == 0

def test_add_single_element_list():
    assert add([1]) == 0
    assert add([2]) == 2

def test_add_even_numbers():
    assert add([1, 2, 3, 4, 5, 6]) == 12

def test_add_odd_numbers():
    assert add([1, 3, 5, 7]) == 0

@pytest.mark.parametrize("input,expected", [
    ([1, 2, 3, 4, 5, 6, 7, 8], 12),
    ([2, 4, 6, 8, 10], 30),
    ([-1, 2, -3, 4, -5, 6], 6),
    ([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], 12.0),
    ([1, 2, 3, 4, 5, 6], 12)
])
def test_add_various_inputs(input, expected):
    assert add(input) == expected

def test_add_non_numeric_input():
    with pytest.raises(TypeError):
        add([1, 2, 'a', 4])