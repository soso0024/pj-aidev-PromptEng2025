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

def test_strongest_extension_basic():
    assert Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'

def test_strongest_extension_mixed_case():
    assert Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']) == 'Slices.SErviNGSliCes'

def test_strongest_extension_equal_strength():
    assert Strongest_Extension('Test', ['AB', 'AB']) == 'Test.AB'

def test_strongest_extension_all_lowercase():
    assert Strongest_Extension('Class', ['ab', 'cd', 'ef']) == 'Class.ab'

def test_strongest_extension_all_uppercase():
    assert Strongest_Extension('Class', ['AB', 'CD', 'EF']) == 'Class.AB'

def test_strongest_extension_empty_list():
    with pytest.raises(IndexError):
        Strongest_Extension('Class', [])

def test_strongest_extension_single_character():
    assert Strongest_Extension('Test', ['A', 'b', 'C']) == 'Test.A'

def test_strongest_extension_complex_names():
    assert Strongest_Extension('MyClass', ['HelloWORLD', 'goodBYE', 'MixedCASE']) == 'MyClass.HelloWORLD'

def test_strongest_extension_numeric_chars():
    assert Strongest_Extension('Numbers', ['A1b2', 'C3d4', 'E5f6']) == 'Numbers.A1b2'

def test_strongest_extension_special_chars():
    assert Strongest_Extension('Special', ['A!b@', 'C#d$', 'E%f^']) == 'Special.A!b@'
