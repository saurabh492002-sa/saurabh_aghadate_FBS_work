# 3. Python Program to Check if a Given Key Exists in a Dictionary or Not

a = {"Name" : "Saurabh", "Age" : 24, "Salary" : 55000, "Depar" : "AI & DS"}

key = input("Enter the Key : ")

found = False

for i in a:
    if i == key:
        found = True

if found == True:
    print("Found")
else:
    print("Not Found")