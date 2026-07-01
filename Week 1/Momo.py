print(" --- MOMO SHOP PROFIT TRACKER --- ")

cost_price = float(input("Enter cost price per plate (NPR): "))
selling_price = float(input("Enter selling price per plate (NPR): "))
plates_sold = int(input("Enter number of plates sold today: "))

total_revenue = selling_price * plates_sold
total_cost = cost_price * plates_sold
total_profit = total_revenue - total_cost
profit_margin = (total_profit / total_revenue) * 100

print("\n --- DAILY PROFIT SUMMARY --- ")
print(f"Plates Sold      : {plates_sold}")
print(f"Total Revenue    : NPR {total_revenue:.2f}")
print(f"Total Cost       : NPR {total_cost:.2f}")
print(f"Total Profit     : NPR {total_profit:.2f}")
print(f"Profit Margin    : {profit_margin:.2f}%")