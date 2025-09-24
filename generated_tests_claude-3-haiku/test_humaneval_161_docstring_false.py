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
    s = "".join(new_str)
    if flg == 0:
        return s[::-1]
    return s

@pytest.mark.parametrize("input_str,expected", [
    ("1234", "4321"),
    ("ab", "AB"),
    ("#a@C", "#A@c"),
    ("HELLO WORLD", "hELLO wORLD"),
    ("123abc456", "123ABC456"),
    ("", ""),
    (" ", " "),
    ("123 ABC 456", "123 aBC 456")
])
def test_solve(input_str, expected):
    assert solve(input_str) == expected

def test_solve_empty_string():
    assert solve("") == ""

def test_solve_all_non_alphabetic():
    assert solve("1234567890!@#$%^&*()_+") == "0987654321!@#$%^&*()_+"

def test_solve_mixed_case():
    assert solve("aBcDeFgHiJkLmNoPqRsTuVwXyZ") == "AbCdEfGhIjKlMnOpQrStUvWxYz"