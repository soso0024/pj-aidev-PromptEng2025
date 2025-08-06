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

def test_common_basic():
    assert common([1, 2, 3], [2, 3, 4]) == [2, 3]

def test_common_no_duplicates():
    assert common([1, 2, 3], [4, 5, 6]) == []

def test_common_empty_lists():
    assert common([], []) == []

def test_common_one_empty_list():
    assert common([1, 2, 3], []) == []
    assert common([], [1, 2, 3]) == []

def test_common_duplicate_elements():
    assert common([1, 1, 2, 2], [1, 2, 2]) == [1, 2]

def test_common_negative_numbers():
    assert common([-1, -2, 3], [-2, 3, 4]) == [-2, 3]

def test_common_float_numbers():
    assert common([1.5, 2.0, 3.7], [2.0, 3.7, 4.2]) == [2.0, 3.7]

@pytest.mark.parametrize("l1, l2, expected", [
    ([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121], [1, 5, 653]),
    ([5, 3, 2, 8], [3, 2], [2, 3]),
    ([1, 1, 1], [1, 1], [1]),
    ([10, 20, 30], [40, 50, 60], []),
    ([0], [0], [0]),
])
def test_common_parametrized(l1, l2, expected):
    assert common(l1, l2) == expected

def test_common_mixed_types():
    result = common([1, "2", 3], [1, 2, 3])
    assert result == [1, 3]

def test_common_none_elements():
    with pytest.raises(TypeError):
        common([1, None, 3], [1, 2, None])

def test_common_invalid_input_types():
    with pytest.raises(TypeError):
        common("not a list", [1, 2, 3])
    with pytest.raises(TypeError):
        common([1, 2, 3], "not a list")
    with pytest.raises(TypeError):
        common(None, [1, 2, 3])
    with pytest.raises(TypeError):
        common([1, 2, 3], None)