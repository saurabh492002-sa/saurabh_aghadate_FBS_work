# Write a program to check if given 3 digit number is a palindrome or not.
# (121 = palindrome)  number that reads same from left to right and right to left. 
# (124 = not a palindrome)


num = int(input("Enter a 3 digit number : "))

last_digit = num % 10
# print(last_digit)
first_digit = num // 100
# print(first_digit)

print(f"You entered = {num}")

if last_digit == first_digit:
    print("It is Palindrome")
else:
    print("It is not Palindrome")