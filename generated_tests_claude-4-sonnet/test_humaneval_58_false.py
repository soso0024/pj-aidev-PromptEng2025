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

def common(l1: list, l2: list):
    ret = set()
    for e1 in l1:
        for e2 in l2:
            if e1 == e2:
                ret.add(e1)
    return sorted(list(ret))

def test_common_empty_lists():
    assert common([], []) == []

def test_common_first_list_empty():
    assert common([], [1, 2, 3]) == []

def test_common_second_list_empty():
    assert common([1, 2, 3], []) == []

def test_common_no_common_elements():
    assert common([1, 2, 3], [4, 5, 6]) == []

def test_common_all_elements_common():
    assert common([1, 2, 3], [1, 2, 3]) == [1, 2, 3]

def test_common_some_elements_common():
    assert common([1, 2, 3, 4], [3, 4, 5, 6]) == [3, 4]

def test_common_duplicates_in_first_list():
    assert common([1, 1, 2, 2, 3], [2, 3, 4]) == [2, 3]

def test_common_duplicates_in_second_list():
    assert common([1, 2, 3], [2, 2, 3, 3, 4]) == [2, 3]

def test_common_duplicates_in_both_lists():
    assert common([1, 1, 2, 2], [2, 2, 3, 3]) == [2]

def test_common_single_element_lists():
    assert common([1], [1]) == [1]

def test_common_single_element_no_match():
    assert common([1], [2]) == []

def test_common_strings():
    assert common(['a', 'b', 'c'], ['b', 'c', 'd']) == ['b', 'c']

def test_common_mixed_types():
    result = common([1, 'a', 2.5], ['a', 2.5, 'b'])
    assert set(result) == {'a', 2.5}
    assert len(result) == 2

def test_common_with_none():
    assert common([1, None, 3], [None, 2, 4]) == [None]

def test_common_with_boolean():
    assert common([True, False, 1], [False, 0, 2]) == [False]

def test_common_tuples():
    assert common([(1, 2), (3, 4)], [(3, 4), (5, 6)]) == [(3, 4)]

def test_common_large_lists():
    l1 = list(range(1000))
    l2 = list(range(500, 1500))
    expected = list(range(500, 1000))
    assert common(l1, l2) == expected

def test_common_unsorted_result_gets_sorted():
    assert common([3, 1, 2], [2, 3, 1]) == [1, 2, 3]

@pytest.mark.parametrize("l1,l2,expected", [
    ([1, 2], [2, 3], [2]),
    (['x', 'y'], ['y', 'z'], ['y']),
    ([1.1, 2.2], [2.2, 3.3], [2.2]),
    ([0], [0, 1], [0])
])
def test_common_parametrized(l1, l2, expected):
    assert common(l1, l2) == expected