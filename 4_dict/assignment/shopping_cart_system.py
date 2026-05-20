# Shopping Cart System

cart = {
    "Laptop": {"price": 50000, "qty": 1},
    "Mouse": {"price": 500, "qty": 2}
}

# 1. Add Product


cart["Keyboard"] = {
    "price": 1500,
    "qty": 1
}

print("After Adding Product:")
print(cart)



# 2. Update Quantity


cart["Mouse"]["qty"] = 3

print("\nAfter Updating Quantity:")
print(cart)



# 3. Remove Product


del cart["Keyboard"]

print("\nAfter Removing Product:")
print(cart)



# 4. Calculate Total Bill


total = 0

for product, details in cart.items():

    item_total = details["price"] * details["qty"]

    total += item_total

print("\nTotal Bill:", total)



# 5. Find Most Expensive Product


most_expensive = max(
    cart,
    key=lambda item: cart[item]["price"]
)

print("Most Expensive Product:", most_expensive)


# 6. Apply 10% Discount


if total > 50000:

    discount = total * 0.10

    final_amount = total - discount

    print("Discount:", discount)
    print("Final Amount:", final_amount)

else:
    print("No Discount Applied")