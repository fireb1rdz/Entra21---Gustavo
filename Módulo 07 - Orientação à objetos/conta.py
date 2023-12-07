"""Implementação da Conta"""

class Conta:
    """Conta representa uma conta bancária.
    
    Attributes:
        numero (str): Número identificador da conta.
        titular (str): Nome do titular da conta.
        saldo (float): Saldo da conta.
        limite (float): Limite da conta.
    """

    def __init__(self, numero: str, titular: str) -> None:
        if len(numero) != 9:
            raise AttributeError("número da conta deve possuir 9 dígitos")
        
    # Encapsulamento
        self.__numero = numero
        self.titular = titular # Está usando o @titular.setter para definir o valor
        self.__limite = 100
        self.__saldo = 0
    
    @property
    def titular(self):
        return self.__titular
    
    @titular.setter
    def titular(self, novo_titular: str):
        self.__titular = novo_titular.title()

    @property
    def limite(self):
        return self.__limite
        
    @limite_setter
    def limite(self, novo_limite: float):
        self.__limite = novo_limite


if __name__ == "__main__":
    conta_gustavo = Conta("123456789", "gustavo")
    print(f"Nome na conta antes de formatar: {conta_gustavo.titular}")
    conta_gustavo.titular = "nelson"
    print(f"Nome na conta depois de formatar: {conta_gustavo.titular}")
    