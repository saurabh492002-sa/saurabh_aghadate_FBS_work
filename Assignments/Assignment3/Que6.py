# Write a program to calculate profit or loss.


cost_price = int(input("Enter cost price = "))
selling_price = int(input("Enter selling price = "))

if selling_price > cost_price:
    profit = (selling_price - cost_price)
    print(f"You earn profit = {profit}")
elif cost_price > selling_price:
    loss = (cost_price - selling_price)
    print(f"You in Loss = {loss}")
else:
    cost_price == selling_price
    print("No profit or loss")