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
    assert add([1, 2, 3, 4, 5, 6]) == 12  # 2 + 4 + 6 = 12

def test_add_empty_list():
    assert add([]) == 0

def test_add_single_element():
    assert add([1]) == 0

def test_add_no_even_numbers():
    assert add([1, 3, 5, 7, 9, 11]) == 0

def test_add_all_even_numbers():
    assert add([1, 2, 3, 4, 5, 6]) == 12

def test_add_negative_numbers():
    assert add([1, -2, 3, -4, 5, -6]) == -12

def test_add_zeros():
    assert add([0, 0, 0, 0, 0, 0]) == 0

@pytest.mark.parametrize("input_list,expected", [
    ([1, 2, 3, 4, 5, 6], 12),
    ([], 0),
    ([1], 0),
    ([1, 3, 5, 7], 0),
    ([1, 2], 2),
    ([1, 2, 3, 4], 6),
    ([0, 2, 0, 4, 0, 6], 12),
    ([1, -2, 3, -4], -6),
])
def test_add_parametrized(input_list, expected):
    assert add(input_list) == expected

@pytest.mark.parametrize("invalid_input", [
    None,
    "string",
    123,
    [1, "2", 3],
    [1, None, 3],
    [1, [], 3]
])
def test_add_invalid_input(invalid_input):
    with pytest.raises((TypeError, AttributeError)):
        add(invalid_input)

def test_add_large_numbers():
    assert add([1, 1000000, 3, 2000000]) == 3000000

def test_add_floating_point():
    result = add([1.0, 2.0, 3.0, 4.0])
    assert result == 6.0