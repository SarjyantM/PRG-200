# Movie Ticket Price Calculator

def ticket_price(seat_type, count):
    if seat_type == "regular":
        price_per_ticket = 350
    else:
        price_per_ticket = 650

    total_cost = price_per_ticket * count
    return total_cost

print(f"Regular x 2 = NPR {ticket_price('regular', 2)}")
print(f"Recliner x 3 = NPR {ticket_price('recliner', 3)}")