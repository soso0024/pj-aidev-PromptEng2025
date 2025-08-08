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
    assert count_upper("") == 0

@pytest.mark.parametrize("input_str,expected", [
    ("AEIOU", 3),
    ("AEIOUaeiou", 5),
    ("abcdefgh", 0),
    ("A E I O U", 5),
    ("   A   E   I   O   U   ", 5)
])
def test_count_upper_valid_inputs(input_str, expected):
    assert count_upper(input_str) == expected

def test_count_upper_non_string_input():
    with pytest.raises(TypeError):
        count_upper(123)