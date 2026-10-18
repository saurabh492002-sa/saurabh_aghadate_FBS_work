# 9. Python Program to Calculate the Number of Words and the Number of
# Characters Present in a String



a = input("Enter the string : ")

words = 1
char = 0

for i in a:
    char += 1

    if i == " ":
        words += 1
    # else:
        # char += 1

print("Your String : ", a)
print("Total Words : ", words)
print("Total Character : ", char)