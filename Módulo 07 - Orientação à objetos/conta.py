"""Implementação da Conta"""

from __future__ import annotations

class Conta:
    """Conta representa uma conta bancária.
    
    Attributes:
        numero (str): Número identificador da conta.
        titular (str): Nome do titular da conta.
        saldo (float): Saldo da conta.
        limite (float): Limite da conta.
    """

    quantidade_contas = 0 # Atributo estático -> Pertence á classe e não ao objeto

    def __init__(self, numero: str, titular: str) -> None:
        if len(numero) != 9:
            raise AttributeError("número da conta deve possuir 9 dígitos")
        
    # Encapsulamento
        self.__numero = numero
        self.titular = titular # Está usando o @titular.setter para definir o valor
        self.__limite = 100
        self.__saldo = 0

        Conta.quantidade_contas += 1

        # Formata a visualização do objeto
    def __str__(self):
        return f"Titular: {self.__titular} | Saldo: {self.__saldo} | Limite: {self.__limite}"
    
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

    def depositar(self, valor):
        "Deposita um valor na conta"
        self.__saldo += valor

    def sacar(self, valor) -> bool:
        if (self.__saldo + self.__limite) < valor:
            print("Saldo indisponível para realizar a operação")
            return False
        
        if self.__saldo < valor:
            self.__limite -= valor - self.__saldo
            self.__saldo = 0
        else:
            self.__saldo -= valor
        
        return True
    
    def transferir(self, valor: float, conta_destino: Conta) -> None:
        """Transfere o valor de uma conta para outra se o (saldo + limite)
        for maior ou igual ao valor do saque
        
        Args:
            valor (float): Valor da transferência
            conta_destino (Conta): Conta de destino da transferência.
        """
        if (self.sacar(valor)):
            conta_destino.depositar(valor)
            print("Transferência realizada com sucesso.")

    @staticmethod
    def verifica_numero_conta(numero: str) -> bool:
        """Verifica se o número da conta é valido
        
        Args:
            numero(str): Número da conta.

        Returns:
            True caso o número da conta seja válido, False caso contrário.
        """
        return len(numero) == 9

if __name__ == "__main__":
    conta_gustavo = Conta("123456789", "gustavo")
    conta_teste = Conta("123456788", "teste")
    conta_gustavo.depositar(1000)
    conta_gustavo.transferir(1050, conta_teste)
    print(conta_teste)
    print(conta_gustavo)
    
    print(Conta.quantidade_contas)

    if Conta.verifica_numero_conta("123456788"):
        print("Número da conta é válido!")
    else:
        print("Número da conta é inválido")