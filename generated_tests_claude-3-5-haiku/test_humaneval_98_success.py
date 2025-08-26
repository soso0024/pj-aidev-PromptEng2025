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

def test_count_upper_normal_cases():
    assert count_upper("AEIOU") == 3
    assert count_upper("aeiou") == 0
    assert count_upper("HELLO") == 1
    assert count_upper("hello") == 0

def test_count_upper_edge_cases():
    assert count_upper("") == 0
    assert count_upper("A") == 1
    assert count_upper("a") == 0
    assert count_upper("ABCDEFGHIJKLMNOPQRSTUVWXYZ") == 5

@pytest.mark.parametrize("input_str,expected", [
    ("AEIOU", 3),
    ("aeiou", 0),
    ("HELLO", 1),
    ("hello", 0),
    ("", 0),
    ("A", 1),
    ("a", 0),
    ("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 5)
])
def test_count_upper_parametrized(input_str, expected):
    assert count_upper(input_str) == expected

def test_count_upper_mixed_case():
    assert count_upper("AeIoU") == 3
    assert count_upper("HeLlO") == 1

def test_count_upper_non_alphabetic():
    assert count_upper("123456") == 0
    assert count_upper("A1E2I3O4U5") == 5