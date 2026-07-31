# Accept age of five people and also per person ticket amount 
# and then calculate total amount to ticket to travel for all of them based on following condition:
# a. Children (below 12) = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c.Others need to pay full.


age1 = int(input("Enter 1st person age : "))
ticket1 = int(input("Enter 1st person ticket amount : "))

if age1 < 12:
    total1 = (ticket1 * 30) / 100
    print(f"Total = {total1}")
elif age1 > 59:
    total2 = (ticket1 * 50) / 100
    print(f"Total = {total2}")
else:
    total3 = ticket1
    print(f"Total = {total3}")




















# age1 = int(input("Enter 1st person age : "))
# ticket1 = int(input("Enter 1st person ticket amount : "))

# Total_price = 0

# if age1 < 12:
#     Total_price = Total_price + (ticket1 * 0.30)
# elif age1 > 59:
#     Total_price = Total_price + (ticket1 * 0.50)
# else:
#     Total_price = Total_price + Total_price

# print(Total_price)