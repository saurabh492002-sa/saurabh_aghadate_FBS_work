# 9. Write a program to calculate the m to the power n using recursion.


def power(m, n):
    if n > 0:
        return m * power(m, n - 1)
    return 1


m = int(input("Enter the base : "))
n = int(input("Enter the power : "))

res = power(m, n)

print(f"Answer is : {res}")