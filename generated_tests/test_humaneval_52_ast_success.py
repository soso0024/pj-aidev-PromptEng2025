# Test cases for HumanEval/52
# Generated using Claude API



def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    """

    for e in l:
        if e >= t:
            return False
    return True


# Generated test cases:
import pytest

def test_empty_list():
    assert below_threshold([], 5) == True

def test_single_element_below():
    assert below_threshold([1], 5) == True

def test_single_element_equal():
    assert below_threshold([5], 5) == False

def test_single_element_above():
    assert below_threshold([6], 5) == False

def test_multiple_elements_all_below():
    assert below_threshold([1, 2, 3, 4], 5) == True

def test_multiple_elements_one_equal():
    assert below_threshold([1, 2, 5, 4], 5) == False

def test_multiple_elements_one_above():
    assert below_threshold([1, 2, 6, 4], 5) == False

def test_negative_numbers():
    assert below_threshold([-3, -2, -1], 0) == True

def test_negative_threshold():
    assert below_threshold([-3, -2, -1], -2) == False

@pytest.mark.parametrize("input_list,threshold,expected", [
    ([], 0, True),
    ([1], 1, False),
    ([0, 0, 0], 1, True),
    ([-1, -2, -3], -2, False),
    ([1, 2, 3, 4, 5], 6, True),
    ([1, 2, 3, 4, 6], 5, False),
])
def test_parametrized_cases(input_list, threshold, expected):
    assert below_threshold(input_list, threshold) == expected

@pytest.mark.parametrize("invalid_list", [
    None,
    "string",
    123,
    True
])
def test_invalid_input_type(invalid_list):
    with pytest.raises(TypeError):
        below_threshold(invalid_list, 5)

def test_invalid_threshold_type():
    with pytest.raises(TypeError):
        below_threshold([1, 2, 3], "5")
