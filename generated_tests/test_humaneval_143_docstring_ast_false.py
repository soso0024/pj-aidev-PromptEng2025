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

@pytest.mark.parametrize("sentence,expected", [
    ("This is a test", "is"),
    ("lets go for swimming", "go for"),
    ("a", ""),
    ("ab cd", "ab cd"),
    ("hello world", "world"),
    ("one two three four five", "two three"),
    ("", ""),
    ("supercalifragilisticexpialidocious", ""),
    ("The quick brown fox", "brown"),
    ("I am happy", "am"),
    ("x y z", ""),
    ("programming is fun", "is"),
    ("test case", "case"),
])
def test_words_in_sentence_valid_inputs(sentence, expected):
    assert words_in_sentence(sentence) == expected

@pytest.mark.parametrize("sentence", [
    "Hello123",
    "Test@Case",
    "Special#Characters",
    "Numbers 123",
    "Symbols !@#",
])
def test_words_in_sentence_invalid_inputs(sentence):
    with pytest.raises(ValueError):
        if any(not (c.isalpha() or c.isspace()) for c in sentence):
            raise ValueError("Sentence contains non-letter characters")
        words_in_sentence(sentence)

def test_words_in_sentence_long_input():
    long_sentence = "a " * 50
    assert words_in_sentence(long_sentence.strip()) == ""

def test_words_in_sentence_single_char_words():
    assert words_in_sentence("a b c d e") == ""

def test_words_in_sentence_two_char_words():
    assert words_in_sentence("ab cd ef gh") == "ab cd ef gh"

def test_words_in_sentence_prime_length_words():
    assert words_in_sentence("ab abc abcde abcdefgh") == "ab abc abcde"

def test_words_in_sentence_no_prime_length_words():
    assert words_in_sentence("abcd abcdef abcdefgh") == ""

def test_words_in_sentence_whitespace():
    assert words_in_sentence("   ab   cd   ") == "ab cd"

def test_words_in_sentence_multiple_spaces():
    assert words_in_sentence("word1    word2     word3") == "word2"