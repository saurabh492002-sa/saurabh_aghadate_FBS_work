# Write a program to find print the following Fibonacci series using functions:
# 1 1 2 3 5 8 n terms

def fibonacci():

    a = -1
    b = 1

    n = int(input("Enter the number : "))

    for i in range(n):
        c = a + b
        print(c, end=' ')

        a = b
        b = c

fibonacci()




# def fibonacci():

#     a = -1
#     b = 1

#     n = int(input("Enter the number : "))

#     for i in range(n):
#         c = a + b
#         print(c, end = ' ')
       
#         a = b
#         b = c

# res = fibonacci()

# print(res)

