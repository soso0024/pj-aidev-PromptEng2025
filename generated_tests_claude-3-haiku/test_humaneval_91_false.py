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
import re
import pytest

def is_bored(S):
    sentences = re.split(r'[.?!]\s*', S)
    return sum(sentence.strip().startswith('I ') for sentence in sentences)

def test_is_bored_empty_string():
    assert is_bored("") == 0

def test_is_bored_single_sentence():
    assert is_bored("I am bored.") == 1
    assert is_bored("I like to read.") == 1

def test_is_bored_multiple_sentences():
    assert is_bored("I am bored. I want to do something fun. I wish I had a hobby.") == 3
    assert is_bored("I like to read. I enjoy cooking. I play tennis on weekends.") == 3

def test_is_bored_mixed_case():
    assert is_bored("I AM bored. I like to READ.") == 2
    assert is_bored("i am bored. i want to do something fun.") == 2

def test_is_bored_punctuation():
    assert is_bored("I am bored! I want to do something fun?") == 2
    assert is_bored("I like to read. I enjoy cooking! I play tennis on weekends.") == 1

def test_is_bored_leading_whitespace():
    assert is_bored("  I am bored. I want to do something fun.") == 2
    assert is_bored("   I like to read. I enjoy cooking. I play tennis on weekends.") == 3

@pytest.mark.parametrize("input,expected", [
    ("I am bored. I want to do something fun.", 2),
    ("I like to read. I enjoy cooking. I play tennis on weekends.", 3),
    ("I AM bored. I like to READ.", 2),
    ("  I am bored! I want to do something fun?", 2),
    ("", 0)
])
def test_is_bored_parametrized(input, expected):
    assert is_bored(input) == expected