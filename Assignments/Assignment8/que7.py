# 7. Write a program to find sum of digits of a number.

def sumDigit():
    sum = 0

    n = int(input("Enter the number : "))

    while(n > 0):
        d = n % 10
        sum += d
        n = n // 10
    return sum
        

res = sumDigit()
print(f"Sum of digit of a number is : {res}")




# n = 123

# sum = 0

# while(n > 0):
#     d = n % 10
#     sum += d
#     n = n // 10
# print(sum)