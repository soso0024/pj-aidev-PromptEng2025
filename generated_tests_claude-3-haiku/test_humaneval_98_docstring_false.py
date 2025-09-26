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

@pytest.mark.parametrize("input_str,expected", [
    ('aBCdEf', 1),
    ('abcdefg', 0),
    ('dBBE', 0),
    ('', 0),
    ('A', 0),
    ('aE', 1),
    ('aEiOu', 2),
    ('AEIOU', 0),
    ('a1B2C3D4E5', 2),
    ('Hello, World!', 0)
])
def test_count_upper(input_str, expected):
    assert count_upper(input_str) == expected

def count_upper(s):
    count = 0
    for i in range(0, len(s), 2):
        if s[i].isupper() and s[i] in "AEIOU":
            count += 1
    return count