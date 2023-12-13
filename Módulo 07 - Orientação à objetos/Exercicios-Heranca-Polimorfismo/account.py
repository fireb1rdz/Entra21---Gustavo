"""
3) Crie uma superclasse Conta com os seguintes atributos: número da conta, titular e saldo. 
Essa superclasse deve implementar os seguintes métodos: depositar(), sacar(), transferir(). 
Implemente as subclasses: ContaCorrente (Possui um limite adicional para saque e transferências), ContaPoupança (Gera juros mensalmente), ContaInvestimento (Permite investir em ações). 
Cada conta possui uma taxa diferente para depósito conforme abaixo:
Conta corrente: 0.2%
Conta poupança: 0.5%
Conta investimento: 0.8%
"""
from __future__ import annotations
from abc import ABC, abstractmethod
from random import randint


class Account(ABC):
    """Essa superclasse representa uma conta."""
    def __init__(self, account_holder: str) -> None:
        self.__account_number = randint(0, 100_000)
        self.account_holder = account_holder
        self.__account_balance = 0
    
    @property
    def number(self):
        """(int): Número da conta"""
        return self.__account_number
    
    @property
    def balance(self):
        """(float): Saldo da conta."""
        return self.__account_balance
    
    @balance.setter
    def balance(self, value: float):
        if value < 0:
            raise ValueError("Saldo não pode ser negativo")
        self.__account_balance = value

    def deposit(self, value: float):
        tax = self.get_deposit_tax()

        self.__account_balance += value * (1 - tax)

    def withdraw(self, value: float) -> None:
        if self.__account_balance >= value:
            self.__account_balance -= value
            return True
        
        return False
    
    def transfer(self, account: Account, value: float):
        if (self.withdraw(value)):
            account.deposit(value)

    @abstractmethod
    def get_deposit_tax(self) -> float:
        """Retorna a taxa de depósito."""
