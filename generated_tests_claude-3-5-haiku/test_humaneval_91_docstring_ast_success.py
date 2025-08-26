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
    return sum(sentence[0:2] == 'I ' for sentence in sentences)

def test_is_bored_no_boredom():
    assert is_bored("Hello world") == 0

def test_is_bored_single_boredom():
    assert is_bored("The sky is blue. I love this weather") == 1

def test_is_bored_multiple_boredoms():
    assert is_bored("I am bored. The day is long. I want to go home!") == 2

def test_is_bored_mixed_punctuation():
    assert is_bored("Hello! I am tired. What's up? I need a break.") == 2

def test_is_bored_empty_string():
    assert is_bored("") == 0

def test_is_bored_only_boredom():
    assert is_bored("I am so bored.") == 1

def test_is_bored_case_sensitive():
    assert is_bored("i am not bored. I am bored.") == 1

@pytest.mark.parametrize("input_string,expected", [
    ("Hello world", 0),
    ("I am bored.", 1),
    ("The sky is blue. I love this weather", 1),
    ("I am bored! I want to go home. Nothing to do.", 2),
    ("", 0),
    ("i am not bored. I am bored.", 1)
])
def test_is_bored_parametrized(input_string, expected):
    assert is_bored(input_string) == expected
