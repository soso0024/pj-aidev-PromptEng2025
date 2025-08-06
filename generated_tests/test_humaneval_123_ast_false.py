# Test cases for HumanEval/123
# Generated using Claude API


def get_odd_collatz(n):
    """
    Given a positive integer n, return a sorted list that has the odd numbers in collatz sequence.

    The Collatz conjecture is a conjecture in mathematics that concerns a sequence defined
    as follows: start with any positive integer n. Then each term is obtained from the 
    previous term as follows: if the previous term is even, the next term is one half of 
    the previous term. If the previous term is odd, the next term is 3 times the previous
    term plus 1. The conjecture is that no matter what value of n, the sequence will always reach 1.

    Note: 
        1. Collatz(1) is [1].
        2. returned list sorted in increasing order.

    For example:
    get_odd_collatz(5) returns [1, 5] # The collatz sequence for 5 is [5, 16, 8, 4, 2, 1], so the odd numbers are only 1, and 5.
    """

    if n%2==0:
        odd_collatz = [] 
    else:
        odd_collatz = [n]
    while n > 1:
        if n % 2 == 0:
            n = n/2
        else:
            n = n*3 + 1
            
        if n%2 == 1:
            odd_collatz.append(int(n))

    return sorted(odd_collatz)


# Generated test cases:
import pytest

def test_get_odd_collatz_basic():
    assert get_odd_collatz(3) == [1, 3, 5]
    assert get_odd_collatz(6) == [1, 3, 5]
    assert get_odd_collatz(7) == [1, 5, 7, 11, 13, 17]

def test_get_odd_collatz_edge_cases():
    assert get_odd_collatz(1) == [1]
    assert get_odd_collatz(2) == [1]
    assert get_odd_collatz(4) == [1]

@pytest.mark.parametrize("input_n,expected", [
    (1, [1]),
    (2, [1]),
    (3, [1, 3, 5]),
    (4, [1]),
    (5, [1, 5]),
    (6, [1, 3, 5]),
    (7, [1, 5, 7, 11, 13, 17]),
    (8, [1]),
    (9, [1, 5, 7, 9, 11, 13, 17]),
    (10, [1, 5])
])
def test_get_odd_collatz_parametrized(input_n, expected):
    assert sorted(get_odd_collatz(input_n)) == sorted(expected)

def test_get_odd_collatz_type():
    result = get_odd_collatz(3)
    assert isinstance(result, list)
    assert all(isinstance(x, int) for x in result)

@pytest.mark.parametrize("input_n", [-1, 0, -5, -10])
def test_get_odd_collatz_negative_numbers(input_n):
    try:
        get_odd_collatz(input_n)
        pytest.fail("Expected ValueError for negative numbers or zero")
    except ValueError:
        pass

@pytest.mark.parametrize("input_n", [1.5, 2.7, "3", [4], {5}])
def test_get_odd_collatz_invalid_types(input_n):
    try:
        get_odd_collatz(input_n)
        pytest.fail("Expected TypeError for invalid input types")
    except TypeError:
        pass

def test_get_odd_collatz_large_number():
    result = get_odd_collatz(27)
    assert isinstance(result, list)
    assert len(result) > 0
    assert all(x % 2 == 1 for x in result)
    assert 1 in result
    assert 27 in result