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

def test_common_basic_case():
    assert common([1, 2, 3], [3, 4, 5]) == [3]

def test_common_empty_lists():
    assert common([], []) == []

def test_common_no_overlap():
    assert common([1, 2], [3, 4]) == []

def test_common_multiple_overlaps():
    assert common([1, 2, 2, 3], [2, 3, 3, 4]) == [2, 3]

def test_common_duplicate_elements():
    assert common([1, 1, 2, 2], [2, 2, 3, 3]) == [2]

def test_common_different_types():
    assert common([1, 'a'], ['a', 2]) == ['a']

def test_common_nested_lists():
    assert common([[1, 2], [3, 4]], [[3, 4], [5, 6]]) == [[3, 4]]

@pytest.mark.parametrize("l1,l2,expected", [
    ([1, 2, 3], [3, 4, 5], [3]),
    ([], [], []),
    ([1, 2], [3, 4], []),
    ([1, 1, 2, 2], [2, 2, 3, 3], [2]),
    ([1, 'a'], ['a', 2], ['a'])
])
def test_common_parametrized(l1, l2, expected):
    assert common(l1, l2) == expected

def test_common_nested_lists_hashable():
    assert common([(1, 2), (3, 4)], [(3, 4), (5, 6)]) == [(3, 4)]