# 1. Write a program to calculate area of rectangle
# (Use Functions in all programs)


def areaRectangle(l,b):
    return l * b

l = int(input("Enter the length : "))
b = int(input("Enter the bredth : "))

res = areaRectangle(l,b)
print(f"Area of rectangel is : {res}")


