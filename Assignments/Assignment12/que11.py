# 11. Python Program to replace every blank space with hyphen in a string.


a = input("Enter the string : ")

new = ""
for i in a:
    if i == " ":
        i = "-"
    new += i

print(new)