# Test cases for HumanEval/153
# Generated using Claude API


def Strongest_Extension(class_name, extensions):
    """You will be given the name of a class (a string) and a list of extensions.
    The extensions are to be used to load additional classes to the class. The
    strength of the extension is as follows: Let CAP be the number of the uppercase
    letters in the extension's name, and let SM be the number of lowercase letters 
    in the extension's name, the strength is given by the fraction CAP - SM. 
    You should find the strongest extension and return a string in this 
    format: ClassName.StrongestExtensionName.
    If there are two or more extensions with the same strength, you should
    choose the one that comes first in the list.
    For example, if you are given "Slices" as the class and a list of the
    extensions: ['SErviNGSliCes', 'Cheese', 'StuFfed'] then you should
    return 'Slices.SErviNGSliCes' since 'SErviNGSliCes' is the strongest extension 
    (its strength is -1).
    Example:
    for Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'
    """

    strong = extensions[0]
    my_val = len([x for x in extensions[0] if x.isalpha() and x.isupper()]) - len([x for x in extensions[0] if x.isalpha() and x.islower()])
    for s in extensions:
        val = len([x for x in s if x.isalpha() and x.isupper()]) - len([x for x in s if x.isalpha() and x.islower()])
        if val > my_val:
            strong = s
            my_val = val

    ans = class_name + "." + strong
    return ans



# Generated test cases:
import pytest

def Strongest_Extension(class_name, extensions):
    strong = extensions[0]
    my_val = len([x for x in extensions[0] if x.isalpha() and x.isupper()]) - len([x for x in extensions[0] if x.isalpha() and x.islower()])
    for s in extensions:
        val = len([x for x in s if x.isalpha() and x.isupper()]) - len([x for x in s if x.isalpha() and x.islower()])
        if val > my_val:
            strong = s
            my_val = val

    ans = class_name + "." + strong
    return ans

def test_basic_functionality():
    assert Strongest_Extension("MyClass", ["ext1", "EXT2"]) == "MyClass.EXT2"

def test_single_extension():
    assert Strongest_Extension("Test", ["abc"]) == "Test.abc"

def test_all_uppercase():
    assert Strongest_Extension("Class", ["ABC", "DEF", "GHI"]) == "Class.ABC"

def test_all_lowercase():
    assert Strongest_Extension("Class", ["abc", "def", "ghi"]) == "Class.abc"

def test_mixed_case():
    assert Strongest_Extension("MyClass", ["AbC", "dEf", "GhI"]) == "MyClass.AbC"

def test_with_numbers():
    assert Strongest_Extension("Test", ["abc123", "DEF456"]) == "Test.DEF456"

def test_with_special_characters():
    assert Strongest_Extension("Class", ["a@b#c", "D$E%F"]) == "Class.D$E%F"

def test_equal_strength_first_wins():
    assert Strongest_Extension("Test", ["Ab", "Cd", "Ef"]) == "Test.Ab"

def test_negative_strength():
    assert Strongest_Extension("Class", ["abc", "def"]) == "Class.abc"

def test_zero_strength():
    assert Strongest_Extension("Test", ["123", "456"]) == "Test.123"

def test_empty_extensions():
    assert Strongest_Extension("Class", [""]) == "Class."

def test_multiple_empty_extensions():
    assert Strongest_Extension("Test", ["", "", ""]) == "Test."

def test_complex_mixed():
    assert Strongest_Extension("MyClass", ["aB1c", "D2eF", "g3H4i"]) == "MyClass.D2eF"

@pytest.mark.parametrize("class_name,extensions,expected", [
    ("A", ["x"], "A.x"),
    ("B", ["X"], "B.X"),
    ("C", ["aA"], "C.aA"),
    ("D", ["Aa"], "D.Aa"),
    ("E", ["aaa", "AAA"], "E.AAA"),
    ("F", ["AAA", "aaa"], "F.AAA"),
    ("G", ["123abc", "456DEF"], "G.456DEF"),
    ("H", ["!@#abc", "!@#DEF"], "H.!@#DEF")
])
def test_parametrized_cases(class_name, extensions, expected):
    assert Strongest_Extension(class_name, extensions) == expected

def test_long_class_name():
    assert Strongest_Extension("VeryLongClassName", ["ext"]) == "VeryLongClassName.ext"

def test_long_extension():
    long_ext = "a" * 100 + "B" * 50
    assert Strongest_Extension("Test", [long_ext]) == f"Test.{long_ext}"

def test_unicode_characters():
    assert Strongest_Extension("Class", ["αβγ", "ΑΒΓ"]) == "Class.ΑΒΓ"

def test_strength_calculation():
    result = Strongest_Extension("Test", ["AAAaaa", "AAaa", "Aaa"])
    assert result == "Test.AAAaaa"

def test_tie_breaking():
    assert Strongest_Extension("Class", ["Aa", "Bb", "Cc"]) == "Class.Aa"

def test_negative_vs_positive_strength():
    assert Strongest_Extension("Test", ["aaa", "A"]) == "Test.A"