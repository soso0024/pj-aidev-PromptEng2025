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

def test_anti_shuffle_basic_case():
    assert anti_shuffle('hello world') == 'ehllo dlorw'

def test_anti_shuffle_multiple_words():
    assert anti_shuffle('python is awesome') == 'hnopty is aeemosw'

def test_anti_shuffle_single_word():
    assert anti_shuffle('programming') == 'aggimnoprr'

def test_anti_shuffle_empty_string():
    assert anti_shuffle('') == ''

def test_anti_shuffle_single_character_words():
    assert anti_shuffle('a b c') == 'a b c'

def test_anti_shuffle_mixed_case():
    assert anti_shuffle('Hello World') == 'Helo Dlorw'

def test_anti_shuffle_numbers_and_words():
    assert anti_shuffle('123 hello 456') == '123 ehllo 456'

@pytest.mark.parametrize("input_str,expected", [
    ('hello world', 'ehllo dlorw'),
    ('python is awesome', 'hnopty is aeemosw'),
    ('', ''),
    ('a b c', 'a b c'),
    ('Hello World', 'Helo Dlorw'),
    ('123 hello 456', '123 ehllo 456')
])
def test_anti_shuffle_parametrized(input_str, expected):
    assert anti_shuffle(input_str) == expected