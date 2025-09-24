# Test cases for HumanEval/143
# Generated using Claude API


def words_in_sentence(sentence):
    """
    You are given a string representing a sentence,
    the sentence contains some words separated by a space,
    and you have to return a string that contains the words from the original sentence,
    whose lengths are prime numbers,
    the order of the words in the new string should be the same as the original one.

    Example 1:
        Input: sentence = "This is a test"
        Output: "is"

    Example 2:
        Input: sentence = "lets go for swimming"
        Output: "go for"

    Constraints:
        * 1 <= len(sentence) <= 100
        * sentence contains only letters
    """

    new_lst = []
    for word in sentence.split():
        flg = 0
        if len(word) == 1:
            flg = 1
        for i in range(2, len(word)):
            if len(word)%i == 0:
                flg = 1
        if flg == 0 or len(word) == 2:
            new_lst.append(word)
    return " ".join(new_lst)


# Generated test cases:
import pytest

def words_in_sentence(sentence):
    new_lst = []
    for word in sentence.split():
        flg = 0
        if len(word) == 1:
            flg = 1
        for i in range(2, len(word)):
            if len(word)%i == 0:
                flg = 1
        if flg == 0 or len(word) == 2:
            new_lst.append(word)
    return " ".join(new_lst)

@pytest.mark.parametrize("sentence,expected", [
    ("", ""),
    (" ", ""),
    ("a", ""),
    ("ab", "ab"),
    ("abc", "abc"),
    ("abcd", ""),
    ("abcde", "abcde"),
    ("abcdef", ""),
    ("abcdefg", "abcdefg"),
    ("abcdefgh", ""),
    ("abcdefghi", ""),
    ("abcdefghij", ""),
    ("abcdefghijk", "abcdefghijk"),
    ("a b", ""),
    ("ab cd", "ab cd"),
    ("abc def", "abc def"),
    ("abcd efgh", ""),
    ("ab abc abcd", "ab abc"),
    ("hello world", "hello world"),
    ("this is a test", "is"),
    ("prime numbers are fun", "prime numbers are fun"),
    ("I love programming", "programming"),
    ("a ab abc abcd abcde", "ab abc abcde"),
    ("x xy xyz", "xy xyz"),
    ("  multiple   spaces  ", ""),
    ("single", ""),
    ("double", ""),
    ("triple", ""),
    ("quadruple", ""),
    ("quintuple", ""),
])
def test_words_in_sentence(sentence, expected):
    assert words_in_sentence(sentence) == expected

def test_empty_string():
    assert words_in_sentence("") == ""

def test_single_character_words():
    assert words_in_sentence("a b c d e") == ""

def test_two_character_words():
    assert words_in_sentence("ab cd ef gh") == "ab cd ef gh"

def test_prime_length_words():
    assert words_in_sentence("ab abc abcde abcdefg") == "ab abc abcde abcdefg"

def test_composite_length_words():
    assert words_in_sentence("abcd abcdef abcdefgh") == ""

def test_mixed_lengths():
    assert words_in_sentence("a ab abc abcd abcde abcdef") == "ab abc abcde"

def test_whitespace_handling():
    assert words_in_sentence("  ab   cd  ") == "ab cd"

def test_single_word_prime_length():
    assert words_in_sentence("hello") == "hello"

def test_single_word_composite_length():
    assert words_in_sentence("test") == ""

def test_single_word_length_one():
    assert words_in_sentence("a") == ""

def test_single_word_length_two():
    assert words_in_sentence("ab") == "ab"