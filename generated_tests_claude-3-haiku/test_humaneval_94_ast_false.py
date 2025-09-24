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

def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

def skjkasdkd(lst):
    maxx = 0
    for i in range(len(lst)):
        if lst[i] > maxx and isPrime(lst[i]):
            maxx = lst[i]
    result = sum(int(digit) for digit in str(maxx))
    return result

def test_skjkasdkd_empty_list():
    assert skjkasdkd([]) == 0

def test_skjkasdkd_all_non_primes():
    assert skjkasdkd([4, 6, 8, 10]) == 0

def test_skjkasdkd_all_primes():
    assert skjkasdkd([2, 3, 5, 7, 11]) == 28

def test_skjkasdkd_mixed_list():
    assert skjkasdkd([2, 4, 6, 7, 11, 13]) == 21

def test_skjkasdkd_single_prime():
    assert skjkasdkd([7]) == 7

def test_skjkasdkd_negative_numbers():
    assert skjkasdkd([-2, -3, -5]) == 0

@pytest.mark.parametrize("input,expected", [
    ([2, 3, 5, 7, 11, 13, 17, 19], 19),
    ([100, 101, 103, 107, 109, 113, 127, 131], 19),
    ([1000, 1001, 1003, 1009, 1013, 1019, 1021, 1031], 14),
    ([10000, 10001, 10003, 10009, 10037, 10039, 10043, 10049], 27)
])
def test_skjkasdkd_larger_lists(input, expected):
    assert skjkasdkd(input) == expected

def test_skjkasdkd_non_integer_list():
    with pytest.raises(TypeError):
        skjkasdkd([2, 3, 'a', 5, 7])