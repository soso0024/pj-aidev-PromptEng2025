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
    assert common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]) == [1, 5, 653]
    assert common([5, 3, 2, 8], [3, 2]) == [2, 3]

@pytest.mark.parametrize("l1,l2,expected", [
    ([], [], []),
    ([1], [], []),
    ([], [1], []),
    ([1], [1], [1]),
    ([1, 1, 1], [1, 1], [1]),
    ([1, 2, 3], [4, 5, 6], []),
    ([1, 2, 3, 2], [2, 3, 2, 4], [2, 3]),
    ([-1, 0, 1], [-2, -1, 0], [-1, 0]),
    ([1.5, 2.5], [2.5, 3.5], [2.5]),
    (['a', 'b', 'c'], ['b', 'c', 'd'], ['b', 'c']),
])
def test_common_parametrized(l1, l2, expected):
    assert common(l1, l2) == expected

def test_common_with_duplicates():
    assert common([1, 1, 2, 2], [2, 2, 3, 3]) == [2]

def test_common_with_mixed_types():
    assert common([1, "2"], [1, "2"]) == ["2", 1]

def test_common_large_lists():
    l1 = list(range(1000))
    l2 = list(range(500, 1500))
    assert common(l1, l2) == list(range(500, 1000))

@pytest.mark.parametrize("invalid_input", [
    ([1, 2, 3], None),
    (None, [1, 2, 3]),
    (None, None),
    (123, [1, 2, 3]),
    ([1, 2, 3], 123)
])
def test_common_invalid_inputs(invalid_input):
    with pytest.raises((TypeError, AttributeError)):
        common(*invalid_input)

def test_common_with_tuples():
    assert common([(1,), (2,)], [(1,), (3,)]) == [(1,)]

def test_common_with_empty_tuples():
    assert common([()], [()]) == [()]