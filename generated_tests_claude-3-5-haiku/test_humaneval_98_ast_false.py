# Test cases for HumanEval/98
# Generated using Claude API


def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """

    count = 0
    for i in range(0,len(s),2):
        if s[i] in "AEIOU":
            count += 1
    return count


# Generated test cases:
import pytest

def count_upper(s):
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    
    count = 0
    for i in range(0, len(s), 2):
        if s[i] in "AEIOU" and s[i].isupper():
            count += 1
    return count

def test_count_upper_normal_cases():
    assert count_upper("AEIOU") == 3
    assert count_upper("aeiou") == 0
    assert count_upper("HELLO") == 1
    assert count_upper("hello") == 0

def test_count_upper_empty_string():
    assert count_upper("") == 0

def test_count_upper_mixed_case():
    assert count_upper("HeLLo") == 1
    assert count_upper("AeIoU") == 2

def test_count_upper_long_string():
    assert count_upper("ABCDEFGHIJKLMNOPQRSTUVWXYZ") == 5
    assert count_upper("aAbBcCdDeE") == 2

@pytest.mark.parametrize("input_str,expected", [
    ("AEIOU", 3),
    ("aeiou", 0),
    ("", 0),
    ("HeLLo", 1),
    ("AeIoU", 2),
    ("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 5),
    ("aAbBcCdDeE", 2)
])
def test_count_upper_parametrized(input_str, expected):
    assert count_upper(input_str) == expected

def test_count_upper_non_string_input():
    with pytest.raises(TypeError):
        count_upper(123)
    with pytest.raises(TypeError):
        count_upper(None)