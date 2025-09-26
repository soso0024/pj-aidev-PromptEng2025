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

@pytest.mark.parametrize("word,expected", [
    ("yogurt", "u"),
    ("FULL", "U"),
    ("quick", ""),
    ("ab", ""),
    ("", ""),
    ("a", ""),
    ("ab", ""),
    ("abc", ""),
    ("aei", ""),
    ("consonant", "o"),
    ("beautiful", "i"),
    ("BEAUTIFUL", "I"),
    ("strength", "e"),
    ("rhythm", ""),
    ("bcdfg", ""),
    ("aeiou", ""),
    ("bcd", ""),
    ("bad", ""),
    ("bed", ""),
    ("bid", ""),
    ("bod", ""),
    ("bud", ""),
    ("BAD", ""),
    ("BED", ""),
    ("BID", ""),
    ("BOD", ""),
    ("BUD", ""),
    ("table", "a"),
    ("TABLE", "A"),
    ("simple", "i"),
    ("SIMPLE", "I"),
    ("bottle", "o"),
    ("BOTTLE", "O"),
    ("purple", "u"),
    ("PURPLE", "U"),
    ("center", "e"),
    ("CENTER", "E"),
    ("computer", "u"),
    ("COMPUTER", "U"),
    ("problem", "o"),
    ("PROBLEM", "O"),
    ("student", "u"),
    ("STUDENT", "U"),
    ("teacher", "a"),
    ("TEACHER", "A"),
    ("picture", "u"),
    ("PICTURE", "U"),
    ("example", "a"),
    ("EXAMPLE", "A"),
    ("important", "a"),
    ("IMPORTANT", "A"),
    ("different", "e"),
    ("DIFFERENT", "E"),
    ("government", "e"),
    ("GOVERNMENT", "E"),
    ("development", "e"),
    ("DEVELOPMENT", "E"),
    ("management", "e"),
    ("MANAGEMENT", "E"),
    ("information", "o"),
    ("INFORMATION", "O"),
    ("organization", "o"),
    ("ORGANIZATION", "O"),
    ("communication", "o"),
    ("COMMUNICATION", "O"),
    ("administration", "o"),
    ("ADMINISTRATION", "O"),
    ("transportation", "o"),
    ("TRANSPORTATION", "O"),
    ("bac", ""),
    ("cab", ""),
    ("cba", ""),
    ("bcad", "a"),
    ("dcab", "a"),
    ("bcadef", "a"),
    ("fedcab", "a"),
    ("xyz", ""),
    ("XYZ", ""),
    ("qwrty", ""),
    ("QWRTY", ""),
    ("bcdfghjklmnpqrstvwxyz", ""),
    ("BCDFGHJKLMNPQRSTVWXYZ", ""),
    ("aeiouAEIOU", ""),
    ("baeiouAEIOUc", "U"),
    ("caeiouAEIOUb", "U"),
    ("baeiouc", "u"),
    ("caeioub", "u"),
    ("bAEIOUc", "U"),
    ("cAEIOUb", "U"),
    ("mixedCASE", "E"),
    ("MIXEDcase", "e"),
    ("tEsT", ""),
    ("TeSt", ""),
    ("programming", "a"),
    ("PROGRAMMING", "A"),
    ("function", "o"),
    ("FUNCTION", "O"),
    ("variable", "a"),
    ("VARIABLE", "A"),
    ("algorithm", "i"),
    ("ALGORITHM", "I"),
    ("structure", "u"),
    ("STRUCTURE", "U"),
    ("database", "a"),
    ("DATABASE", "A"),
    ("software", "a"),
    ("SOFTWARE", "A"),
    ("hardware", "a"),
    ("HARDWARE", "A"),
    ("network", "o"),
    ("NETWORK", "O"),
    ("security", "u"),
    ("SECURITY", "U"),
    ("application", "o"),
    ("APPLICATION", "O"),
    ("development", "e"),
    ("DEVELOPMENT", "E"),
    ("testing", "i"),
    ("TESTING", "I"),
    ("debugging", "i"),
    ("DEBUGGING", "I"),
    ("optimization", "o"),
    ("OPTIMIZATION", "O"),
    ("performance", "a"),
    ("PERFORMANCE", "A"),
    ("maintenance", "a"),
    ("MAINTENANCE", "A"),
    ("documentation", "o"),
    ("DOCUMENTATION", "O"),
    ("implementation", "o"),
    ("IMPLEMENTATION", "O"),
    ("configuration", "o"),
    ("CONFIGURATION", "O"),
    ("installation", "o"),
    ("INSTALLATION", "O"),
    ("integration", "o"),
    ("INTEGRATION", "O"),
    ("migration", "o"),
    ("MIGRATION", "O"),
    ("validation", "o"),
    ("VALIDATION", "O"),
    ("verification", "a"),
    ("VERIFICATION", "A"),
    ("authentication", "o"),
    ("AUTHENTICATION", "O"),
    ("authorization", "o"),
    ("AUTHORIZATION", "O"),
    ("encryption", "o"),
    ("ENCRYPTION", "O"),
    ("decryption", "o"),
    ("DECRYPTION", "O"),
    ("compression", "o"),
    ("COMPRESSION", "O"),
    ("decompression", "o"),
    ("DECOMPRESSION", "O"),
    ("serialization", "o"),
    ("SERIALIZATION", "O"),
    ("deserialization", "o"),
    ("DESERIALIZATION", "O"),
    ("synchronization", "o"),
    ("SYNCHRONIZATION", "O"),
    ("asynchronization", "o"),
    ("ASYNCHRONIZATION", "O"),
    ("parallelization", "o"),
    ("PARALLELIZATION", "O"),
    ("optimization", "o"),
    ("OPTIMIZATION", "O"),
    ("minimization", "o"),
    ("MINIMIZATION", "O"),
    ("maximization", "o"),
    ("MAXIMIZATION", "O"),
    ("normalization", "o"),
    ("NORMALIZATION", "O"),
    ("standardization", "o"),
    ("STANDARDIZATION", "O"),
    ("generalization", "o"),
    ("GENERALIZATION", "O"),
    ("specialization", "o"),
    ("SPECIALIZATION", "O"),
    ("abstraction", "o"),
    ("ABSTRACTION", "O"),
    ("encapsulation", "o"),
    ("ENCAPSULATION", "O"),
    ("inheritance", "a"),
    ("INHERITANCE", "A"),
    ("polymorphism", "i"),
    ("POLYMORPHISM", "I"),
])
def test_get_closest_vowel(word, expected):
    assert get_closest_vowel(word) == expected

def test_get_closest_vowel_empty_string():
    assert get_closest_vowel("") == ""

def test_get_closest_vowel_single_char():
    assert get_closest_vowel("a") == ""
    assert get_closest_vowel("b") == ""
    assert get_closest_vowel("A") == ""
    assert get_closest_vowel("B") == ""

def test_get_closest_vowel_two_chars():
    assert get_closest_vowel("ab") == ""
    assert get_closest_vowel("ba")
