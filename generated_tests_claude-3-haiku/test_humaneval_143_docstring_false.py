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
from your_module import words_in_sentence

@pytest.mark.parametrize("sentence,expected", [
    ("This is a test", "is"),
    ("lets go for swimming", "go for"),
    ("Hello World", ""),
    ("a b c d e", "a c e"),
    ("", ""),
    ("  ", ""),
    ("123 456 789", ""),
    ("Hello123 World456", "World"),
    ("This   is   a   test", "is a"),
    ("The quick brown fox jumps over the lazy dog", "quick fox jumps over the dog")
])
def test_words_in_sentence(sentence, expected):
    assert words_in_sentence(sentence) == expected

def test_edge_cases():
    assert words_in_sentence("1") == ""
    assert words_in_sentence("a b") == "a"
    assert words_in_sentence("ab cd") == "ab cd"
    assert words_in_sentence("a b c d e f g") == "a c e g"

def test_error_handling():
    with pytest.raises(TypeError):
        words_in_sentence(123)
    with pytest.raises(TypeError):
        words_in_sentence(None)