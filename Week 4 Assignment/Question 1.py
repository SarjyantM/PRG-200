# Small Shop Billing and Inventory System By Sarjyant

inventory = {
    "rice": {"price": 120, "stock": 20},
    "milk": {"price": 90, "stock": 10},
    "bread": {"price": 60, "stock": 15},
    "eggs": {"price": 15, "stock": 30}
}

cart = {
    "rice": 2,
    "milk": 3,
    "eggs": 12
}

def process_order(inventory, cart):
    total = 0
    print("---- Bill ----")

    for item in cart:
        quantity = cart[item]

        if quantity <= inventory[item]["stock"]:
            cost = inventory[item]["price"] * quantity
            total = total + cost
            inventory[item]["stock"] = inventory[item]["stock"] - quantity
            print(item, "x" + str(quantity), "= NPR", cost)
        else:
            print("Sorry, not enough stock for", item)

    print("Grand Total: NPR", total)
    print("--------------")

    stock_text = "Updated stock: "
    for item in cart:
        stock_text = stock_text + item + "=" + str(inventory[item]["stock"]) + ", "
    print(stock_text[:-2])

process_order(inventory, cart)