# 1. Write a program to find sum of following series using recursive functions:

# i. 1! + 2! + 3! + 4! +..... + n!
# Note : For fact and sum two recursive functions


def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)

def sos(n):
    if n == 0:
        return 0
    return fact(n) + sos(n - 1)


n = int(input("Enter the number : "))
res = sos(n)
print(f"Som of series is : {res}")


# def sos(n):
#     if(n == 0):
#         return 0
#     return sos(n - 1) + n

# res = sos(3)
# print(res)

    