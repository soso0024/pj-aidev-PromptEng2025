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
    ("1234", "4321"),
    ("ab", "AB"),
    ("#a@C", "#A@c"),
    ("", ""),
    ("a", "A"),
    ("Z", "z"),
    ("hello", "HELLO"),
    ("WORLD", "world"),
    ("HeLLo", "hEllO"),
    ("123", "321"),
    ("!@#$%", "%$#@!"),
    ("a1b2c3", "A1B2C3"),
    ("!@#a$%^", "!@#A$%^"),
    ("123abc456", "123ABC456"),
    ("MiXeD123CaSe", "mIxEd123cAsE"),
    ("   ", "   "),
    ("!@#", "#@!"),
    ("0", "0"),
    ("aB1cD2", "Ab1Cd2"),
    ("NoLetters123!@#", "nOlETTERS123!@#"),
    ("12345", "54321"),
    ("!@#$%^&*()", ")(*&^%$#@!"),
    ("a", "A"),
    ("A", "a"),
    ("aA", "Aa"),
    ("1a2B3c", "1A2b3C"),
    ("aBc123XyZ", "AbC123xYz")
])
def test_solve(input_str, expected):
    assert solve(input_str) == expected

def test_solve_empty_string():
    assert solve("") == ""

def test_solve_only_numbers():
    assert solve("987654321") == "123456789"

def test_solve_only_special_chars():
    assert solve("!@#$%^&*()") == ")(*&^%$#@!"

def test_solve_single_letter_lower():
    assert solve("x") == "X"

def test_solve_single_letter_upper():
    assert solve("Y") == "y"

def test_solve_single_number():
    assert solve("5") == "5"

def test_solve_single_special_char():
    assert solve("!") == "!"

def test_solve_mixed_with_spaces():
    assert solve("a B c") == "A b C"

def test_solve_only_spaces():
    assert solve("   ") == "   "
