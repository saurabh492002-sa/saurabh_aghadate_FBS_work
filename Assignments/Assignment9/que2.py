# 2. Write a program to check if given number is Armstrong or not 
# using recursive function.


def countDigits(n):
    if n == 0:
        return 0
    return 1 + countDigits(n // 10)


def armstrong(n, digits, original):
    if n == 0:
        return 0

    digit = n % 10

    return (digit ** digits) + armstrong(n // 10, digits, original)


n = int(input("Enter a number: "))

digits = countDigits(n)

sum = armstrong(n, digits, n)

if sum == n:
    print("Armstrong number")
else:
    print("Not an Armstrong number")