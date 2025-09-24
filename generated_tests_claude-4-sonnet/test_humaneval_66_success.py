# Test cases for HumanEval/66
# Generated using Claude API


def digitSum(s):
    """Task
    Write a function that takes a string as input and returns the sum of the upper characters only'
    ASCII codes.

    Examples:
        digitSum("") => 0
        digitSum("abAB") => 131
        digitSum("abcCd") => 67
        digitSum("helloE") => 69
        digitSum("woArBld") => 131
        digitSum("aAaaaXa") => 153
    """

    if s == "": return 0
    return sum(ord(char) if char.isupper() else 0 for char in s)


# Generated test cases:
import pytest

def digitSum(s):
    if s == "": return 0
    return sum(ord(char) if char.isupper() else 0 for char in s)

class TestDigitSum:
    
    def test_empty_string(self):
        assert digitSum("") == 0
    
    def test_single_uppercase_letter(self):
        assert digitSum("A") == 65
        assert digitSum("Z") == 90
        assert digitSum("B") == 66
    
    def test_single_lowercase_letter(self):
        assert digitSum("a") == 0
        assert digitSum("z") == 0
        assert digitSum("m") == 0
    
    def test_single_digit(self):
        assert digitSum("0") == 0
        assert digitSum("5") == 0
        assert digitSum("9") == 0
    
    def test_single_special_character(self):
        assert digitSum("!") == 0
        assert digitSum("@") == 0
        assert digitSum("#") == 0
        assert digitSum(" ") == 0
    
    def test_all_uppercase_letters(self):
        assert digitSum("ABC") == 65 + 66 + 67
        assert digitSum("HELLO") == 72 + 69 + 76 + 76 + 79
        assert digitSum("XYZ") == 88 + 89 + 90
    
    def test_all_lowercase_letters(self):
        assert digitSum("abc") == 0
        assert digitSum("hello") == 0
        assert digitSum("xyz") == 0
    
    def test_mixed_case_letters(self):
        assert digitSum("Hello") == 72
        assert digitSum("HeLLo") == 72 + 76 + 76
        assert digitSum("PyThOn") == 80 + 84 + 79
    
    def test_letters_with_digits(self):
        assert digitSum("A1B2C3") == 65 + 66 + 67
        assert digitSum("hello123WORLD") == 87 + 79 + 82 + 76 + 68
        assert digitSum("123abc456DEF") == 68 + 69 + 70
    
    def test_letters_with_special_characters(self):
        assert digitSum("A!B@C#") == 65 + 66 + 67
        assert digitSum("Hello, World!") == 72 + 87
        assert digitSum("TEST-case_123") == 84 + 69 + 83 + 84
    
    def test_only_digits(self):
        assert digitSum("123456") == 0
        assert digitSum("0") == 0
        assert digitSum("999") == 0
    
    def test_only_special_characters(self):
        assert digitSum("!@#$%^&*()") == 0
        assert digitSum("   ") == 0
        assert digitSum(".,;:") == 0
    
    def test_whitespace_with_letters(self):
        assert digitSum(" A B C ") == 65 + 66 + 67
        assert digitSum("Hello World") == 72 + 87
        assert digitSum("\tTEST\n") == 84 + 69 + 83 + 84
    
    @pytest.mark.parametrize("input_str,expected", [
        ("", 0),
        ("a", 0),
        ("A", 65),
        ("aA", 65),
        ("Aa", 65),
        ("ABC", 198),
        ("abc", 0),
        ("123", 0),
        ("A1a", 65),
        ("Hello World!", 72 + 87),
        ("PYTHON", 80 + 89 + 84 + 72 + 79 + 78),
        ("python", 0),
        ("PyThOn123", 80 + 84 + 79),
    ])
    def test_parametrized_cases(self, input_str, expected):
        assert digitSum(input_str) == expected
    
    def test_unicode_characters(self):
        assert digitSum("café") == 0
        assert digitSum("CAFÉ") == 67 + 65 + 70 + 201
        assert digitSum("αβγ") == 0
    
    def test_long_string(self):
        long_lower = "a" * 1000
        assert digitSum(long_lower) == 0
        
        long_upper = "A" * 100
        assert digitSum(long_upper) == 65 * 100
    
    def test_alternating_case(self):
        assert digitSum("AbCdEfGh") == 65 + 67 + 69 + 71
        assert digitSum("aBcDeFgH") == 66 + 68 + 70 + 72