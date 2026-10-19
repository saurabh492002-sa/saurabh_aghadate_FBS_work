# 7. Python Program to Remove the Given Key from a Dictionary

a = {"Name" : "Saurabh", "Age" : 24, "Salary" : 55000, "Depar" : "AI & DS"}

b = input("Enter the Key to remove : ")

dic = {}

for i in a:
    if i != b:
        dic[i] = a[i]

print("Dictionary after removing key :", dic)