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
    if n < 0:
        raise ValueError("n must be non-negative")
    A = [i*i - i + 1 for i in range(1,n+1)]
    ans = []
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if (A[i]+A[j]+A[k])%3 == 0:
                    ans.append((A[i],A[j],A[k]))
    return len(ans)

def test_get_max_triples_normal_case():
    assert get_max_triples(5) == 4

def test_get_max_triples_empty_input():
    assert get_max_triples(0) == 0

def test_get_max_triples_single_element():
    assert get_max_triples(1) == 0

@pytest.mark.parametrize("n,expected", [
    (10, 29),
    (15, 79),
    (20, 154),
    (25, 259),
])
def test_get_max_triples_various_inputs(n, expected):
    assert get_max_triples(n) == expected

def test_get_max_triples_negative_input():
    with pytest.raises(ValueError):
        get_max_triples(-5)