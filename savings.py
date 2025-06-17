from account import Account

class SavingsAccount(Account):
    def __init__(self, balance=0, interest_rate=0.02):
        super().__init__(balance)
        self.interest_rate = interest_rate  # 2% interest by default
        self.withdrawals = 0
        self.max_withdrawals = 3  # Optional: Max 3 withdrawals per month

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        return interest

    def withdraw(self, amount):
        if self.withdrawals >= self.max_withdrawals:
            print("Withdrawal limit reached for the month.")
            return False
        if super().withdraw(amount):
            self.withdrawals += 1
            return True
        return False

    def reset_withdrawals(self):
        self.withdrawals = 0