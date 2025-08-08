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

def test_anti_shuffle_single_word():
    assert anti_shuffle('hello') == 'ehllo'
    assert anti_shuffle('Hi') == 'Hi'

def test_anti_shuffle_multiple_words():
    assert anti_shuffle('Hello World!!!') == 'Hello !!!Wdlor'
    assert anti_shuffle('The quick brown fox jumps over the lazy dog') == 'The kcuq bnowr xfo jumps over the azy dgo'

def test_anti_shuffle_with_numbers():
    assert anti_shuffle('123 abc DEF') == '123 abc DEF'

def test_anti_shuffle_with_special_characters():
    assert anti_shuffle('Hello, World!') == 'Hello, !Wdlor'
    assert anti_shuffle('A1b! c@d#') == 'A1b! c@d#'

def test_anti_shuffle_with_mixed_case():
    assert anti_shuffle('aBc dEf') == 'Abc dEf'

def test_anti_shuffle_with_leading_and_trailing_spaces():
    assert anti_shuffle('  hello world  ') == '  ehllo dlrow  '

def test_anti_shuffle_with_multiple_spaces():
    assert anti_shuffle('hello   world') == 'ehllo   dlrow'

def test_anti_shuffle_with_non_ascii_characters():
    assert anti_shuffle('Héllò, Wórld!') == 'Héllò, !Wórld'