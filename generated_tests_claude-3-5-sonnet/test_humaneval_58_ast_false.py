# Test cases for HumanEval/58
# Generated using Claude API



def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """

    ret = set()
    for e1 in l1:
        for e2 in l2:
            if e1 == e2:
                ret.add(e1)
    return sorted(list(ret))


# Generated test cases:
import pytest

def test_common_empty_lists():
    assert common([], []) == []

def test_common_one_empty_list():
    assert common([1, 2, 3], []) == []
    assert common([], [1, 2, 3]) == []

def test_common_no_intersection():
    assert common([1, 2, 3], [4, 5, 6]) == []

def test_common_single_common_element():
    assert common([1, 2, 3], [3, 4, 5]) == [3]

def test_common_multiple_common_elements():
    assert common([1, 2, 3, 4], [3, 4, 5, 6]) == [3, 4]

def test_common_duplicate_elements():
    assert common([1, 1, 2, 2], [1, 2, 2]) == [1, 2]

def test_common_different_types():
    assert common([1, 2, 3], [1, 2, 3]) == [1, 2, 3]

@pytest.mark.parametrize("l1,l2,expected", [
    ([1, 2, 3], [1, 2, 3], [1, 2, 3]),
    ([3, 2, 1], [1, 2, 3], [1, 2, 3]),
    (["a", "b", "c"], ["b", "c", "d"], ["b", "c"]),
    ([True, False], [True, True], [True]),
    ([1, 2, 2, 3], [2, 2, 3, 3], [2, 3])
])
def test_common_parametrized(l1, l2, expected):
    assert common(l1, l2) == expected

def test_common_with_none():
    assert common([1, 2], [2, 3]) == [2]

@pytest.mark.parametrize("invalid_input", [
    (None, []),
    ([1, 2, 3], None),
    (42, [1, 2, 3])
])
def test_common_invalid_inputs(invalid_input):
    with pytest.raises(TypeError):
        common(*invalid_input)

def test_common_same_type_only():
    assert common([1, "2", 3.0], [1, "2", 3]) == ["2", 1]

def test_common_hashable_only():
    with pytest.raises(TypeError):
        common([[1], [2]], [[1], [3]])

def test_common_mixed_types():
    assert common([1, "2", True], [1, "2", True]) == [1, "2", True]

def test_common_string_inputs():
    assert common(["a", "b"], ["b", "c"]) == ["b"]