# Test cases for HumanEval/86
# Generated using Claude API


def anti_shuffle(s):
    """
    Write a function that takes a string and returns an ordered version of it.
    Ordered version of string, is a string where all words (separated by space)
    are replaced by a new word where all the characters arranged in
    ascending order based on ascii value.
    Note: You should keep the order of words and blank spaces in the sentence.

    For example:
    anti_shuffle('Hi') returns 'Hi'
    anti_shuffle('hello') returns 'ehllo'
    anti_shuffle('Hello World!!!') returns 'Hello !!!Wdlor'
    """

    return ' '.join([''.join(sorted(list(i))) for i in s.split(' ')])


# Generated test cases:
import pytest

def test_anti_shuffle_empty_string():
    assert anti_shuffle('') == ''

@pytest.mark.parametrize("input,expected", [
    ("hello world", "ehll oowrd"),
    ("python is awesome", "phtyon iasewmoe"),
    ("a b c d e", "a b c d e"),
    ("   leading spaces   ", "   aeilngps   "),
    ("trailing spaces   ", "ailgnrsp   "),
    ("   both leading and trailing spaces   ", "   aeilbhnogt dnsrpaces   ")
])
def test_anti_shuffle_normal_cases(input, expected):
    assert anti_shuffle(input) == expected

def test_anti_shuffle_single_character():
    assert anti_shuffle('a') == 'a'

def test_anti_shuffle_all_whitespace():
    assert anti_shuffle('   ') == '   '

def test_anti_shuffle_non_string_input():
    with pytest.raises(TypeError):
        anti_shuffle(123)