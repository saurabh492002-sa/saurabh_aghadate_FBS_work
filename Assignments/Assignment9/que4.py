# 4. Write a program to find sum of n numbers using recursion.


def sumNumber(n):
    if n > 0:
        return n + sumNumber(n - 1)
    return 0

n = int(input("Enter the number : "))
res = sumNumber(n)
print(f"Sum of number is : {res}")