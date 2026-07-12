# Ride Fare Estimator

def estimate_fare(distance_km, vehicle_type, surge=1.0):
    if vehicle_type == "bike":
        rate_per_km = 25
    elif vehicle_type == "car":
        rate_per_km = 45
    else:
        rate_per_km = 0

    fare = distance_km * rate_per_km * surge
    return fare


print(f"Bike, 5km, no surge = NPR {estimate_fare(5, 'bike')}")
print(f"Car, 8km, no surge = NPR {estimate_fare(8, 'car')}")
print(f"Car, 8km, peak hour = NPR {estimate_fare(8, 'car', surge=1.5)}")