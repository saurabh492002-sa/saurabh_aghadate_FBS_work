# Find the sum of three-digit numbers.
# d1 = 379 % 10 = 9
# num = 379 // 10 = 37

number = int(input("Enter your Three-Digit number."))

digit1 = number % 10  # suppose number 999 then ans = 9 # modulo (remainder)
# print(digit1)

num1 = number // 10   # ans = 99 because // gives without decimal
# print(num1)

digit2 = num1 % 10    # number 99 then ans = 9 # modulo (remainder)
# print(digit2)

num2 = num1 // 10    # ans 9 because // gives without decimal
# print(num2)

sum = digit1 + digit2 + num2

 

print(f"Sum of your Three-Digit number is : {sum}")