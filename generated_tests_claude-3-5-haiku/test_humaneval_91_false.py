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

def test_is_bored_empty_string():
    assert is_bored("") == 0

def test_is_bored_no_boredom():
    assert is_bored("Hello world. This is a test.") == 0

def test_is_bored_single_boredom():
    assert is_bored("The sky is blue. I am bored.") == 1

def test_is_bored_multiple_boredoms():
    assert is_bored("I am bored. This is fun. I want to go home.") == 2

def test_is_bored_mixed_sentences():
    assert is_bored("Hello world. I am bored! Something else. I want to sleep?") == 2

def test_is_bored_case_sensitive():
    assert is_bored("i am not bored. I am bored.") == 1

def test_is_bored_whitespace():
    assert is_bored("   I am bored.   Other sentence.") == 1