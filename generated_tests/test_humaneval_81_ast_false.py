# Test cases for HumanEval/81
# Generated using Claude API


def numerical_letter_grade(grades):
    """It is the last week of the semester and the teacher has to give the grades
    to students. The teacher has been making her own algorithm for grading.
    The only problem is, she has lost the code she used for grading.
    She has given you a list of GPAs for some students and you have to write 
    a function that can output a list of letter grades using the following table:
             GPA       |    Letter grade
              4.0                A+
            > 3.7                A 
            > 3.3                A- 
            > 3.0                B+
            > 2.7                B 
            > 2.3                B-
            > 2.0                C+
            > 1.7                C
            > 1.3                C-
            > 1.0                D+ 
            > 0.7                D 
            > 0.0                D-
              0.0                E
    

    Example:
    grade_equation([4.0, 3, 1.7, 2, 3.5]) ==> ['A+', 'B', 'C-', 'C', 'A-']
    """


   
    letter_grade = []
    for gpa in grades:
        if gpa == 4.0:
            letter_grade.append("A+")
        elif gpa > 3.7:
            letter_grade.append("A")
        elif gpa > 3.3:
            letter_grade.append("A-")
        elif gpa > 3.0:
            letter_grade.append("B+")
        elif gpa > 2.7:
            letter_grade.append("B")
        elif gpa > 2.3:
            letter_grade.append("B-")
        elif gpa > 2.0:
            letter_grade.append("C+")
        elif gpa > 1.7:
            letter_grade.append("C")
        elif gpa > 1.3:
            letter_grade.append("C-")
        elif gpa > 1.0:
            letter_grade.append("D+")
        elif gpa > 0.7:
            letter_grade.append("D")
        elif gpa > 0.0:
            letter_grade.append("D-")
        else:
            letter_grade.append("E")
    return letter_grade


# Generated test cases:
import pytest

@pytest.mark.parametrize("grades,expected", [
    ([4.0], ["A+"]),
    ([3.8], ["A"]),
    ([3.4], ["A-"]),
    ([3.1], ["B+"]),
    ([2.8], ["B"]),
    ([2.4], ["B-"]),
    ([2.1], ["C+"]),
    ([1.8], ["C"]),
    ([1.4], ["C-"]),
    ([1.1], ["D+"]),
    ([0.8], ["D"]),
    ([0.1], ["D-"]),
    ([0.0], ["E"]),
    ([-1.0], ["E"]),
    ([4.0, 3.8, 3.4], ["A+", "A", "A-"]),
    ([2.8, 2.4, 2.1], ["B", "B-", "C+"]),
    ([1.8, 1.4, 1.1], ["C", "C-", "D+"]),
    ([0.8, 0.1, 0.0], ["D", "D-", "E"]),
    ([], []),
    ([3.85, 2.95, 1.95, 0.95], ["A", "B", "C", "D"]),
])
def test_numerical_letter_grade(grades, expected):
    result = numerical_letter_grade(grades)
    assert result == expected

@pytest.mark.parametrize("invalid_input", [
    ["A"],
    ["3.5"],
    [None],
])
def test_numerical_letter_grade_invalid_input(invalid_input):
    with pytest.raises((TypeError, ValueError)):
        numerical_letter_grade(invalid_input)

def test_numerical_letter_grade_none_input():
    with pytest.raises(TypeError):
        numerical_letter_grade(None)

def test_numerical_letter_grade_non_list_input():
    with pytest.raises(TypeError):
        numerical_letter_grade(3.5)

def test_numerical_letter_grade_boolean_input():
    with pytest.raises(TypeError):
        numerical_letter_grade([True])
    with pytest.raises(TypeError):
        numerical_letter_grade([False])

def validate_numeric_input(grades):
    if not isinstance(grades, list):
        raise TypeError("Input must be a list")
    if grades is None:
        raise TypeError("Input cannot be None")
    for grade in grades:
        if not isinstance(grade, (int, float)):
            raise TypeError("All grades must be numeric")