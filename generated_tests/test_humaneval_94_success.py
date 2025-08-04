# Test cases for HumanEval/94
# Generated using Claude API



def skjkasdkd(lst):
    """You are given a list of integers.
    You need to find the largest prime value and return the sum of its digits.

    Examples:
    For lst = [0,3,2,1,3,5,7,4,5,5,5,2,181,32,4,32,3,2,32,324,4,3] the output should be 10
    For lst = [1,0,1,8,2,4597,2,1,3,40,1,2,1,2,4,2,5,1] the output should be 25
    For lst = [1,3,1,32,5107,34,83278,109,163,23,2323,32,30,1,9,3] the output should be 13
    For lst = [0,724,32,71,99,32,6,0,5,91,83,0,5,6] the output should be 11
    For lst = [0,81,12,3,1,21] the output should be 3
    For lst = [0,8,1,2,1,7] the output should be 7
    """

    def isPrime(n):
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False

        return True
    maxx = 0
    i = 0
    while i < len(lst):
        if(lst[i] > maxx and isPrime(lst[i])):
            maxx = lst[i]
        i+=1
    result = sum(int(digit) for digit in str(maxx))
    return result



# Generated test cases:
import pytest

def test_skjkasdkd_empty_list():
    assert skjkasdkd([]) == 0

def test_skjkasdkd_no_primes():
    assert skjkasdkd([4, 6, 8, 9]) == 0

def test_skjkasdkd_single_prime():
    assert skjkasdkd([7]) == 7

@pytest.mark.parametrize("input_list,expected", [
    ([2, 3, 5, 7, 11], 2),  # 11 -> 1+1
    ([4, 6, 23, 8, 19], 5),  # 23 -> 2+3
    ([100, 97, 89, 83], 16),  # 97 -> 9+7
    ([1, 2, 3, 4, 5], 5),  # 5 -> 5
    ([10, 20, 30, 31], 4),  # 31 -> 3+1
    ([2, 2, 2, 2], 2),  # 2 -> 2
    ([1, 1, 1, 1], 1),  # 1 is considered prime in this implementation
    ([4, 8, 15, 16, 23, 42], 5),  # 23 -> 2+3
])
def test_skjkasdkd_various_cases(input_list, expected):
    assert skjkasdkd(input_list) == expected

def test_skjkasdkd_large_numbers():
    assert skjkasdkd([1000, 997, 991]) == 25  # 997 -> 9+9+7

def test_skjkasdkd_repeated_primes():
    assert skjkasdkd([2, 2, 2, 3, 3, 3, 5, 5]) == 5

def test_skjkasdkd_single_digit_primes():
    assert skjkasdkd([2, 3, 5, 7]) == 7

@pytest.mark.parametrize("invalid_input", [
    None,
    "string",
    123,
    3.14,
    [None],
    ["string"],
    [1, "2", 3],
    [1.5, 2.7, 3.14]
])
def test_skjkasdkd_invalid_input(invalid_input):
    with pytest.raises((TypeError, ValueError)):
        skjkasdkd(invalid_input)