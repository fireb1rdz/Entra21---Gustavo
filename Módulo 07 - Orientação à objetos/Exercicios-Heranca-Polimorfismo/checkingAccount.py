"""Continuação do ex 3"""

from account import Account

class CheckingAccount(Account):
    "Essa classe representa uma conta corrente."
    def __init__(self, account_holder: str, limit: (float)) -> None:
        super().__init__(account_holder)
        self.__limit = limit


    def deposit(self, value: float):
        self.account_balance += value
        print(f"the deposit has been done sucessfully! The new account balance is {self.account_balance}")
    
    def withdraw(self, value: float) -> None:
        self.account_balance -= value
        print(f"the withdraw has been done sucessfully! The new account balance is {self.account_balance}")
    
    def transfer(self, account: Account, value: float):
        return super().transfer(account, value)