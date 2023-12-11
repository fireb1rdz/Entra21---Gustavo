import pytest

from student import Aluno

def test_student_creation():
    student = Student("123123", "Gustavo", [10, 10, 10])

    assert student.name == "Gustavo"
    assert student.grades == [10, 10 ,10]
    assert student.numero_matricula == "123123"