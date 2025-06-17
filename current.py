from account import Account

class CurrentAccount(Account):
    def __init__(self, balance=0, overdraft_limit=1000):
        super().__init__(balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if 0 < amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            return True
        return False