# Test cases for HumanEval/48
# Generated using Claude API



def is_palindrome(text: str):
    """
    Checks if given string is a palindrome
    >>> is_palindrome('')
    True
    >>> is_palindrome('aba')
    True
    >>> is_palindrome('aaaaa')
    True
    >>> is_palindrome('zbcd')
    False
    """

    for i in range(len(text)):
        if text[i] != text[len(text) - 1 - i]:
            return False
    return True


# Generated test cases:
import pytest

def is_palindrome(text: str):
    for i in range(len(text)):
        if text[i] != text[len(text) - 1 - i]:
            return False
    return True

class TestIsPalindrome:
    
    def test_empty_string(self):
        assert is_palindrome('') == True
    
    def test_single_character(self):
        assert is_palindrome('a') == True
        assert is_palindrome('z') == True
        assert is_palindrome('1') == True
    
    def test_two_character_palindrome(self):
        assert is_palindrome('aa') == True
        assert is_palindrome('bb') == True
    
    def test_two_character_non_palindrome(self):
        assert is_palindrome('ab') == False
        assert is_palindrome('xy') == False
    
    def test_odd_length_palindromes(self):
        assert is_palindrome('aba') == True
        assert is_palindrome('aaaaa') == True
        assert is_palindrome('racecar') == True
        assert is_palindrome('madam') == True
    
    def test_even_length_palindromes(self):
        assert is_palindrome('abba') == True
        assert is_palindrome('noon') == True
        assert is_palindrome('deed') == True
    
    def test_non_palindromes(self):
        assert is_palindrome('zbcd') == False
        assert is_palindrome('hello') == False
        assert is_palindrome('python') == False
        assert is_palindrome('abcde') == False
    
    def test_numeric_strings(self):
        assert is_palindrome('121') == True
        assert is_palindrome('12321') == True
        assert is_palindrome('123') == False
    
    def test_mixed_alphanumeric(self):
        assert is_palindrome('a1a') == True
        assert is_palindrome('1a1') == True
        assert is_palindrome('a1b') == False
    
    def test_special_characters(self):
        assert is_palindrome('!@!') == True
        assert is_palindrome('!@#') == False
        assert is_palindrome('a!a') == True
    
    def test_case_sensitive(self):
        assert is_palindrome('Aa') == False
        assert is_palindrome('AaA') == True
        assert is_palindrome('AbA') == True
    
    def test_whitespace(self):
        assert is_palindrome(' ') == True
        assert is_palindrome('   ') == True
        assert is_palindrome('a a') == True
        assert is_palindrome('a b') == False
    
    @pytest.mark.parametrize("text,expected", [
        ('', True),
        ('a', True),
        ('aba', True),
        ('aaaaa', True),
        ('zbcd', False),
        ('racecar', True),
        ('hello', False),
        ('noon', True),
        ('12321', True),
        ('123', False)
    ])
    def test_parametrized_cases(self, text, expected):
        assert is_palindrome(text) == expected