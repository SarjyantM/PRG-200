# Simple ATM Simulator By Sarjyant

accounts = {
    "A001": {"name": "Ramesh Thapa", "balance": 15000, "pin": "1234"},
    "A002": {"name": "Sunita Karki", "balance": 8500, "pin": "5678"},
    "A003": {"name": "Bikash Rai", "balance": 22000, "pin": "9012"}
}


def atm(account_id, pin, action, amount=0):
    if account_id not in accounts:
        print("Account not found")
        return

    if pin != accounts[account_id]["pin"]:
        print("Incorrect PIN")
        return

    if action == "balance":
        print(accounts[account_id]["name"], "- Balance: NPR", accounts[account_id]["balance"])
    elif action == "deposit":
        accounts[account_id]["balance"] += amount
        print("New balance: NPR", accounts[account_id]["balance"])
    elif action == "withdraw":
        if amount > accounts[account_id]["balance"]:
            print("Insufficient funds")
        else:
            accounts[account_id]["balance"] -= amount
            print("New balance: NPR", accounts[account_id]["balance"])


atm("A001", "1234", "balance")
atm("A002", "0000", "withdraw", 2000)
atm("A002", "5678", "deposit", 3000)
atm("A003", "9012", "withdraw", 25000)
atm("A004", "1111", "balance")