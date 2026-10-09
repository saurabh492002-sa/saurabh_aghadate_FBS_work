# 6. Write a program to print Fibonacci series using recursion.
 
def fibonacci(n, a = -1, b = 1):
    if n > 0:
        c = a + b
        print(c)
        # b = a
        # c = b
        return fibonacci(n -1, b, c)
    return 0

n = int(input("Enter the number : "))
fibonacci(n)
# print(res)


# def fib(n, a = -1, b = 1):
#     if n > 0:
#         c = a + b
#         print(c)
#         return fib(n - 1, b, c)
#     return 0
# n = 5
# fib(n)