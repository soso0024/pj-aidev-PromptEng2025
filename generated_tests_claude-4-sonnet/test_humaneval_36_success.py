# Test cases for HumanEval/36
# Generated using Claude API



def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """

    ns = []
    for i in range(n):
        if i % 11 == 0 or i % 13 == 0:
            ns.append(i)
    s = ''.join(list(map(str, ns)))
    ans = 0
    for c in s:
        ans += (c == '7')
    return ans


# Generated test cases:
import pytest

def fizz_buzz(n: int):
    ns = []
    for i in range(n):
        if i % 11 == 0 or i % 13 == 0:
            ns.append(i)
    s = ''.join(list(map(str, ns)))
    ans = 0
    for c in s:
        ans += (c == '7')
    return ans

def test_fizz_buzz_zero():
    assert fizz_buzz(0) == 0

def test_fizz_buzz_one():
    assert fizz_buzz(1) == 0

def test_fizz_buzz_small_numbers():
    assert fizz_buzz(10) == 0
    assert fizz_buzz(11) == 0
    assert fizz_buzz(12) == 0

def test_fizz_buzz_includes_multiples_of_11():
    assert fizz_buzz(14) == 0

def test_fizz_buzz_includes_multiples_of_13():
    assert fizz_buzz(15) == 0

def test_fizz_buzz_with_seven_in_result():
    result = fizz_buzz(78)
    expected_numbers = []
    for i in range(78):
        if i % 11 == 0 or i % 13 == 0:
            expected_numbers.append(i)
    combined_string = ''.join(map(str, expected_numbers))
    expected_count = combined_string.count('7')
    assert result == expected_count

def test_fizz_buzz_larger_range():
    result = fizz_buzz(100)
    expected_numbers = []
    for i in range(100):
        if i % 11 == 0 or i % 13 == 0:
            expected_numbers.append(i)
    combined_string = ''.join(map(str, expected_numbers))
    expected_count = combined_string.count('7')
    assert result == expected_count

def test_fizz_buzz_specific_case_77():
    result = fizz_buzz(78)
    expected_numbers = []
    for i in range(78):
        if i % 11 == 0 or i % 13 == 0:
            expected_numbers.append(i)
    combined_string = ''.join(map(str, expected_numbers))
    assert '77' in combined_string
    expected_count = combined_string.count('7')
    assert result == expected_count

@pytest.mark.parametrize("n,expected_multiples", [
    (22, [0, 11, 13]),
    (26, [0, 11, 13, 22]),
    (39, [0, 11, 13, 22, 26, 33]),
    (50, [0, 11, 13, 22, 26, 33, 39, 44])
])
def test_fizz_buzz_multiples_identification(n, expected_multiples):
    actual_numbers = []
    for i in range(n):
        if i % 11 == 0 or i % 13 == 0:
            actual_numbers.append(i)
    assert actual_numbers == expected_multiples

def test_fizz_buzz_negative_input():
    assert fizz_buzz(-1) == 0
    assert fizz_buzz(-10) == 0

def test_fizz_buzz_very_large_input():
    result = fizz_buzz(1000)
    expected_numbers = []
    for i in range(1000):
        if i % 11 == 0 or i % 13 == 0:
            expected_numbers.append(i)
    combined_string = ''.join(map(str, expected_numbers))
    expected_count = combined_string.count('7')
    assert result == expected_count

def test_fizz_buzz_count_sevens_in_concatenated_string():
    n = 200
    expected_numbers = []
    for i in range(n):
        if i % 11 == 0 or i % 13 == 0:
            expected_numbers.append(i)
    
    combined_string = ''.join(map(str, expected_numbers))
    manual_count = 0
    for char in combined_string:
        if char == '7':
            manual_count += 1
    
    assert fizz_buzz(n) == manual_count