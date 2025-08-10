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
        if len(word) == 1 or (len(word) > 1 and all(word[i] != word[0] or i == 0 for i in range(len(word)))):
            new_lst.append(word)
    return " ".join(new_lst)

def test_words_in_sentence():
    assert words_in_sentence("The quick brown fox jumps over the lazy dog") == "The quick brown fox jumps over the lazy dog"
    assert words_in_sentence("Hello, world! 123 abc def") == "Hello, world! abc def"
    assert words_in_sentence("a b c d e") == "a b c d e"
    assert words_in_sentence("aa bb cc dd") == "aa bb cc dd"
    assert words_in_sentence("a b c d e f g") == "a b c d e f g"
    assert words_in_sentence("") == ""
    assert words_in_sentence("   ") == ""
    assert words_in_sentence("123") == ""
    assert words_in_sentence("abc123") == "abc"
    assert words_in_sentence("abc123def") == "abc def"

@pytest.mark.parametrize("input,expected", [
    ("The quick brown fox jumps over the lazy dog", "The quick brown fox jumps over the lazy dog"),
    ("Hello, world! 123 abc def", "Hello, world! abc def"),
    ("a b c d e", "a b c d e"),
    ("aa bb cc dd", "aa bb cc dd"),
    ("a b c d e f g", "a b c d e f g"),
    ("", ""),
    ("   ", ""),
    ("123", ""),
    ("abc123", "abc"),
    ("abc123def", "abc def")
])
def test_words_in_sentence_parametrized(input, expected):
    assert words_in_sentence(input) == expected