# Mobile Data Pack Recharge

def recharge_cost(gb, validity_days=30):
    if gb == 1:
        price = 49
    elif gb == 2:
        price = 89
    elif gb == 5:
        price = 199
    elif gb == 10:
        price = 349
    else:
        price = 0

    print(f"{gb}GB pack valid for {validity_days} days = NPR {price}")
    return price


recharge_cost(1)
recharge_cost(5)
recharge_cost(10, 15)
