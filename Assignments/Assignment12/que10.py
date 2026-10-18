# 10.Python Program to Take in Two Strings and Display the Larger String
# without Using Built-in Functions


a = input("Enter 1st string : ")
b = input("Enter 2nd string : ")


count1 = 0
count2 = 0

for i in a:
    count1 += 1
for i in b:
    count2 += 1

if count1 > count2:
    print("Larger string : ", a)
elif count1 < count2:
    print("Larger string : ", b)
else:
    print("Both string are equal")