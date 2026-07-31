# WAP to calculate selling price of book based on cost price and discount.


cost_price = int(input("Enter Cost Price of Book:"))
discount = int(input("Enter how much Discount you want :"))

price = cost_price * discount / 100

selling_price = cost_price - price

print(f"Selling Price of Book is = {selling_price}")