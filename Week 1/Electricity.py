print(" --- NEA Electricity Unit Cost --- ")

previous_reading = float(input("Enter previous meter reading (kWh): "))
current_reading = float(input("Enter current meter reading (kWh): "))
rate_per_unit = float(input("Enter rate per unit (NPR): "))
service_charge = float(input("Enter fixed monthly service/meter charge (NPR): "))
 
units_consumed = current_reading - previous_reading
energy_cost = units_consumed * rate_per_unit
total_bill = energy_cost + service_charge
 
print("\n---ELECTRICITY BILL SUMMARY ---")
print(f"Previous Reading  : {previous_reading} kWh")
print(f"Current Reading   : {current_reading} kWh")
print(f"Units Consumed    : {units_consumed:.2f} kWh")
print(f"Rate per Unit     : NPR {rate_per_unit:.2f}")
print(f"Energy Cost       : NPR {energy_cost:.2f}")
print(f"Service Charge    : NPR {service_charge:.2f}")
print(f"Total Bill        : NPR {total_bill:.2f}")
 
