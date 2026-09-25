# 10. Write a program to check if entered year is a leap year or not.

def leapYear():
    year = int(input("Enter the year : "))

    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        print(f"{year} is Leap Year")
    else:
        print(f"{year} is not Leap Year")

leapYear()
