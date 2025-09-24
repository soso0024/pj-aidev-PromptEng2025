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

def test_count_upper_empty_string():
    assert count_upper('') == 0

def test_count_upper_all_uppercase():
    assert count_upper('AEIOU') == 5

def test_count_upper_all_lowercase():
    assert count_upper('aeiou') == 0

@pytest.mark.parametrize("input,expected", [
    ('A3B2C1D4', 2),
    ('HELLO WORLD', 2),
    ('123456789', 0),
    ('AeIoU', 5),
    ('aEiOu', 5)
])
def test_count_upper_various_inputs(input, expected):
    assert count_upper(input) == expected

def test_count_upper_non_string_input():
    with pytest.raises(TypeError):
        count_upper(123)

def count_upper(s):
    count = 0
    for i in range(0, len(s), 2):
        if s[i] in "AEIOU":
            count += 1
    return count