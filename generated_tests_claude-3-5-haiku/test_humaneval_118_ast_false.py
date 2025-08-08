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

    vowels = {"a", "e", "i", "o", "u", "A", "E", 'O', 'U', 'I'}
    for i in range(len(word)-2, 0, -1):
        if word[i] in vowels:
            if (word[i+1] not in vowels) and (word[i-1] not in vowels):
                return word[i]
    return ""

def test_get_closest_vowel_short_word():
    assert get_closest_vowel("hi") == ""
    assert get_closest_vowel("a") == ""
    assert get_closest_vowel("") == ""

def test_get_closest_vowel_no_valid_vowel():
    assert get_closest_vowel("xyz") == ""
    assert get_closest_vowel("bcd") == ""

def test_get_closest_vowel_single_valid_vowel():
    assert get_closest_vowel("rate") == "a"
    assert get_closest_vowel("bite") == "i"
    assert get_closest_vowel("note") == "o"

def test_get_closest_vowel_multiple_valid_vowels():
    assert get_closest_vowel("create") == "e"
    assert get_closest_vowel("absolute") == "o"

def test_get_closest_vowel_case_sensitivity():
    assert get_closest_vowel("rAtE") == "A"
    assert get_closest_vowel("bItE") == "I"

@pytest.mark.parametrize("word,expected", [
    ("rate", "a"),
    ("bite", "i"),
    ("note", "o"),
    ("create", "e"),
    ("absolute", "o"),
    ("xyz", ""),
    ("hi", ""),
    ("rAtE", "A"),
    ("bItE", "I")
])
def test_get_closest_vowel_parametrized(word, expected):
    assert get_closest_vowel(word) == expected