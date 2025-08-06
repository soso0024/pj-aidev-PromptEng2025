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
    assert add([1, 4, 3, 6, 5, 8]) == 18

def test_add_empty():
    with pytest.raises(ValueError):
        add([])

def test_add_single():
    with pytest.raises(ValueError):
        add([1])

def test_add_no_even():
    assert add([1, 3, 5, 7]) == 0

def test_add_all_even():
    assert add([2, 4, 6, 8]) == 4

@pytest.mark.parametrize("input_list,expected", [
    ([4, 2, 6, 7], 2),
    ([1, 4, 3, 6, 5, 8], 18),
    ([1, 3, 5, 7], 0),
    ([2, 4, 6, 8], 4),
    ([0, 2, 0, 4], 2),
    ([1, 10, 3, 20, 5, 30], 60),
    ([2, 2, 4, 4, 6, 6], 12),
    ([1, -2, 3, -4], -2)
])
def test_add_parametrized(input_list, expected):
    assert add(input_list) == expected

def test_add_negative():
    assert add([1, -2, 3, -4]) == -2

def test_add_zeros():
    assert add([0, 2, 0, 4]) == 2

@pytest.mark.parametrize("invalid_input", [
    None,
    "string",
    123,
    [1, "2", 3, 4],
    [1, None, 3, 4],
    [[], 2, 3, 4]
])
def test_add_invalid_input(invalid_input):
    with pytest.raises(TypeError):
        add(invalid_input)