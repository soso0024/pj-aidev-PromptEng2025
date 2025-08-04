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

def test_all_below():
    assert below_threshold([1, 2, 3], 4) == True

def test_all_above():
    assert below_threshold([5, 6, 7], 4) == False

def test_mixed_values():
    assert below_threshold([1, 4, 7], 5) == False

def test_equal_to_threshold():
    assert below_threshold([1, 2, 3, 3], 3) == False

def test_single_element_below():
    assert below_threshold([1], 2) == True

def test_single_element_above():
    assert below_threshold([3], 2) == False

@pytest.mark.parametrize("input_list,threshold,expected", [
    ([], 0, True),
    ([1, 2, 3], 4, True),
    ([4, 5, 6], 4, False),
    ([1], 1, False),
    ([0, -1, -2], 1, True),
    ([1.5, 2.5, 3.5], 4, True),
    ([-1, 0, 1, 2], 3, True),
    ([10, 20, 30], 5, False)
])
def test_below_threshold_parametrized(input_list, threshold, expected):
    assert below_threshold(input_list, threshold) == expected

@pytest.mark.parametrize("invalid_input", [
    None,
    "string",
    42,
    3.14
])
def test_invalid_list_type(invalid_input):
    with pytest.raises(TypeError):
        below_threshold(invalid_input, 5)

def test_invalid_threshold_type():
    with pytest.raises(TypeError):
        below_threshold([1, 2, 3], "5")

def test_none_threshold():
    with pytest.raises(TypeError):
        below_threshold([1, 2, 3], None)

def test_list_with_none():
    with pytest.raises(TypeError):
        below_threshold([1, None, 3], 5)

def test_list_with_strings():
    with pytest.raises(TypeError):
        below_threshold([1, "2", 3], 5)
