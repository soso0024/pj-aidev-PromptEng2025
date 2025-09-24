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

def test_get_odd_collatz_one():
    assert get_odd_collatz(1) == [1]

def test_get_odd_collatz_five():
    assert get_odd_collatz(5) == [1, 5]

def test_get_odd_collatz_even_start():
    assert get_odd_collatz(2) == [1]
    assert get_odd_collatz(4) == [1]
    assert get_odd_collatz(8) == [1]
    assert get_odd_collatz(16) == [1]

def test_get_odd_collatz_odd_start():
    assert get_odd_collatz(3) == [1, 3, 5]
    assert get_odd_collatz(7) == [1, 5, 7, 11, 13, 17]
    assert get_odd_collatz(9) == [1, 5, 7, 9, 11, 13, 17]

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
    (10, [1, 5]),
    (11, [1, 5, 11, 13, 17]),
    (12, [1, 3, 5]),
    (13, [1, 5, 13]),
    (14, [1, 5, 7, 11, 13, 17]),
    (15, [1, 5, 15, 23, 35, 53]),
    (16, [1]),
    (17, [1, 5, 13, 17]),
    (18, [1, 5, 7, 9, 11, 13, 17]),
    (19, [1, 5, 11, 13, 17, 19, 29]),
    (20, [1, 5])
])
def test_get_odd_collatz_parametrized(n, expected):
    assert get_odd_collatz(n) == expected

def test_get_odd_collatz_larger_numbers():
    result = get_odd_collatz(27)
    assert 1 in result
    assert 27 in result
    assert all(x % 2 == 1 for x in result)
    assert result == sorted(result)

def test_get_odd_collatz_power_of_two():
    for i in range(1, 10):
        power_of_two = 2 ** i
        assert get_odd_collatz(power_of_two) == [1]

def test_get_odd_collatz_result_properties():
    for n in range(1, 21):
        result = get_odd_collatz(n)
        assert 1 in result
        assert all(x % 2 == 1 for x in result)
        assert result == sorted(result)
        assert len(result) == len(set(result))