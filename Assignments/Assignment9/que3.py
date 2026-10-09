# 3. Write a program to reverse a given number using recursive function.


def reverse(n, rev = 0):
    # rev = 0
    if n == 0:
        return rev
    return reverse(n // 10, rev * 10 + n % 10)

n = int(input("Enter the number : "))
res = reverse(n)
print(res)