# Write a program to input electricity unit charges and calculate total electricity bill according to given condition:
# For first 50 unit Rs. 0.50/unit
# For next 100 units Rs. 0.75/unit
# For next 100 units Rs. 1.20/unit
# For unit above 250 Rs. 1.50/unit
# An additional surcharge of 20% is added to the bill 


unit = float(input("Enter unit of Electricity Bill : "))

bill = 0

if unit <= 50:
    bill = unit * 0.50
    # print (bill)
elif unit <= 150:
    bill = (50 * 0.50) + ((unit - 50) * 0.75)
    # print (bill)
elif unit <= 250:
    bill = (50 * 0.50) + (100 * 0.75) + ((unit - 150) * 1.20)
    # print (bill)
else:
    bill = (50 * 0.50) + (100 * 0.75) + (100 * 1.20) + ((unit - 250) * 1.50)
    # print (bill)


surcharge = bill * 20 / 100
total = bill + surcharge

print(f"Your Total Bill is = {total}")