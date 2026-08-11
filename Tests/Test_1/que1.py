# 1. Write a program to find the area and perimeter of following figure (Accept the
# length, breadth and radius from user:

l = int(input("Enter the length : "))
b = int(input("Enter the breadth : "))
r = int(input("Enter the radius : "))

area = (l * b) + (3.14 * r**2) / 2

perimeter = ((2 * l ) + b + (3.14 * r))

print(f"Area is : {area} and Perimeter is : {perimeter}")