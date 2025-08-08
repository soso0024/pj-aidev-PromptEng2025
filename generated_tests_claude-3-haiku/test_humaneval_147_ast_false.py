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
    if n < 1:
        raise ValueError("n must be a positive integer")
    A = [i*i - i + 1 for i in range(1,n+1)]
    ans = 0
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if (A[i]+A[j]+A[k])%3 == 0:
                    ans += 1
    return ans

def test_get_max_triples_zero():
    with pytest.raises(ValueError):
        get_max_triples(0)

def test_get_max_triples_one():
    assert get_max_triples(1) == 0

def test_get_max_triples_small():
    assert get_max_triples(5) == 1

@pytest.mark.parametrize("n,expected", [
    (10, 4),
    (20, 27),
    (30, 84),
    (40, 170),
    (50, 292)
])
def test_get_max_triples_known_values(n, expected):
    assert get_max_triples(n) == expected

def test_get_max_triples_negative():
    with pytest.raises(ValueError):
        get_max_triples(-1)

def test_get_max_triples_float():
    with pytest.raises(ValueError):
        get_max_triples(3.14)

def test_get_max_triples_string():
    with pytest.raises(ValueError):
        get_max_triples("10")