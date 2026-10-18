# 6. Python Program to Take in a String and Replace Every Blank Space
# with Hyphen


a = input("Enter the string : ")
b = ""

for i in a:
    if i == " ":
        b += "-"
    else:
        b += i

print(b)