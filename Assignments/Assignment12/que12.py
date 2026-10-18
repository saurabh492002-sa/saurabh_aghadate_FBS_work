# 12. Python Program to count number of lowercase characters in a string.

a = input("Enter the string : ")

count = 0 
for i in a:
    if i >= "a" and i <= "z":
        count += 1

print("Count of lowercase character is : ", count)