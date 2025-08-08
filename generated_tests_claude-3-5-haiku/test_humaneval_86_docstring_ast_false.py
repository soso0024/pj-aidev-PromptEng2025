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
    return ' '.join([''.join(sorted(word)) for word in s.split(' ')])

def test_anti_shuffle_basic_words():
    assert anti_shuffle('hello') == 'ehllo'
    assert anti_shuffle('world') == 'dlorw'

def test_anti_shuffle_multiple_words():
    assert anti_shuffle('hello world') == 'ehllo dlorw'
    assert anti_shuffle('Hi there') == 'Hi eehtrt'

def test_anti_shuffle_with_punctuation():
    assert anti_shuffle('Hello World!!!') == 'Hello !!!Wdlor'
    assert anti_shuffle('test, case') == 'est, acet'

def test_anti_shuffle_mixed_case():
    assert anti_shuffle('Python Programming') == 'Phnoty Aagmmnorpgr'

def test_anti_shuffle_single_character():
    assert anti_shuffle('a') == 'a'
    assert anti_shuffle('Z') == 'Z'

def test_anti_shuffle_empty_string():
    assert anti_shuffle('') == ''

def test_anti_shuffle_spaces():
    assert anti_shuffle('  ') == '  '
    assert anti_shuffle(' test ') == ' estt '

def test_anti_shuffle_numbers_and_symbols():
    assert anti_shuffle('123 abc !@#') == '123 abc !#@'

@pytest.mark.parametrize("input_str,expected", [
    ('hello', 'ehllo'),
    ('world', 'dlorw'),
    ('Hello World!!!', 'Hello !!!Wdlor'),
    ('', ''),
    ('a', 'a'),
    ('test case', 'estt acet')
])
def test_anti_shuffle_parametrized(input_str, expected):
    assert anti_shuffle(input_str) == expected