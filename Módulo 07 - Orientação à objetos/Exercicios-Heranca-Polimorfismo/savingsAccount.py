from account import Account

class SavingAccount(Account):
    """Representa uma conta-poupança"""
    interest_percentage = 0.58

    def __init__(self, account_holder: str, initial_balance: float) -> None:
        super().__init__(account_holder)
        self.initial_balance = initial_balance
        
    def generate_interest(self):
        """Gera o juros mensal da conta"""
        self.balance += self.balance * (SavingAccount.interest_percentage / 100)

    def get_deposit_tax(self) -> float:
        """Informa a taxa de depósito"""
        return 0.5