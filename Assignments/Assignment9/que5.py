# 5. Write a program to find factorial using recursion.

def fact(n):
    if n > 0:
        return n * fact(n - 1)
    return 1

n = int(input("Enter the number : "))
res = fact(n)
print(f"Factorial of number is : {res}")