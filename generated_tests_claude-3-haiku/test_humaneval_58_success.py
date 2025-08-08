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

def test_common_no_common_elements():
    assert common([1, 2, 3], [4, 5, 6]) == []

def test_common_some_common_elements():
    assert common([1, 2, 3, 4], [3, 4, 5, 6]) == [3, 4]
    assert common([1.0, 2.0, 3.0], [2.0, 3.0, 4.0]) == [2.0, 3.0]
    assert common(['a', 'b', 'c'], ['b', 'c', 'd']) == ['b', 'c']

def test_common_duplicate_elements():
    assert common([1, 1, 2, 2, 3], [2, 2, 3, 3]) == [2, 3]

def test_common_with_none():
    assert common([1, None, 3], [None, 2, None]) == [None]

@pytest.mark.parametrize("l1,l2,expected", [
    ([], [], []),
    ([1, 2, 3], [], []),
    ([], [1, 2, 3], []),
    ([1, 2, 3, 4], [3, 4, 5, 6], [3, 4]),
    ([1.0, 2.0, 3.0], [2.0, 3.0, 4.0], [2.0, 3.0]),
    (['a', 'b', 'c'], ['b', 'c', 'd'], ['b', 'c']),
    ([1, 1, 2, 2, 3], [2, 2, 3, 3], [2, 3]),
    ([1, None, 3], [None, 2, None], [None])
])
def test_common_parametrized(l1, l2, expected):
    assert common(l1, l2) == expected

def common(l1: list, l2: list):
    ret = set()
    for e1 in l1:
        for e2 in l2:
            if e1 == e2:
                ret.add(e1)
    return sorted(list(ret))
