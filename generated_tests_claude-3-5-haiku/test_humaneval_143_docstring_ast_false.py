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

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def words_in_sentence(sentence):
    if not sentence:
        return ""
    
    new_lst = []
    for word in sentence.split():
        if is_prime(len(word)):
            new_lst.append(word)
    
    return " ".join(new_lst)

def test_words_in_sentence_normal_cases():
    assert words_in_sentence("This is a test") == "is"
    assert words_in_sentence("lets go for swimming") == "go for"

def test_words_in_sentence_edge_cases():
    assert words_in_sentence("") == ""
    assert words_in_sentence("a") == "a"
    assert words_in_sentence("ab") == "ab"

@pytest.mark.parametrize("sentence,expected", [
    ("hello world", ""),
    ("python programming language", "python"),
    ("short long longer longest", "short long"),
    ("two three five seven eleven", "two three five seven eleven"),
])
def test_words_in_sentence_parametrized(sentence, expected):
    assert words_in_sentence(sentence) == expected

def test_words_in_sentence_case_sensitivity():
    assert words_in_sentence("PRIME words TEST") == "PRIME"

def test_words_in_sentence_special_characters():
    assert words_in_sentence("no special chars here") == "no special"