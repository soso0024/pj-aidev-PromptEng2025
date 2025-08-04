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
    assert common([1, 2, 3], [3, 4, 5]) == [3]

def test_common_multiple():
    assert common([1, 2, 3, 4], [3, 4, 5, 6]) == [3, 4]

def test_common_empty_lists():
    assert common([], []) == []

def test_common_one_empty_list():
    assert common([1, 2, 3], []) == []
    assert common([], [1, 2, 3]) == []

def test_common_duplicates():
    assert common([1, 1, 2, 2], [2, 2, 3, 3]) == [2]

def test_common_all_same():
    assert common([1, 1, 1], [1, 1, 1]) == [1]

def test_common_no_intersection():
    assert common([1, 2, 3], [4, 5, 6]) == []

def test_common_mixed_types():
    result = common(["a", 2.5], ["a", 2.5])
    assert result == [2.5, "a"]

@pytest.mark.parametrize("l1,l2,expected", [
    ([1, 2, 3], [3, 2, 1], [1, 2, 3]),
    (["test"], ["test"], ["test"]),
    ([True, False], [True, False], [False, True]),
    (["a", "b", "c"], ["d", "e", "f"], []),
    ([1, 1, 1, 2, 2, 3], [1, 2, 2, 4], [1, 2])
])
def test_common_parametrized(l1, l2, expected):
    result = common(l1, l2)
    assert sorted(result) == sorted(expected)

def test_common_with_none():
    with pytest.raises(TypeError):
        common([None, 1, 2], [None, 2, 3])

@pytest.mark.parametrize("invalid_input", [
    ([1, 2, 3], None),
    (None, [1, 2, 3]),
    (None, None)
])
def test_common_with_invalid_input(invalid_input):
    with pytest.raises(TypeError):
        common(*invalid_input)

def test_common_large_lists():
    l1 = list(range(1000))
    l2 = list(range(500, 1500))
    expected = list(range(500, 1000))
    assert common(l1, l2) == expected