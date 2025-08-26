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
        return s[::-1]
    return s

def test_solve_lowercase_to_uppercase():
    assert solve("ab") == "AB"

def test_solve_uppercase_to_lowercase():
    assert solve("AB") == "ab"

def test_solve_mixed_case_string():
    assert solve("#a@C") == "#A@c"

def test_solve_no_letters_string():
    assert solve("1234") == "4321"

def test_solve_empty_string():
    assert solve("") == ""

def test_solve_all_symbols():
    assert solve("!@#$%^") == "^%$#@!"

def test_solve_mixed_alphanumeric():
    assert solve("a1B2c3") == "A1b2C3"

def test_solve_unicode_letters():
    assert solve("áÉ") == "ÁéÉ"

@pytest.mark.parametrize("input_str,expected", [
    ("ab", "AB"),
    ("AB", "ab"),
    ("#a@C", "#A@c"),
    ("1234", "4321"),
    ("", ""),
    ("!@#$%^", "^%$#@!"),
    ("a1B2c3", "A1b2C3"),
    ("áÉ", "ÁéÉ")
])
def test_solve_parametrized(input_str, expected):
    assert solve(input_str) == expected