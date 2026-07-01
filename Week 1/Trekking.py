print(" --- Trekking Trip Expense Splitter --- ")
friends = ["Sarjyant", "Anuprash", "Prajit", "Prashanna", "Kabit"]
expenses = {}
print("Enter the amount spent by each friend:")
for friend in friends:
    expenses[friend] = float(input(f"Amount spent by {friend}: Rs. "))
total_trip_cost = sum(expenses.values())
fair_share = total_trip_cost / 5

print("\n--- Trip Summary ---")
print(f"Total Group Expenditure: Rs. {total_trip_cost:.2f}")
print(f"Fair Share per Person:   Rs. {fair_share:.2f}")
print("--------------------")

debtors = []
creditors = []

for friend, amount_spent in expenses.items():
    balance = amount_spent - fair_share
    if balance < 0:
        debtors.append((friend, abs(balance)))
    elif balance > 0:
        creditors.append((friend, balance))

print("\n --- Exact Transaction Breakdown --- ")

debtor_index = 0
creditor_index = 0

while debtor_index < len(debtors) and creditor_index < len(creditors):
    debtor_name, debtor_owes = debtors[debtor_index]
    creditor_name, creditor_owed = creditors[creditor_index]
    
    transfer_amount = min(debtor_owes, creditor_owed)
    
    print(f"-> {debtor_name} owes Rs. {transfer_amount:.2f} to {creditor_name}")
    
    debtor_owes -= transfer_amount
    creditor_owed -= transfer_amount
    
    if debtor_owes < 0.01:
        debtor_index += 1
    else:
        debtors[debtor_index] = (debtor_name, debtor_owes)
        
    if creditor_owed < 0.01:
        creditor_index += 1
    else:
        creditors[creditor_index] = (creditor_name, creditor_owed)

print("-----------------------------------")