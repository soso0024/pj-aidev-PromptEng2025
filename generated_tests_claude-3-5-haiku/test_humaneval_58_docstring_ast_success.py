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

def test_common_normal_case():
    assert common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]) == [1, 5, 653]

def test_common_subset():
    assert common([5, 3, 2, 8], [3, 2]) == [2, 3]

def test_common_no_overlap():
    assert common([1, 2, 3], [4, 5, 6]) == []

def test_common_empty_lists():
    assert common([], []) == []

def test_common_one_empty_list():
    assert common([1, 2, 3], []) == []

@pytest.mark.parametrize("list1,list2,expected", [
    ([1, 1, 1], [1, 1, 1], [1]),
    ([1, 2, 3], [3, 2, 1], [1, 2, 3]),
    ([-1, -2, -3], [-3, -2, -1], [-3, -2, -1])
])
def test_common_parametrized(list1, list2, expected):
    assert common(list1, list2) == expected

def test_common_different_types():
    assert common([1, 2], [1, 2]) == [1, 2]