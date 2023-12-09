

"""
3) Crie uma classe agenda que pode armazenar 10 pessoas e que seja capaz de realizar as seguintes operações:
adicionar_pessoa() - Adiciona uma pessoa na agenda.
remover_pessoa() - Remove uma pessoa pelo nome da agenda.
buscar_pessoa() - Busca uma pessoa pelo nome na agenda (Mostra todas as informações da pessoa encontrada).
listar_pessoas() - Mostra as informações de todas as pessoas da agenda.

As pessoas da agenda devem ser objetos da classe Pessoa (ex. 1).
"""

import re
class InvalidNameError(Exception):
    pass


class InvalidPhoneError(Exception):
    pass

class Person:
    """Person representa uma pessoa."""
    
    def __init__(self, name: str, phone: str):
        self.name = name
        self.phone = phone

    def __str__(self):
        return f"Nome: {self.name}"
        
    def __repr__(self):
        return f"Nome: {self.name}"
    
    @property
    def name(self):
        """str: Nome da pessoa."""
        return self.__name
    
    @name.setter
    def name(self, name: str):
        if not self.__is_name_valid(name):
            raise InvalidNameError()
        self.__name = name
        
    @property
    def phone(self):
        """str: Número de telefone."""
        return self.__phone
    
    @phone.setter
    def phone(self, phone: str):
        if not self.__is_phone_valid(phone):
            raise InvalidPhoneError()
        self.__phone = phone
        
    def __is_phone_valid(self, phone: str) -> bool:
        """Verifica se um número de telefone é valido (+55 47 9 9999-9999).
        
        Args:
            name (str): Número de telefone que será verificado.
            
        Returns:
            bool: True caso o número de telefone seja válido, False caso não seja.
        """
        phone_regex = r"\+55\s?(?:\([1-9]{2}\)|[1-9]{2})\s?(?:9\s?\d{4}[-.\s]?\d{4}|\d{4}[-.\s]?\d{4})"
        return re.match(phone_regex, phone)
        
    def __is_name_valid(self, name: str) -> bool:
        """Verifica se um nome é valido (Nome completo).
        
        Args:
            name (str): Nome que será verificado.
            
        Returns:
            bool: True caso o nome seja composto, False caso não seja.
        """
        return len(name.strip().split()) > 1

class Agenda:
    """A classe agenda contém pessoas. Podendo adicionar, remover, buscar e listar as pessoas."""
    
    def __init__(self, nome: str) -> None:

        self.nome = nome
        self.pessoas = []

    def adicionar_pessoa(self, pessoa: Person):
        """Adiciona uma pessoa na agenda.
        
        Args:
            pessoa (Person): objeto Person que será adicionado.
            
        """
        if len(self.pessoas) < 10:
            self.pessoas.append(pessoa)

    def remover_pessoa(self, pessoa: Person):
        """Remove uma pessoa na agenda.
        
        Args:
            pessoa (Person): objeto Person que será removido.
            
        """
        if pessoa in self.pessoas:
            self.pessoas.remove(pessoa)

    def buscar_pessoa(self, pessoa: Person):
        """Busca uma pessoa na agenda.
        
        Args:
            pessoa (Person): objeto Person que será buscada.
        """
        if pessoa in self.pessoas:
            print(f"""
Nome: {pessoa.name} 
Telefone: {pessoa.phone}""")
        else:
            print("Pessoa não localizada")
    
    def listar_pessoas(self):
        """Lista as pessoas na agenda."""

        for pessoa in self.pessoas:
            print(f"""
Nome: {pessoa.name} 
Telefone: {pessoa.phone}
""")

if __name__ == "__main__":
    gustavo = Person("Gustavo Paganelli", "+55 47 9 2000-0223")
    juliana = Person("Juliana Ferreira", "+55 47 9 4230-0356")
    agenda1 = Agenda("Agenda de contatos")
    agenda1.adicionar_pessoa(gustavo)
    agenda1.adicionar_pessoa(juliana)
    agenda1.listar_pessoas()