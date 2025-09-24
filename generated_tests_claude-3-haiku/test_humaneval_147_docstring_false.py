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

@pytest.mark.parametrize("n,expected", [
    (5, 1),
    (10, 8),
    (1, 0),
    (0, 0),
    (-5, ValueError),
    (3, 1)
])
def test_get_max_triples(n, expected):
    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            get_max_triples(n)
    else:
        assert get_max_triples(n) == expected

def get_max_triples(n):
    if not isinstance(n, int) or n < 1:
        raise ValueError("n must be a positive integer")
    A = [i*i - i + 1 for i in range(1,n+1)]
    ans = []
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if (A[i]+A[j]+A[k])%3 == 0:
                    ans.append((A[i],A[j],A[k]))
    return len(ans)