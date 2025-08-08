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
    assert get_odd_collatz(5) == [1, 5]
    assert get_odd_collatz(1) == [1]
    assert get_odd_collatz(4) == [1]

@pytest.mark.parametrize("input_n,expected", [
    (1, [1]),
    (2, [1]),
    (3, [1, 3]),
    (4, [1]),
    (5, [1, 5]),
    (6, [1, 3]),
    (7, [1, 7, 11, 17]),
    (10, [1, 5]),
    (20, [1, 5]),
])
def test_get_odd_collatz_various_inputs(input_n, expected):
    assert get_odd_collatz(input_n) == expected

def test_get_odd_collatz_larger_numbers():
    assert get_odd_collatz(27) == [1, 5, 7, 9, 27, 31, 41, 61, 91, 103]
    assert get_odd_collatz(50) == [1, 5]

@pytest.mark.parametrize("input_n", [100, 200, 500])
def test_get_odd_collatz_ends_with_one(input_n):
    result = get_odd_collatz(input_n)
    assert 1 in result
    assert result == sorted(result)
    assert all(x % 2 == 1 for x in result)

def test_get_odd_collatz_sorted_output():
    result = get_odd_collatz(27)
    assert result == sorted(result)

@pytest.mark.parametrize("invalid_input", [0, -1, -5, -100])
def test_get_odd_collatz_invalid_inputs(invalid_input):
    with pytest.raises(ValueError):
        get_odd_collatz(invalid_input)

def test_get_odd_collatz_type_check():
    result = get_odd_collatz(15)
    assert all(isinstance(x, int) for x in result)

def test_get_odd_collatz_uniqueness():
    result = get_odd_collatz(27)
    assert len(result) == len(set(result))

def get_odd_collatz(n):
    if n <= 0:
        raise ValueError("Input must be a positive integer")
    
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