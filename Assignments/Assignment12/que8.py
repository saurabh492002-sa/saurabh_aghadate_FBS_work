# 8. Python Program to Remove the Characters of Odd Index Values in a String


a = input("Enter the string : ")

b = ""

count = 0

for i in a:
    count += 1

for i in range(0, count):
    if i % 2 == 0:
        b += a[i]

print("Your Odd Index Value is : ",b)