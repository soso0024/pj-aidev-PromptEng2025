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

def test_basic_below_threshold():
    assert below_threshold([1, 2, 3], 4) == True
    assert below_threshold([1, 2, 3], 3) == False

@pytest.mark.parametrize("input_list,threshold,expected", [
    ([1, 2, 4, 10], 100, True),
    ([1, 20, 4, 10], 5, False),
    ([], 5, True),
    ([0], 1, True),
    ([1], 1, False),
    ([-1, -2, -3], 0, True),
    ([5, 5, 5], 5, False),
    ([4, 4, 4], 5, True)
])
def test_below_threshold_parametrized(input_list, threshold, expected):
    assert below_threshold(input_list, threshold) == expected

def test_empty_list():
    assert below_threshold([], 0) == True
    assert below_threshold([], -1) == True
    assert below_threshold([], 1000) == True

def test_negative_numbers():
    assert below_threshold([-5, -4, -3], -2) == True
    assert below_threshold([-5, -4, -3], 0) == True

def test_single_element():
    assert below_threshold([1], 2) == True
    assert below_threshold([2], 2) == False
    assert below_threshold([3], 2) == False

@pytest.mark.parametrize("invalid_input", [
    None,
    "string",
    123,
    True,
    {'a': 1}
])
def test_invalid_list_type(invalid_input):
    with pytest.raises(TypeError):
        below_threshold(invalid_input, 5)

@pytest.mark.parametrize("invalid_threshold", [
    None,
    "string",
    [1, 2],
    {'a': 1},
    (1, 2)
])
def test_invalid_threshold_type(invalid_threshold):
    with pytest.raises(TypeError):
        below_threshold([1, 2, 3], invalid_threshold)

def test_list_with_invalid_elements():
    with pytest.raises(TypeError):
        below_threshold([1, "2", 3], 5)
    with pytest.raises(TypeError):
        below_threshold([1, None, 3], 5)
    with pytest.raises(TypeError):
        below_threshold([1, [2], 3], 5)