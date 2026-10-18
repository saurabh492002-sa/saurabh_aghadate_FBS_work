# 5. Python Program to Count the Number of Vowels in a String


# a = "firstbit soluation"
a = input("Enter the string : ")

count = 0
for i in a:
    if i == "a" or  i == "e" or i == "i" or i == "o" or i == "u":
        count += 1

print("Number of vowels : ", count)