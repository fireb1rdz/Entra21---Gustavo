import pytest

from person import Person, InvalidNameError, InvalidPhoneError

def test_person_creation():
    person = Person("Gustavo Paganelli", "+55 47 9 9999-9999")

    assert person.name == "Gustavo Paganelli"
    assert person.phone == "+55 47 9 9999-9999"

def test_invalid_name():
    with pytest.raises(InvalidNameError):
        person = Person("Gustavo", "+55 47 9 9999-9999")

def test_invalid_phone():
    with pytest.raises(InvalidPhoneError):
        person = Person("Gustavo Paganelli", "")