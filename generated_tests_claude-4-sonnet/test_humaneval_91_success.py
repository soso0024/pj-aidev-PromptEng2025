# Test cases for HumanEval/91
# Generated using Claude API


def is_bored(S):
    """
    You'll be given a string of words, and your task is to count the number
    of boredoms. A boredom is a sentence that starts with the word "I".
    Sentences are delimited by '.', '?' or '!'.
   
    For example:
    >>> is_bored("Hello world")
    0
    >>> is_bored("The sky is blue. The sun is shining. I love this weather")
    1
    """

    import re
    sentences = re.split(r'[.?!]\s*', S)
    return sum(sentence[0:2] == 'I ' for sentence in sentences)


# Generated test cases:
import pytest
import re

def is_bored(S):
    sentences = re.split(r'[.?!]\s*', S)
    return sum(sentence[0:2] == 'I ' for sentence in sentences if len(sentence) >= 2)

def test_empty_string():
    assert is_bored("") == 0

def test_single_sentence_starting_with_i():
    assert is_bored("I am happy.") == 1

def test_single_sentence_not_starting_with_i():
    assert is_bored("You are happy.") == 0

def test_multiple_sentences_all_starting_with_i():
    assert is_bored("I am happy. I like coding. I enjoy testing.") == 3

def test_multiple_sentences_none_starting_with_i():
    assert is_bored("You are happy. She likes coding. They enjoy testing.") == 0

def test_mixed_sentences():
    assert is_bored("I am happy. You are sad. I like coding.") == 2

def test_different_punctuation():
    assert is_bored("I am happy! I like coding? I enjoy testing.") == 3

def test_no_space_after_punctuation():
    assert is_bored("I am happy.I like coding!I enjoy testing?") == 3

def test_multiple_spaces_after_punctuation():
    assert is_bored("I am happy.   I like coding!    I enjoy testing?") == 3

def test_sentence_starting_with_lowercase_i():
    assert is_bored("i am happy. I like coding.") == 1

def test_sentence_starting_with_i_but_no_space():
    assert is_bored("Iamhappy. I like coding.") == 1

def test_only_punctuation():
    assert is_bored("...!!!???") == 0

def test_sentence_with_only_i():
    assert is_bored("I. You. I!") == 0

def test_sentence_shorter_than_two_characters():
    assert is_bored("I. A. B.") == 0

def test_whitespace_only_sentences():
    assert is_bored("I am happy.   . I like coding.") == 2

def test_sentences_ending_without_punctuation():
    assert is_bored("I am happy. I like coding") == 2

@pytest.mark.parametrize("input_str,expected", [
    ("", 0),
    ("I am bored.", 1),
    ("You are bored.", 0),
    ("I am bored. I am tired.", 2),
    ("I am bored! Are you bored? I think so.", 2),
    ("Hello world. I am here. How are you? I am fine.", 2),
    ("I! I? I.", 0),
    ("i am here. I AM HERE.", 1),
    ("I", 0),
    (".", 0)
])
def test_parametrized_cases(input_str, expected):
    assert is_bored(input_str) == expected

def test_special_characters_in_sentences():
    assert is_bored("I have $100. I bought @home. I use #hashtag.") == 3

def test_numbers_in_sentences():
    assert is_bored("I have 5 cats. You have 3 dogs. I like 123.") == 2

def test_consecutive_punctuation():
    assert is_bored("I am happy... I am sad!!! I am okay???") == 3

def test_mixed_case_after_i():
    assert is_bored("I Am Happy. I am Sad. I aM oKaY.") == 3