# 3. Accept no. of passengers from user and per ticket cost. Then accept age of each
# passenger and then calculate total amount to ticket to travel for all of them based on
# following condition :
# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c. Others need to pay full.


passenger = int(input("Enter the number of passengers : "))
cost = int(input("Enter the ticket cost : "))
# age = int(input("Enter the your age : "))

total_amount = 0

for i in range(1, passenger + 1):

    # cost = int(input("Enter the ticket cost : "))
    age = int(input("Enter the your age : "))

    if age < 12:
        amount = cost * 0.30
        # total_amount += cost * 0.70
        total_amount += cost - amount
        print("You are in Childern Category")

    elif age > 59:
        amount = cost * 0.50
        # total_amount += cost * 0.50
        total_amount += cost - amount
        print("You are in Senior citizen Category")

    else:
        amount = cost
        total_amount += cost
        print("You are in Audelt Category")

print(f"Total amount of ticket to travel for all member is : {total_amount}")