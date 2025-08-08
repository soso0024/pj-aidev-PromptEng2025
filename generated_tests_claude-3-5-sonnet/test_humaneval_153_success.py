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

@pytest.mark.parametrize("class_name,extensions,expected", [
    ("Strength", ["Extension", "EXTENSION", "ExTENsion"], "Strength.EXTENSION"),
    ("Example", ["abc", "ABC", "AbC"], "Example.ABC"),
    ("Test", ["aaa", "bbb", "CCC"], "Test.CCC"),
    ("Class", ["", "A", "a"], "Class.A"),
    ("Sample", ["abcDEF", "ABCdef", "AbCdEf"], "Sample.abcDEF"),
    ("Demo", ["A1B2C3", "a1b2c3", "A1B2c3"], "Demo.A1B2C3"),
    ("Mix", ["aBcDeF", "AbCdEf", "ABCDEF"], "Mix.ABCDEF"),
    ("Case", ["lower", "UPPER", "MiXeD"], "Case.UPPER"),
    ("Special", ["@#$ABC", "123abc", "XYZ!!!"], "Special.@#$ABC"),
    ("Empty", ["a", "A", ""], "Empty.A")
])
def test_strongest_extension(class_name, extensions, expected):
    assert Strongest_Extension(class_name, extensions) == expected

def test_single_extension():
    assert Strongest_Extension("Test", ["ABC"]) == "Test.ABC"

def test_same_case_count():
    assert Strongest_Extension("Test", ["aA", "Aa"]) == "Test.aA"

def test_numbers_and_special_chars():
    assert Strongest_Extension("Test", ["A1@B", "a1@b"]) == "Test.A1@B"

def test_all_special_chars():
    assert Strongest_Extension("Test", ["@#$", "123", "!!!"]) == "Test.@#$"

def test_empty_class_name():
    assert Strongest_Extension("", ["ABC"]) == ".ABC"
