# # WAP to convert days into years, weeks and days.

# day = int(input("Enter Days :"))

# year = day // 365

# remaining = day % 365

# week = remaining // 7

# days = remaining % 7

# print("You Enter = ", day)

# print("Year = ", year)

# # print(remaining)

# print("Week =", week)

# print("Days = ", days)



# Write a program to convert days into years, weeks and days.

days = int(input("Enter Days :"))

year = days // 365
# print(year)

remaining_days = days % 365
# print(remaining_days)

week = remaining_days // 7
# print(week)

day = remaining_days % 7
# print(day)

print(f"Total Days: {days} Year: {year} Week: {week} Day: {day}")


 
 


    