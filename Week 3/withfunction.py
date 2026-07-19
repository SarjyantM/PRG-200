# convert $5 $50 $500 dollars into nepali rupee using function


def exchange(amt):
    exchange_rate = 152.53
    return amt * exchange_rate

print(f"$5 = NPR {exchange(5)}")
print(f"$50 = NPR {exchange(50)}")
print(f"$500 = NPR {exchange(500)}")
