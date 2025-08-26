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

def test_solve_empty_string():
    assert solve("") == ""

def test_solve_no_letters():
    assert solve("1234") == "4321"
    assert solve("!@#$") == "$#@!"

def test_solve_all_letters_lowercase():
    assert solve("abc") == "ABC"

def test_solve_all_letters_uppercase():
    assert solve("XYZ") == "xyz"

def test_solve_mixed_case_letters():
    assert solve("aBc") == "AbC"

def test_solve_letters_with_numbers():
    assert solve("a1B2c") == "A1b2C"

def test_solve_letters_with_special_characters():
    assert solve("#a@C") == "#A@c"

def test_solve_complex_string():
    assert solve("Hello, World! 123") == "hELLO, wORLD! 123"

@pytest.mark.parametrize("input_str,expected", [
    ("", ""),
    ("1234", "4321"),
    ("abc", "ABC"),
    ("XYZ", "xyz"),
    ("aBc", "AbC"),
    ("a1B2c", "A1b2C"),
    ("#a@C", "#A@c"),
    ("Hello, World! 123", "hELLO, wORLD! 123")
])
def test_solve_parametrized(input_str, expected):
    assert solve(input_str) == expected
