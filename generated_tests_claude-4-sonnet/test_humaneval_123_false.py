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

def get_odd_collatz(n):
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

def test_get_odd_collatz_n_equals_1():
    assert get_odd_collatz(1) == [1]

def test_get_odd_collatz_small_odd_numbers():
    assert get_odd_collatz(3) == [1, 3, 5]
    assert get_odd_collatz(5) == [1, 5]
    assert get_odd_collatz(7) == [1, 5, 7, 11, 13, 17]

def test_get_odd_collatz_small_even_numbers():
    assert get_odd_collatz(2) == [1]
    assert get_odd_collatz(4) == [1]
    assert get_odd_collatz(6) == [1, 3, 5]
    assert get_odd_collatz(8) == [1]

def test_get_odd_collatz_larger_numbers():
    assert get_odd_collatz(9) == [1, 5, 7, 9, 11, 13, 17]
    assert get_odd_collatz(10) == [1, 5]
    assert get_odd_collatz(11) == [1, 5, 11, 13, 17]
    assert get_odd_collatz(12) == [1, 5]

def test_get_odd_collatz_powers_of_two():
    assert get_odd_collatz(16) == [1]
    assert get_odd_collatz(32) == [1]
    assert get_odd_collatz(64) == [1]

def test_get_odd_collatz_result_is_sorted():
    result = get_odd_collatz(13)
    assert result == sorted(result)
    result = get_odd_collatz(15)
    assert result == sorted(result)

def test_get_odd_collatz_contains_one():
    for n in range(1, 20):
        result = get_odd_collatz(n)
        assert 1 in result

def test_get_odd_collatz_all_odd():
    for n in range(1, 20):
        result = get_odd_collatz(n)
        for num in result:
            assert num % 2 == 1

@pytest.mark.parametrize("n,expected", [
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
def test_get_odd_collatz_parametrized(n, expected):
    assert get_odd_collatz(n) == expected

def test_get_odd_collatz_no_duplicates():
    for n in range(1, 30):
        result = get_odd_collatz(n)
        assert len(result) == len(set(result))