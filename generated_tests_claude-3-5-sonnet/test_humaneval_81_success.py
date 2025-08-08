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
    ([4.0, 0.0], ["A+", "E"])
])
def test_numerical_letter_grade_parametrized(grades, expected):
    assert numerical_letter_grade(grades) == expected

def test_numerical_letter_grade_empty_list():
    assert numerical_letter_grade([]) == []

def test_numerical_letter_grade_single_grade():
    assert numerical_letter_grade([3.5]) == ["A-"]

def test_numerical_letter_grade_multiple_grades():
    assert numerical_letter_grade([4.0, 3.7, 2.5]) == ["A+", "A-", "B-"]

def test_numerical_letter_grade_boundary_values():
    assert numerical_letter_grade([4.0, 3.71, 3.31, 3.01, 2.71, 2.31, 2.01, 1.71, 1.31, 1.01, 0.71, 0.01]) == [
        "A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-"
    ]

def test_numerical_letter_grade_negative_values():
    assert numerical_letter_grade([-1.0, -2.0, -3.0]) == ["E", "E", "E"]

def test_numerical_letter_grade_zero():
    assert numerical_letter_grade([0.0]) == ["E"]

def test_numerical_letter_grade_exact_boundaries():
    assert numerical_letter_grade([3.7, 3.3, 3.0, 2.7, 2.3, 2.0, 1.7, 1.3, 1.0, 0.7, 0.0]) == [
        "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-", "E"
    ]
