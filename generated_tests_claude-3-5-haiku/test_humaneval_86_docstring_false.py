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

def anti_shuffle(s):
    return ' '.join([''.join(sorted(word)) if word.isalpha() else word for word in s.split(' ')])

def test_anti_shuffle_single_word():
    assert anti_shuffle('hello') == 'ehllo'
    assert anti_shuffle('world') == 'dlorw'

def test_anti_shuffle_multiple_words():
    assert anti_shuffle('Hello World') == 'Hello Wdlor'
    assert anti_shuffle('python programming') == 'python aagmmnoprrg'

def test_anti_shuffle_with_punctuation():
    assert anti_shuffle('Hello World!!!') == 'Hello !!!Wdlor'
    assert anti_shuffle('test, case') == 'est, acst'

def test_anti_shuffle_mixed_case():
    assert anti_shuffle('AbCdE') == 'AbCdE'
    assert anti_shuffle('ZaYbXc') == 'AabcXYz'

def test_anti_shuffle_empty_string():
    assert anti_shuffle('') == ''

def test_anti_shuffle_single_character():
    assert anti_shuffle('a') == 'a'
    assert anti_shuffle('Z') == 'Z'

@pytest.mark.parametrize("input_str,expected", [
    ('hello', 'ehllo'),
    ('world', 'dlorw'),
    ('Hello World', 'Hello Wdlor'),
    ('python programming', 'python aagmmnoprrg'),
    ('', ''),
    ('a', 'a'),
    ('Hello World!!!', 'Hello !!!Wdlor')
])
def test_anti_shuffle_parametrized(input_str, expected):
    assert anti_shuffle(input_str) == expected