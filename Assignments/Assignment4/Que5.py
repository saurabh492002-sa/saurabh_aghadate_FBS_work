# WAP to print Fibonacci series upto n.
# fibonacci series = 1 2 3 5 8 13 21

# n = int(input("Enter the number : "))

# a = -1
# b = 1

# for i in range(n):
#     c = a + b
#     print(c)

# c = b
# b = a


n = int(input("Enter the number : "))


a = -1
b = 1

for i in range(n):
    c = a + b
    print(c)
    a = b 
    b = c






