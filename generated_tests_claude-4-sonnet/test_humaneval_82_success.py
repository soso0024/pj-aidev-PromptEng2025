# Test cases for HumanEval/82
# Generated using Claude API


def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """

    l = len(string)
    if l == 0 or l == 1:
        return False
    for i in range(2, l):
        if l % i == 0:
            return False
    return True


# Generated test cases:
import pytest

def prime_length(string):
    l = len(string)
    if l == 0 or l == 1:
        return False
    for i in range(2, l):
        if l % i == 0:
            return False
    return True

@pytest.mark.parametrize("input_string,expected", [
    ("", False),
    ("a", False),
    ("ab", True),
    ("abc", True),
    ("abcd", False),
    ("abcde", True),
    ("abcdef", False),
    ("abcdefg", True),
    ("abcdefgh", False),
    ("abcdefghi", False),
    ("abcdefghij", False),
    ("abcdefghijk", True),
    ("abcdefghijkl", False),
    ("abcdefghijklm", True),
    ("abcdefghijklmn", False),
    ("abcdefghijklmno", False),
    ("abcdefghijklmnop", False),
    ("abcdefghijklmnopq", True),
    ("abcdefghijklmnopqr", False),
    ("abcdefghijklmnopqrs", True),
    ("abcdefghijklmnopqrst", False),
    ("x" * 23, True),
    ("x" * 29, True),
    ("x" * 31, True),
    ("x" * 37, True),
    ("x" * 41, True),
    ("x" * 43, True),
    ("x" * 47, True),
    ("x" * 4, False),
    ("x" * 6, False),
    ("x" * 8, False),
    ("x" * 9, False),
    ("x" * 10, False),
    ("x" * 12, False),
    ("x" * 14, False),
    ("x" * 15, False),
    ("x" * 16, False),
    ("x" * 18, False),
    ("x" * 20, False),
    ("x" * 21, False),
    ("x" * 22, False),
    ("x" * 24, False),
    ("x" * 25, False),
    ("x" * 26, False),
    ("x" * 27, False),
    ("x" * 28, False),
    ("x" * 30, False),
])
def test_prime_length_parametrized(input_string, expected):
    assert prime_length(input_string) == expected

def test_prime_length_empty_string():
    assert prime_length("") == False

def test_prime_length_single_character():
    assert prime_length("a") == False
    assert prime_length("1") == False
    assert prime_length(" ") == False

def test_prime_length_two_characters():
    assert prime_length("ab") == True
    assert prime_length("12") == True
    assert prime_length("  ") == True

def test_prime_length_three_characters():
    assert prime_length("abc") == True
    assert prime_length("123") == True
    assert prime_length("   ") == True

def test_prime_length_composite_numbers():
    assert prime_length("abcd") == False
    assert prime_length("abcdef") == False
    assert prime_length("abcdefgh") == False
    assert prime_length("abcdefghij") == False

def test_prime_length_special_characters():
    assert prime_length("!@") == True
    assert prime_length("!@#") == True
    assert prime_length("!@#$") == False
    assert prime_length("!@#$%") == True

def test_prime_length_mixed_content():
    assert prime_length("a1!") == True
    assert prime_length("a1!@") == False
    assert prime_length("a1!@#") == True

def test_prime_length_unicode():
    assert prime_length("αβ") == True
    assert prime_length("αβγ") == True
    assert prime_length("αβγδ") == False

def test_prime_length_whitespace():
    assert prime_length("a b") == True
    assert prime_length("a  b") == False
    assert prime_length("a   b") == True

def test_prime_length_newlines_and_tabs():
    assert prime_length("a\nb") == True
    assert prime_length("a\tb") == True
    assert prime_length("a\n\tb") == False
