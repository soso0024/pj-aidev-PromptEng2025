# Test cases for HumanEval/161
# Generated using Claude API


def solve(s):
    """You are given a string s.
    if s[i] is a letter, reverse its case from lower to upper or vise versa, 
    otherwise keep it as it is.
    If the string contains no letters, reverse the string.
    The function should return the resulted string.
    Examples
    solve("1234") = "4321"
    solve("ab") = "AB"
    solve("#a@C") = "#A@c"
    """

    flg = 0
    idx = 0
    new_str = list(s)
    for i in s:
        if i.isalpha():
            new_str[idx] = i.swapcase()
            flg = 1
        idx += 1
    s = ""
    for i in new_str:
        s += i
    if flg == 0:
        return s[len(s)::-1]
    return s


# Generated test cases:
import pytest

def solve(s):
    flg = 0
    idx = 0
    new_str = list(s)
    for i in s:
        if i.isalpha():
            new_str[idx] = i.swapcase()
            flg = 1
        idx += 1
    s = ""
    for i in new_str:
        s += i
    if flg == 0:
        return s[len(s)::-1]
    return s

@pytest.mark.parametrize("input_str,expected", [
    ("hello", "HELLO"),
    ("WORLD", "world"),
    ("Hello", "hELLO"),
    ("HeLLo", "hEllO"),
    ("abc", "ABC"),
    ("XYZ", "xyz"),
    ("", ""),
    ("123", "321"),
    ("!@#", "!@#"[::-1]),
    ("12345", "54321"),
    ("!@#$%", "%$#@!"),
    ("hello123", "HELLO123"),
    ("123world", "123WORLD"),
    ("Hello123World", "hELLO123wORLD"),
    ("a", "A"),
    ("Z", "z"),
    ("1", "1"),
    ("!", "!"),
    ("a1b2c3", "A1B2C3"),
    ("A1B2C3", "a1b2c3"),
    ("MiXeD123!@#", "mIxEd123!@#"),
    ("   ", "   "),
    ("a b c", "A B C"),
    ("A B C", "a b c"),
    ("123 456", "654 321"),
    ("hello world", "HELLO WORLD"),
    ("HELLO WORLD", "hello world"),
    ("Test123!@#Test", "tEST123!@#tEST"),
    ("!@#123", "321#@!"),
    ("abc!@#123", "ABC!@#123"),
    ("123!@#abc", "123!@#ABC"),
    ("aB1cD2eF3", "Ab1Cd2Ef3"),
    ("1a2B3c", "1A2b3C"),
    ("NoLetters123!@#", "nOlETTERS123!@#"),
    ("OnlyNumbers12345", "oNLYnUMBERS12345"),
    ("SpecialChars!@#$%^&*()", "sPECIALcHARS!@#$%^&*()"),
])
def test_solve(input_str, expected):
    assert solve(input_str) == expected

def test_solve_empty_string():
    assert solve("") == ""

def test_solve_only_numbers():
    assert solve("12345") == "54321"

def test_solve_only_special_chars():
    assert solve("!@#$%") == "%$#@!"

def test_solve_single_letter():
    assert solve("a") == "A"
    assert solve("Z") == "z"

def test_solve_single_non_letter():
    assert solve("1") == "1"
    assert solve("!") == "!"

def test_solve_mixed_case():
    result = solve("AbCdEf")
    expected = "aBcDeF"
    assert result == expected

def test_solve_whitespace_only():
    assert solve("   ") == "   "
    assert solve("\t\n") == "\n\t"

def test_solve_unicode_letters():
    assert solve("café") == "CAFÉ"
    assert solve("CAFÉ") == "café"
