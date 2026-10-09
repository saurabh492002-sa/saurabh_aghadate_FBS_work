# 7. Write a program to find sum of digits using recursion.


def sumDigit(n, sum = 0):
    if n > 0:
        d = n % 10
        sum = sum + d
        return sumDigit(n // 10, sum)
    return sum

n = 123
res = sumDigit(n)
print(res)



# n = 333
# sum = 0
# for i in range(n):
#     if n > 0:
#         d = n % 10
#         sum += d
#     n = n // 10
# print(sum)