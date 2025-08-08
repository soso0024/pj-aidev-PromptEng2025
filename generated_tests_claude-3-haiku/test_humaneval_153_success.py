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

def test_strongest_extension_normal_case():
    assert Strongest_Extension('MyClass', ['MyExt', 'MyOtherExt']) == 'MyClass.MyExt'
    assert Strongest_Extension('AnotherClass', ['MYEXT', 'myext']) == 'AnotherClass.MYEXT'

def test_strongest_extension_empty_extensions():
    with pytest.raises(IndexError):
        Strongest_Extension('MyClass', [])

def test_strongest_extension_single_extension():
    assert Strongest_Extension('MyClass', ['MyExt']) == 'MyClass.MyExt'

@pytest.mark.parametrize("class_name,extensions,expected", [
    ('MyClass', ['MyExt', 'MYEXT', 'myext'], 'MyClass.MYEXT'),
    ('AnotherClass', ['UPPERCASE', 'lowercase', 'MixedCase'], 'AnotherClass.UPPERCASE'),
    ('TestClass', ['TEST', 'tEST', 'TeSt'], 'TestClass.TEST')
])
def test_strongest_extension_multiple_cases(class_name, extensions, expected):
    assert Strongest_Extension(class_name, extensions) == expected

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
