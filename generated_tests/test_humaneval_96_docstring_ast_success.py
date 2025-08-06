# Test cases for HumanEval/96
# Generated using Claude API


def count_up_to(n):
    """Implement a function that takes an non-negative integer and returns an array of the first n
    integers that are prime numbers and less than n.
    for example:
    count_up_to(5) => [2,3]
    count_up_to(11) => [2,3,5,7]
    count_up_to(0) => []
    count_up_to(20) => [2,3,5,7,11,13,17,19]
    count_up_to(1) => []
    count_up_to(18) => [2,3,5,7,11,13,17]
    """

    primes = []
    for i in range(2, n):
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    return primes



# Generated test cases:
import pytest

def test_count_up_to_zero():
    assert count_up_to(0) == []

def test_count_up_to_one():
    assert count_up_to(1) == []

def test_count_up_to_two():
    assert count_up_to(2) == []

def test_count_up_to_three():
    assert count_up_to(3) == [2]

def test_count_up_to_five():
    assert count_up_to(5) == [2, 3]

def test_count_up_to_eleven():
    assert count_up_to(11) == [2, 3, 5, 7]

def test_count_up_to_twenty():
    assert count_up_to(20) == [2, 3, 5, 7, 11, 13, 17, 19]

def test_count_up_to_eighteen():
    assert count_up_to(18) == [2, 3, 5, 7, 11, 13, 17]

@pytest.mark.parametrize("input_n,expected", [
    (0, []),
    (1, []),
    (2, []),
    (3, [2]),
    (5, [2, 3]),
    (11, [2, 3, 5, 7]),
    (20, [2, 3, 5, 7, 11, 13, 17, 19]),
    (18, [2, 3, 5, 7, 11, 13, 17])
])
def test_count_up_to_parametrized(input_n, expected):
    assert count_up_to(input_n) == expected

def test_count_up_to_negative_numbers():
    for n in [-1, -100, -999]:
        result = count_up_to(n)
        assert result == []

def test_count_up_to_large_number():
    result = count_up_to(100)
    assert len(result) == 25  # Number of primes less than 100
    assert result[:5] == [2, 3, 5, 7, 11]  # First few primes
    assert result[-5:] == [73, 79, 83, 89, 97]  # Last few primes

def test_count_up_to_type_error():
    with pytest.raises(TypeError):
        count_up_to("not a number")
    with pytest.raises(TypeError):
        count_up_to([1, 2, 3])
    with pytest.raises(TypeError):
        count_up_to(None)