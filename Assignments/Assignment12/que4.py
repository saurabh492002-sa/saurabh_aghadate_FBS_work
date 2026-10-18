# 4. Python Program to Form a New String where the First Character and
# the Last Character have been Exchanged


# a = "aditya"
a = input("Enter the string. : ")

b = a[-1]

b = b + a[1:-1]

b = b + a[0]

print(b)