print(" --- Foreign Remittance Convertor --- ")

USD = float(input("Enter amt sent in USD : "))
exchange_rate = float(input("Enter exchange rate (1 USD = ? NPR) : "))
fee_percentage = float(input("Enter service fee percentage (%) : "))

converted_npr = USD * exchange_rate
fee_charged = (fee_percentage / 100) * converted_npr
final_amount = converted_npr - fee_charged
 
print("\n--- REMITTANCE SUMMARY ---")
print(f"Amount Sent          : USD {USD}")
print(f"Exchange Rate        : 1 USD = NPR {exchange_rate}")
print(f"Converted Amount     : NPR {converted_npr}")
print(f"Service Fee ({fee_percentage}%)   : NPR {fee_charged}")
print(f"Final Amount Received: NPR {final_amount}")
 

 