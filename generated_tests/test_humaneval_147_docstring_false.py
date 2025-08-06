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

def test_get_max_triples_basic():
    assert get_max_triples(5) == 1

def test_get_max_triples_minimum():
    assert get_max_triples(3) == 0

def test_get_max_triples_large():
    assert get_max_triples(6) == 4

@pytest.mark.parametrize("n,expected", [
    (4, 1),
    (7, 10),
    (8, 11),
    (3, 0),
    (5, 1),
    (6, 4)
])
def test_get_max_triples_parametrized(n, expected):
    assert get_max_triples(n) == expected

def test_get_max_triples_sequence_check():
    n = 5
    result = [i*i - i + 1 for i in range(1,n+1)]
    assert result == [1, 3, 7, 13, 21]

@pytest.mark.parametrize("invalid_input", [
    0,
    -1,
    -100
])
def test_get_max_triples_invalid_input(invalid_input):
    try:
        get_max_triples(invalid_input)
        pytest.fail("Expected ValueError was not raised")
    except ValueError:
        pass

def test_get_max_triples_type_error():
    with pytest.raises(TypeError):
        get_max_triples("invalid")
    with pytest.raises(TypeError):
        get_max_triples(None)
    with pytest.raises(TypeError):
        get_max_triples(3.14)

def test_get_max_triples_large_input():
    assert get_max_triples(10) == 36

def test_get_max_triples_verify_specific_triple():
    n = 5
    A = [i*i - i + 1 for i in range(1,n+1)]
    assert (A[0] + A[2] + A[3]) % 3 == 0