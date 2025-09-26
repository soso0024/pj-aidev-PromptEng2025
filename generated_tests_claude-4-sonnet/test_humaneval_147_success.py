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

def get_max_triples(n):
    A = [i*i - i + 1 for i in range(1,n+1)]
    ans = []
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if (A[i]+A[j]+A[k])%3 == 0:
                    ans += [(A[i],A[j],A[k])]
    return len(ans)

def test_get_max_triples_edge_cases():
    assert get_max_triples(1) == 0
    assert get_max_triples(2) == 0
    assert get_max_triples(0) == 0

def test_get_max_triples_small_values():
    assert get_max_triples(3) == 0
    assert get_max_triples(4) == 1
    assert get_max_triples(5) == 1

@pytest.mark.parametrize("n,expected", [
    (6, 4),
    (7, 10),
    (8, 11),
    (9, 21),
    (10, 36)
])
def test_get_max_triples_normal_cases(n, expected):
    assert get_max_triples(n) == expected

def test_get_max_triples_larger_values():
    result_15 = get_max_triples(15)
    assert isinstance(result_15, int)
    assert result_15 >= 0
    
    result_20 = get_max_triples(20)
    assert isinstance(result_20, int)
    assert result_20 >= 0

def test_get_max_triples_sequence_property():
    results = []
    for i in range(1, 11):
        results.append(get_max_triples(i))
    
    for i in range(1, len(results)):
        assert results[i] >= results[i-1]

def test_get_max_triples_return_type():
    assert isinstance(get_max_triples(5), int)
    assert isinstance(get_max_triples(10), int)
    assert isinstance(get_max_triples(1), int)

def test_get_max_triples_negative_input():
    assert get_max_triples(-1) == 0
    assert get_max_triples(-5) == 0