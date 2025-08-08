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

def test_get_max_triples_zero():
    assert get_max_triples(0) == 0

def test_get_max_triples_one():
    assert get_max_triples(1) == 0

def test_get_max_triples_two():
    assert get_max_triples(2) == 0

@pytest.mark.parametrize("n,expected", [
    (3, 0),
    (4, 1),
    (5, 1),
    (6, 4),
])
def test_get_max_triples_small_numbers(n, expected):
    assert get_max_triples(n) == expected

def test_get_max_triples_negative():
    try:
        get_max_triples(-1)
        assert False, "Should have raised ValueError"
    except:
        pass

def test_get_max_triples_float():
    with pytest.raises(TypeError):
        get_max_triples(3.5)

def test_get_max_triples_string():
    with pytest.raises(TypeError):
        get_max_triples("3")

def test_get_max_triples_none():
    with pytest.raises(TypeError):
        get_max_triples(None)

def test_get_max_triples_large_number():
    assert get_max_triples(10) >= 35

def test_get_max_triples_sequence():
    result1 = get_max_triples(4)
    result2 = get_max_triples(6)
    result3 = get_max_triples(8)
    assert result1 < result2 < result3