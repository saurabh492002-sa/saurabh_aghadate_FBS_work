# 13. Python Program to count number of digits and letters in a string.


a = input("Enter the string : ")

digits = 0
letter = 0

for i in a :
    if i >= "a" and i <= "z" or i >= "A" and i <= "Z":
        letter += 1

    elif i >= "0" and i <= "9":
        digits += 1

print("Total No. of Digits : ", digits)
print("Total No. of Letters : ", letter)
