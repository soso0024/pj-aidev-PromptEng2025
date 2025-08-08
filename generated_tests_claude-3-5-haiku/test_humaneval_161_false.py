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

def test_solve_basic_alphabetic_swap():
    assert solve("Hello") == "hELLO"

def test_solve_mixed_case_swap():
    assert solve("HeLLo") == "hEllO"

def test_solve_no_alphabetic_chars():
    assert solve("123!@#") == "321!@#"

def test_solve_empty_string():
    assert solve("") == ""

def test_solve_single_char_uppercase():
    assert solve("A") == "a"

def test_solve_single_char_lowercase():
    assert solve("a") == "A"

def test_solve_complex_string():
    assert solve("Hello123World!") == "hELLO123wORLD!"

@pytest.mark.parametrize("input_str,expected", [
    ("Hello", "hELLO"),
    ("HeLLo", "hEllO"),
    ("123!@#", "321!@#"),
    ("", ""),
    ("A", "a"),
    ("a", "A"),
    ("Hello123World!", "hELLO123wORLD!")
])
def test_solve_parametrized(input_str, expected):
    assert solve(input_str) == expected