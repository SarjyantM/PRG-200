class BankAccount:
    def __init__(self, name, account_number, balance=0):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited NPR {amount} to {self.name} ({self.account_number}). New balance: NPR {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"Withdrew NPR {amount} from {self.name} ({self.account_number}). New balance: NPR {self.balance}")

    def get_balance(self):
        print(f"{self.name} ({self.account_number}): NPR {self.balance}")


accounts_data = [
    ("Ramesh Thapa", "A001", 5000),
    ("Sunita Karki", "A002", 0),
    ("Bikash Rai", "A003", 12000),
]

accounts = [BankAccount(name, acc_no, bal) for name, acc_no, bal in accounts_data]

accounts[1].deposit(3000)
accounts[2].withdraw(15000)
accounts[0].withdraw(2000)

print("---- Final Balances ----")
for acc in accounts:
    acc.get_balance()