# 15. Python Program to find larger string without using built-in functions.


a = input("Enter the 1st string : ")
b = input("Enter the 2nd string : ")

count_a = 0
count_b = 0

for i in a :
    count_a += 1

for i in b :
    count_b += 1

if count_a > count_b:
    print("1st string is larger.")
elif count_a < count_b:
    print("2st string is larger.")
else:
    print("Both string are same.")