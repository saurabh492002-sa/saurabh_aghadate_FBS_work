# Write a program to reverse three-digit number.


num = int(input("Enter Three_Digit number. :"))

num1 = num // 10
# print(num1)

last_digit = num % 10
print(last_digit)

middle_digit = num1 % 10
print(middle_digit)

first_digit = num // 100
print(first_digit)


reverse = (last_digit * 100) + (middle_digit * 10) + (first_digit)

print(f"Reverse of your digit is : {reverse}")



# num1 = num //100
# print(num1)


# num2 = num // 10 % 10
# print(num2) 


# num3 = num % 10
# print(num3)


# reverse = (num3 * 100) + (num2 * 10) + num1
# print(reverse)