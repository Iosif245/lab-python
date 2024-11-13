class Account:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount

class SavingsAccount(Account):
    def __init__(self, balance=0, interest_rate=0.05):
        super().__init__(balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        return self.balance * self.interest_rate

class CheckingAccount(Account):
    def __init__(self, balance=0, overdraft_limit=500):
        super().__init__(balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount > self.balance + self.overdraft_limit:
            print("Overdraft limit exceeded")
        else:
            self.balance -= amount

savings = SavingsAccount(balance=1000, interest_rate=0.05)
checking = CheckingAccount(balance=500, overdraft_limit=200)

print("Savings Account:")
savings.deposit(500)
print("Balance after deposit:", savings.balance)
print("Interest:", savings.calculate_interest())

print("\nChecking Account:")
checking.withdraw(600)
print("Balance after withdrawal:", checking.balance)
checking.withdraw(200)  # Exceeds overdraft limit
print("Balance after second withdrawal:", checking.balance)