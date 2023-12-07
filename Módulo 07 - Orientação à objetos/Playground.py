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
        self.__saldo = 100
    
    @property
    def titular(self):
        return self.__titular
    
    @titular.setter
    def titular(self, novo_titular: str):
        self.__titular = novo_titular.title()

    @property
    def limite(self):
        return self.__limite
        
    @limite.setter
    def limite(self, novo_limite: float):
        self.__limite = novo_limite
    
    @property
    def saldo(self):
        return self.__saldo
    
    def consulta_saldo(self):
        return self.__saldo
    
    def consulta_limite(self):
        return self.__limite
    
    def saque(self, valor_saque: float):
        self.__saldo -= valor_saque
        print(f"Saque realizado com sucesso! seu saldo atual é {self.__saldo}")

    def deposito(self, valor_deposito: float):
        self.__saldo += valor_deposito
        print(f"Depósito realizado com sucesso! seu saldo atual é {self.__saldo}")


if __name__ == "__main__":
    conta_gustavo = Conta("123456789", "gustavo")
    print(conta_gustavo.consulta_saldo())
    conta_gustavo.deposito(1000)
    print(conta_gustavo.consulta_saldo())
    conta_gustavo.saque(200)
    print(conta_gustavo.consulta_saldo())