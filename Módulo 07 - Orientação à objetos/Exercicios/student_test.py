import pytest

from student import Aluno

def test_student_creation():
    student = Aluno("123123", "Gustavo", [10, 10, 10])

    assert student.nome == "Gustavo"
    assert student.notas == [10, 10 ,10]
    assert student.numero_matricula == "123123"