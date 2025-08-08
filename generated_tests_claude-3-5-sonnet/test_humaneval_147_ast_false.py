# Test cases for HumanEval/147
# Generated using Claude API


def get_max_triples(n):
    """
    You are given a positive integer n. You have to create an integer array a of length n.
        For each i (1 ≤ i ≤ n), the value of a[i] = i * i - i + 1.
        Return the number of triples (a[i], a[j], a[k]) of a where i < j < k, 
    and a[i] + a[j] + a[k] is a multiple of 3.

    Example :
        Input: n = 5
        Output: 1
        Explanation: 
        a = [1, 3, 7, 13, 21]
        The only valid triple is (1, 7, 13).
    """

    A = [i*i - i + 1 for i in range(1,n+1)]
    ans = []
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if (A[i]+A[j]+A[k])%3 == 0:
                    ans += [(A[i],A[j],A[k])]
    return len(ans)


# Generated test cases:
import pytest

def test_get_max_triples_empty():
    assert get_max_triples(0) == 0
    assert get_max_triples(1) == 0

def test_get_max_triples_small():
    assert get_max_triples(2) == 0
    assert get_max_triples(3) == 0

@pytest.mark.parametrize("n,expected", [
    (4, 1),
    (5, 1),
    (6, 4),
])
def test_get_max_triples_medium(n, expected):
    assert get_max_triples(n) == expected

def test_get_max_triples_large():
    assert get_max_triples(10) == 36

@pytest.mark.parametrize("invalid_input", [
    -1,
    -100,
])
def test_get_max_triples_negative(invalid_input):
    try:
        get_max_triples(invalid_input)
        pytest.fail("Expected ValueError for negative input")
    except ValueError:
        pass

@pytest.mark.parametrize("invalid_type", [
    "string",
    None,
    3.14,
    [],
    {},
])
def test_get_max_triples_invalid_types(invalid_type):
    with pytest.raises((TypeError, ValueError)):
        get_max_triples(invalid_type)

def test_get_max_triples_boundary():
    assert get_max_triples(1) == 0
    assert get_max_triples(2) == 0
    assert get_max_triples(3) == 0

def test_get_max_triples_sequence():
    results = [get_max_triples(i) for i in range(1, 6)]
    assert results == [0, 0, 0, 1, 1]