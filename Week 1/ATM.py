number = 1245
balance = 50000
count = 3

for i in range(count):
    pin = int(input("Enter the pin: "))

    if pin == number:
        print("PIN verified!")
        
        choice = input("1. Check Balance\n2. Withdraw\nEnter choice: ")
        
        if choice == "1":
            print(f"Your balance is: Rs. {balance}")
            # no break here — loop continues, will ask for PIN again
        elif choice == "2":
            amount = float(input("Enter amount to withdraw: "))
            if amount > balance:
                print("Insufficient balance.")
            else:
                balance -= amount
                print(f"Collect cash. Remaining balance: Rs. {balance}")
            break   # 👈 now break is inside the "withdraw" branch only

    else:
        print("Invalid pin")
        if i == count - 1:
            print("Card blocked")