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

def test_solve_empty_string():
    assert solve("") == ""

def test_solve_no_letters():
    assert solve("1234") == "4321"
    assert solve("!@#$") == "$#@!"

def test_solve_all_lowercase():
    assert solve("hello") == "HELLO"

def test_solve_all_uppercase():
    assert solve("WORLD") == "world"

def test_solve_mixed_case():
    assert solve("aBc") == "AbC"

def test_solve_alphanumeric():
    assert solve("a1B2c3") == "A1b2C3"

def test_solve_special_characters():
    assert solve("#a@C") == "#A@c"

def test_solve_unicode_letters():
    assert solve("áÉ") == "ÁéÉ"

@pytest.mark.parametrize("input_str,expected", [
    ("", ""),
    ("1234", "4321"),
    ("hello", "HELLO"),
    ("WORLD", "world"),
    ("aBc", "AbC"),
    ("a1B2c3", "A1b2C3"),
    ("#a@C", "#A@c"),
    ("áÉ", "ÁéÉ")
])
def test_solve_parametrized(input_str, expected):
    assert solve(input_str) == expected