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
    ("ab cd", "ab"),
    ("hello world", "hello"),
    ("one two three four five", "two three"),
    ("", ""),
    ("pneumonoultramicroscopicsilicovolcanoconiosis", ""),
    ("a ab abc abcd abcde", "ab abc"),
    ("The quick brown fox jumps", "quick brown fox"),
])
def test_words_in_sentence_valid_inputs(sentence, expected):
    result = words_in_sentence(sentence)
    assert result == expected

def test_words_in_sentence_single_letter():
    assert words_in_sentence("a") == ""

def test_words_in_sentence_all_prime_lengths():
    assert words_in_sentence("ab abc abcde") == "ab abc"

def test_words_in_sentence_no_prime_lengths():
    assert words_in_sentence("abcd abcdef") == ""

def test_words_in_sentence_empty_string():
    assert words_in_sentence("") == ""

def test_words_in_sentence_multiple_spaces():
    assert words_in_sentence("ab    abc   abcd") == "ab abc"

@pytest.mark.parametrize("invalid_input", [
    None,
    123,
    ["test"],
    {"key": "value"},
    True
])
def test_words_in_sentence_invalid_inputs(invalid_input):
    with pytest.raises(AttributeError):
        words_in_sentence(invalid_input)

def test_words_in_sentence_special_cases():
    assert words_in_sentence("a b c") == ""
    assert words_in_sentence("aa bb cc") == ""
    assert words_in_sentence("aaa bbb ccc") == "aaa bbb ccc"

def test_words_in_sentence_long_words():
    long_sentence = "antidisestablishmentarianism supercalifragilisticexpialidocious"
    assert words_in_sentence(long_sentence) == ""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def words_in_sentence(sentence):
    if not sentence:
        return ""
    words = sentence.split()
    return " ".join(word for word in words if is_prime(len(word)))