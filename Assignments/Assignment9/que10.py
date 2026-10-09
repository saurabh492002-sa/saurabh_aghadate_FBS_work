# 10. Write a program to reverse a number using recursion.


def reverse(n, rev=0):
    if n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        return reverse(n // 10, rev)

    return rev


n = int(input("Enter the number : "))

res = reverse(n)

print(f"Reverse of number is : {res}")