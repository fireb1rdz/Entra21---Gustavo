import pytest

from agenda import Agenda
from agenda import Person

def test_add_person():
    agenda = Agenda("Agenda de contatos.")

    pessoa = Person("Gustavo Paganelli", "+55 47 9 9999-9999")
    agenda.adicionar_pessoa(pessoa)

    assert len(agenda.pessoas) == 1
    assert agenda.pessoas[0].name == "Gustavo Paganelli"

def test_add_person_failed(capfd):
    agenda = Agenda("Agenda de contatos.")

    for i in range(10):
        pessoa = Person(f"Pessoa {i}", f"+55 (47) 9 9999-999{i}")
        agenda.adicionar_pessoa(pessoa)
    
    pessoa2 = Person(f"Pessoa extra", f"+55 (47) 9 9999-9991")
    agenda.adicionar_pessoa(pessoa2)
    out, _ = capfd.readouterr()

    assert "Agenda lotada.\n" == out
    assert len(agenda.pessoas) == 10
    

def test_remove_person():
    agenda = Agenda("Agenda de contatos.")

    pessoa = Person("Gustavo Paganelli", "+55 47 9 9999-9999")
    agenda.adicionar_pessoa(pessoa)
    agenda.remover_pessoa(pessoa)
    assert len(agenda.pessoas) == 0
