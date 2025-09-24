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

@pytest.mark.parametrize("n,expected", [
    (1, 0),
    (2, 0),
    (3, 0),
    (4, 1),
    (5, 1),
    (6, 4),
    (7, 10),
    (8, 11),
    (9, 21),
    (10, 36)
])
def test_get_max_triples_parametrized(n, expected):
    assert get_max_triples(n) == expected

def test_get_max_triples_edge_case_n_1():
    assert get_max_triples(1) == 0

def test_get_max_triples_edge_case_n_2():
    assert get_max_triples(2) == 0

def test_get_max_triples_edge_case_n_3():
    assert get_max_triples(3) == 0

def test_get_max_triples_example_case():
    assert get_max_triples(5) == 1

def test_get_max_triples_larger_values():
    assert get_max_triples(15) == 130
    assert get_max_triples(20) == 321

def test_get_max_triples_verify_array_generation():
    n = 5
    A = [i*i - i + 1 for i in range(1, n+1)]
    expected_array = [1, 3, 7, 13, 21]
    assert A == expected_array

def test_get_max_triples_verify_triple_sum():
    n = 5
    A = [i*i - i + 1 for i in range(1, n+1)]
    valid_triple_sum = A[0] + A[2] + A[3]  # 1 + 7 + 13 = 21
    assert valid_triple_sum % 3 == 0

def test_get_max_triples_small_cases():
    for i in range(1, 5):
        result = get_max_triples(i)
        assert isinstance(result, int)
        assert result >= 0