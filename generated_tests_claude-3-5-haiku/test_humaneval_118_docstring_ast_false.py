# Test cases for HumanEval/118
# Generated using Claude API


def get_closest_vowel(word):
    """You are given a word. Your task is to find the closest vowel that stands between 
    two consonants from the right side of the word (case sensitive).
    
    Vowels in the beginning and ending doesn't count. Return empty string if you didn't
    find any vowel met the above condition. 

    You may assume that the given string contains English letter only.

    Example:
    get_closest_vowel("yogurt") ==> "u"
    get_closest_vowel("FULL") ==> "U"
    get_closest_vowel("quick") ==> ""
    get_closest_vowel("ab") ==> ""
    """

    if len(word) < 3:
        return ""

    vowels = {"a", "e", "i", "o", "u", "A", "E", 'O', 'U', 'I'}
    for i in range(len(word)-2, 0, -1):
        if word[i] in vowels:
            if (word[i+1] not in vowels) and (word[i-1] not in vowels):
                return word[i]
    return ""


# Generated test cases:
import pytest

def get_closest_vowel(word):
    if len(word) < 3:
        return ""

    vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
    for i in range(len(word)-2, 0, -1):
        if word[i] in vowels:
            if (word[i+1] not in vowels) and (word[i-1] not in vowels):
                return word[i]
    return ""

def test_get_closest_vowel_normal_cases():
    assert get_closest_vowel("yogurt") == "u"
    assert get_closest_vowel("FULL") == "U"
    assert get_closest_vowel("quick") == ""

def test_get_closest_vowel_edge_cases():
    assert get_closest_vowel("ab") == ""
    assert get_closest_vowel("") == ""
    assert get_closest_vowel("a") == ""
    assert get_closest_vowel("ab") == ""

@pytest.mark.parametrize("word,expected", [
    ("concert", "e"),
    ("rhythm", ""),
    ("strength", ""),
    ("aeiou", ""),
    ("xAx", ""),
    ("bEAb", "E"),
    ("rAdAr", "A")
])
def test_get_closest_vowel_parametrized(word, expected):
    assert get_closest_vowel(word) == expected

def test_get_closest_vowel_multiple_vowels():
    assert get_closest_vowel("chocolate") == "a"
    assert get_closest_vowel("beautiful") == "u"

def test_get_closest_vowel_case_sensitivity():
    assert get_closest_vowel("bAcOn") == "A"
    assert get_closest_vowel("cOdE") == "O"