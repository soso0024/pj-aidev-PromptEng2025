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

def test_common_basic_case():
    assert common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]) == [1, 5, 653]

def test_common_subset():
    assert common([5, 3, 2, 8], [3, 2]) == [2, 3]

def test_common_empty_lists():
    assert common([], []) == []

def test_common_first_empty():
    assert common([], [1, 2, 3]) == []

def test_common_second_empty():
    assert common([1, 2, 3], []) == []

def test_common_no_common_elements():
    assert common([1, 2, 3], [4, 5, 6]) == []

def test_common_identical_lists():
    assert common([1, 2, 3], [1, 2, 3]) == [1, 2, 3]

def test_common_duplicates_in_both():
    assert common([1, 1, 2, 2, 3], [2, 2, 3, 3, 4]) == [2, 3]

def test_common_single_elements():
    assert common([5], [5]) == [5]

def test_common_single_no_match():
    assert common([5], [6]) == []

def test_common_mixed_types():
    result = common([1, 'a', 3.5], ['a', 2, 3.5])
    assert set(result) == {3.5, 'a'}
    assert len(result) == 2

def test_common_strings():
    assert common(['apple', 'banana', 'cherry'], ['banana', 'date', 'apple']) == ['apple', 'banana']

def test_common_negative_numbers():
    assert common([-1, -2, 3], [-2, 4, -1]) == [-2, -1]

def test_common_floats():
    assert common([1.1, 2.2, 3.3], [2.2, 4.4, 1.1]) == [1.1, 2.2]

def test_common_boolean_values():
    assert common([True, False], [False, True]) == [False, True]

def test_common_none_values():
    result = common([None, 1, 2], [2, None, 3])
    assert set(result) == {2, None}
    assert len(result) == 2

@pytest.mark.parametrize("l1,l2,expected", [
    ([1, 2, 3], [3, 4, 5], [3]),
    ([10, 20, 30], [30, 20, 10], [10, 20, 30]),
    ([1], [2], []),
    ([0], [0], [0]),
    ([1, 1, 1], [1], [1])
])
def test_common_parametrized(l1, l2, expected):
    assert common(l1, l2) == expected