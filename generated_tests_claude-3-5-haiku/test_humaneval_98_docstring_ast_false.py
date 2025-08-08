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
    assert count_upper('aBCdEf') == 1
    assert count_upper('abcdefg') == 0
    assert count_upper('dBBE') == 0

def test_count_upper_edge_cases():
    assert count_upper('') == 0
    assert count_upper('A') == 1
    assert count_upper('a') == 0
    assert count_upper('AEIOU') == 1
    assert count_upper('aEiOu') == 2

@pytest.mark.parametrize("input_str,expected", [
    ('aBCdEf', 1),
    ('abcdefg', 0),
    ('dBBE', 0),
    ('', 0),
    ('A', 1),
    ('a', 0),
    ('AEIOU', 1),
    ('aEiOu', 2),
    ('xAyEzIoU', 2)
])
def test_count_upper_parametrized(input_str, expected):
    assert count_upper(input_str) == expected

def test_count_upper_long_string():
    assert count_upper('aAeEiIoOuU' * 10) == 10